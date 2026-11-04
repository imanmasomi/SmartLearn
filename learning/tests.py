from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Choice, Question, Quiz, QuizAttempt, Subject, Topic


User = get_user_model()


class SmartLearnTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="student1",
            password="test-password-123",
        )
        self.other_user = User.objects.create_user(
            username="student2",
            password="test-password-123",
        )

        self.subject = Subject.objects.create(
            owner=self.user,
            name="Python",
            description="Python fundamentals",
        )

        self.topic = Topic.objects.create(
            subject=self.subject,
            title="Variables",
        )

        self.client.force_login(self.user)

    def test_topic_progress_is_calculated_correctly(self):
        Topic.objects.create(
            subject=self.subject,
            title="Functions",
            is_completed=True,
        )

        response = self.client.get(
            reverse("topic_list", args=[self.subject.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_topics"], 2)
        self.assertEqual(response.context["completed_topics"], 1)
        self.assertEqual(response.context["progress"], 50)

    def test_user_cannot_view_another_users_subject_topics(self):
        other_subject = Subject.objects.create(
            owner=self.other_user,
            name="Private subject",
        )

        response = self.client.get(
            reverse("topic_list", args=[other_subject.pk])
        )

        self.assertEqual(response.status_code, 404)

    def test_topic_completion_toggle_requires_post(self):
        url = reverse(
            "topic_toggle",
            args=[self.subject.pk, self.topic.pk],
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

        self.topic.refresh_from_db()
        self.assertFalse(self.topic.is_completed)

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

        self.topic.refresh_from_db()
        self.assertTrue(self.topic.is_completed)

    def test_subject_creation_assigns_current_user_as_owner(self):
        response = self.client.post(
            reverse("subject_create"),
            {
                "name": "Django",
                "description": "Web development",
            },
        )

        self.assertEqual(response.status_code, 302)

        subject = Subject.objects.get(name="Django")
        self.assertEqual(subject.owner, self.user)

    def test_quiz_attempt_records_correct_score(self):
        quiz = Quiz.objects.create(
            subject=self.subject,
            title="Python basics",
        )

        question = Question.objects.create(
            quiz=quiz,
            text="What is Python?",
        )

        correct_choice = Choice.objects.create(
            question=question,
            text="A programming language",
            is_correct=True,
        )

        Choice.objects.create(
            question=question,
            text="A database",
            is_correct=False,
        )

        response = self.client.post(
            reverse("quiz_take", args=[quiz.pk]),
            {
                f"question_{question.pk}": str(correct_choice.pk)
            },
        )

        self.assertEqual(response.status_code, 302)

        attempt = QuizAttempt.objects.get(
            user=self.user,
            quiz=quiz,
        )

        self.assertEqual(attempt.score, 1)
        self.assertEqual(attempt.total_questions, 1)
