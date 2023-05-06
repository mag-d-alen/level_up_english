from django import forms
from silky.models import TestQuestion, TestAnswer

attendance_choices = (
    ('absent', 'Afwezig'),
    ('allowedabsent', 'Geoorloofd afwezig'),
    ('present', 'Aanwezig'),
)


class TestQuestionForm(forms.ModelForm):
    class Meta:
        model = TestQuestion
        fields = ['question', ]
        widgets = {
            'question': forms.RadioSelect(choices=attendance_choices)
        }
