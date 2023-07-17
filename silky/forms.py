from django import forms
from silky.models import TestQuestion


class TestQuestionForm(forms.ModelForm):
    class Meta:
        model = TestQuestion
        fields = '__all__'

