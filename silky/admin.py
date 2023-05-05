from django.contrib import admin
from silky.models import TestQuestion, TestAnswer


# Register your models here.
class TestQuestionAdmin(admin.ModelAdmin):
    model = TestQuestion
    list_display = ["question", "answer_1", "answer_2", "answer_3", "answer_4",
                    "correct_answer"]


class TestAnswersAdmin(admin.ModelAdmin):
    model = TestAnswer
    list_display = ["test_question", "author", "answer"]


admin.site.register(TestQuestion, TestQuestionAdmin)
admin.site.register(TestAnswer, TestAnswersAdmin)
