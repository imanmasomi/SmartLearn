    def test_choice_from_another_question_is_not_accepted(self):
        quiz = Quiz.objects.create(
            subject=self.subject,
            title="Python security test",
        )

        first_question = Question.objects.create(
            quiz=quiz,
            text="First question",
        )

        second_question = Question.objects.create(
            quiz=quiz,
            text="Second question",
        )

        Choice.objects.create(
            question=first_question,
            text="First correct choice",
            is_correct=True,
        )

        second_correct_choice = Choice.objects.create(
            question=second_question,
            text="Second correct choice",
            is_correct=True,
        )

        response = self.client.post(
            reverse("quiz_take", args=[quiz.pk]),
            {
                f"question_{first_question.pk}": str(second_correct_choice.pk),
            },
        )

        self.assertEqual(response.status_code, 302)

        attempt = QuizAttempt.objects.get(
            user=self.user,
            quiz=quiz,
        )

        self.assertEqual(attempt.score, 0)
        self.assertEqual(attempt.total_questions, 2)
