from django.conf import settings
from django.db import models


class Subject(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=150)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class StudySession(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="study_sessions")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="study_sessions")
    title = models.CharField(max_length=150)
    scheduled_for = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["scheduled_for"]

    def __str__(self):
        return self.title


class Quiz(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quiz_attempts")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="attempts")
    score = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.quiz} ({self.score}/{self.total_questions})"


class Review(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="reviews")
    due_at = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["due_at"]

    def __str__(self):
        return f"Review: {self.topic}"
