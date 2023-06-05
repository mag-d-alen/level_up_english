from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, ListView

from accounts.forms import CustomUserCreationForm
from silky.forms import TestQuestionForm
from silky.models import TestQuestion, TestAnswer


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class RegisterPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class TestQuestionListView(ListView):
    model = TestQuestion
    template_name = 'question_list.html'
    context_object_name = "questions"

    def get_queryset(self):
        qs = TestQuestion.objects.exclude(answers__author=self.request.user)
        return qs


def add_question_view(request):
    form = TestQuestionForm()
    if request.method == 'POST':
        form = TestQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')
    else:
        return render(request, 'partials/question_form.html', {'form': form})

@require_http_methods(['GET', 'POST'])
def edit_question_view(request, pk):
    question = TestQuestion.objects.get(pk=pk)
    if request.method == 'POST':
        data = {key:value for (key, value) in request.POST.items()}
        TestQuestion.objects.filter(id = pk).update(**data)
        message =' <p>Congratulations, the question was updated successfully</p>'
        return HttpResponse(message, status=200)
    else:
        return render(request, 'partials/edit_question.html', {'q': question})


def question_detail_view(request, pk):
    question = TestQuestion.objects.filter(pk=pk).first()
    if request.method == "POST":
        answer = request.POST.get("q.pk")
        data = {"answer": answer, "test_question": question, "author": request.user}
        new_answer = TestAnswer.objects.create(**data)
        new_answer.save()
        return redirect('results')
    else:
        return render(request, 'question.html', {'q': question})


def user_results_view(request):
    questions = list(TestQuestion.objects.filter(answers__author=request.user).order_by("-answers__id"))
    results = [{"question": q.question, "correct": q.correct_answer, "1": q.answer_1, "2": q.answer_2, "3": q.answer_3,
                "4": q.answer_4, "response": TestAnswer.objects.filter(author=request.user, test_question=q)
        .values().first()["answer"], "is_right": TestAnswer.objects.filter(author=request.user, test_question=q)
                                                 .values().first()["answer"] == q.correct_answer} for q in questions]
    return render(request, 'test_results.html', {'results': results})
