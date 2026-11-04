
from django import forms

from .models import (
    Subject,
    Topic,
    StudySession,
    Quiz,
    Question,
    Choice,
)


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "e.g. Mathematics"
            }),
            "description": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "A short description about this subject"
            }),
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Variables and Data Types"
            }),
        }


class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = [
            "subject",
            "title",
            "scheduled_for",
            "duration_minutes",
        ]

        widgets = {
            "subject": forms.Select(),
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Python Practice"
            }),
            "scheduled_for": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
            "duration_minutes": forms.NumberInput(attrs={
                "min": 1,
                "placeholder": "30"
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields["subject"].queryset = Subject.objects.filter(
                owner=user
            )

    def clean_duration_minutes(self):
        duration = self.cleaned_data["duration_minutes"]

        if duration < 1:
            raise forms.ValidationError(
                "Duration must be at least 1 minute."
            )

        return duration


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["subject", "title", "description"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Python Basics Quiz"
            }),
            "description": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Describe this quiz"
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields["subject"].queryset = Subject.objects.filter(
                owner=user
            )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text"]

        widgets = {
            "text": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Write your question here"
            }),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["text", "is_correct"]

        widgets = {
            "text": forms.TextInput(attrs={
                "placeholder": "Write an answer option"
            }),
        }

