from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView

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


def question_detail_view(request, pk=8):
    question = TestQuestion.objects.filter(pk=pk).first()
    if request.method == "POST":
        answer = request.POST.get("q.pk")
        print("-------->", answer)
        data = {"answer": answer, "test_question": question, "author": request.user}
        print(data)
        new_answer = TestAnswer.objects.create(**data)
        new_answer.save()
        results = TestAnswer.objects.filter(author=request.user)
        return redirect('results')
    else:
        return render(request, 'question.html', {'q': question})


def user_results_view(request):
    questions = list(TestQuestion.objects.filter(answers__author=request.user))
    results = [{"question":q.question, "correct": q.correct_answer,"1":q.answer_1, "2":q.answer_2, "3":q.answer_3,
                "4":q.answer_4,"response":TestAnswer.objects.filter(author=request.user, test_question=q)
                    .values().first()["answer"]} for q in questions]
    print(results)
    return render(request, 'test_results.html', {'results': results})
