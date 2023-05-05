from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class TestQuestion(models.Model):
    class Meta:
        verbose_name = "Test Question"

    question = models.CharField(max_length=300)
    answer_1 = models.CharField(max_length=300)
    answer_2 = models.CharField(max_length=300)
    answer_3 = models.CharField(max_length=300)
    answer_4 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.question} {self.correct_answer}"


class TestAnswer(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name="answers")
    answer = models.CharField(max_length=1)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


def __str__(self): return f"{self.test_question},{self.answer}"
