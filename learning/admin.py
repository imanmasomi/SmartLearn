from django.contrib import admin
from .models import Subject, Topic, StudySession, Quiz, Question, Choice, QuizAttempt, Review

admin.site.register([Subject, Topic, StudySession, Quiz, Question, Choice, QuizAttempt, Review])
