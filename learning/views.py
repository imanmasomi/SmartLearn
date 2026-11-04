
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import (
    SubjectForm,
    TopicForm,
    StudySessionForm,
    QuizForm,
    QuestionForm,
    ChoiceForm,
)

from .models import (
    Subject,
    Topic,
    StudySession,
    Quiz,
    Question,
    Choice,
    QuizAttempt,
)


# Dashboard

@login_required
def dashboard(request):
    subjects = Subject.objects.filter(owner=request.user)

    sessions = StudySession.objects.filter(
        owner=request.user,
        is_completed=False
    )[:5]

    attempts = QuizAttempt.objects.filter(
        user=request.user
    ).select_related("quiz")[:5]

    return render(request, "learning/dashboard.html", {
        "subjects": subjects,
        "sessions": sessions,
        "attempts": attempts,
    })


# Subject views

@login_required
def subject_list(request):
    subjects = Subject.objects.filter(owner=request.user)

    return render(request, "learning/subjects.html", {
        "subjects": subjects
    })


@login_required
def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)

        if form.is_valid():
            subject = form.save(commit=False)
            subject.owner = request.user
            subject.save()

            messages.success(request, "Subject added successfully!")
            return redirect("subjects")
    else:
        form = SubjectForm()

    return render(request, "learning/subject_form.html", {
        "form": form
    })


@login_required
def subject_edit(request, pk):
    subject = get_object_or_404(
        Subject,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()
            messages.success(request, "Subject updated successfully!")
            return redirect("subjects")
    else:
        form = SubjectForm(instance=subject)

    return render(request, "learning/subject_form.html", {
        "form": form,
        "is_edit": True
    })


@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(
        Subject,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        subject.delete()
        messages.success(request, "Subject deleted successfully!")
        return redirect("subjects")

    return render(
        request,
        "learning/subject_confirm_delete.html",
        {"subject": subject}
    )


# Topic views

@login_required
def topic_list(request, subject_id):
    subject = get_object_or_404(
        Subject,
        pk=subject_id,
        owner=request.user
    )

    topics = subject.topics.all()
    total_topics = topics.count()
    completed_topics = topics.filter(is_completed=True).count()

    progress = 0

    if total_topics > 0:
        progress = round(completed_topics / total_topics * 100)

    return render(request, "learning/topics.html", {
        "subject": subject,
        "topics": topics,
        "form": TopicForm(),
        "total_topics": total_topics,
        "completed_topics": completed_topics,
        "progress": progress,
    })


@login_required
@require_POST
def topic_create(request, subject_id):
    subject = get_object_or_404(
        Subject,
        pk=subject_id,
        owner=request.user
    )

    form = TopicForm(request.POST)

    if form.is_valid():
        topic = form.save(commit=False)
        topic.subject = subject
        topic.save()

        messages.success(request, "Topic added successfully!")
    else:
        messages.error(request, "Please enter a valid topic title.")

    return redirect("topic_list", subject_id=subject.id)


@login_required
def topic_edit(request, subject_id, pk):
    subject = get_object_or_404(
        Subject,
        pk=subject_id,
        owner=request.user
    )

    topic = get_object_or_404(
        Topic,
        pk=pk,
        subject=subject
    )

    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)

        if form.is_valid():
            form.save()
            messages.success(request, "Topic updated successfully!")

            return redirect(
                "topic_list",
                subject_id=subject.id
            )
    else:
        form = TopicForm(instance=topic)

    return render(request, "learning/topic_edit.html", {
        "form": form,
        "subject": subject,
        "topic": topic,
    })


@login_required
def topic_delete(request, subject_id, pk):
    subject = get_object_or_404(
        Subject,
        pk=subject_id,
        owner=request.user
    )

    topic = get_object_or_404(
        Topic,
        pk=pk,
        subject=subject
    )

    if request.method == "POST":
        topic.delete()
        messages.success(request, "Topic deleted successfully!")

        return redirect(
            "topic_list",
            subject_id=subject.id
        )

    return render(
        request,
        "learning/topic_confirm_delete.html",
        {
            "subject": subject,
            "topic": topic,
        }
    )


@login_required
@require_POST
def topic_toggle(request, subject_id, pk):
    subject = get_object_or_404(
        Subject,
        pk=subject_id,
        owner=request.user
    )

    topic = get_object_or_404(
        Topic,
        pk=pk,
        subject=subject
    )

    topic.is_completed = not topic.is_completed
    topic.save(update_fields=["is_completed"])

    return redirect(
        "topic_list",
        subject_id=subject.id
    )


# Study Session views

@login_required
def session_list(request):
    sessions = StudySession.objects.filter(
        owner=request.user
    ).select_related("subject")

    return render(request, "learning/sessions.html", {
        "sessions": sessions,
    })


@login_required
def session_create(request):
    if request.method == "POST":
        form = StudySessionForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():
            session = form.save(commit=False)
            session.owner = request.user
            session.save()

            messages.success(
                request,
                "Study session created successfully!"
            )

            return redirect("sessions")
    else:
        form = StudySessionForm(user=request.user)

    return render(request, "learning/session_form.html", {
        "form": form,
    })


@login_required
@require_POST
def session_toggle(request, pk):
    session = get_object_or_404(
        StudySession,
        pk=pk,
        owner=request.user
    )

    session.is_completed = not session.is_completed
    session.save(update_fields=["is_completed"])

    messages.success(
        request,
        "Study session status updated!"
    )

    return redirect("sessions")


# Quiz views

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.filter(
        subject__owner=request.user
    ).select_related("subject")

    return render(request, "learning/quizzes.html", {
        "quizzes": quizzes,
    })


@login_required
def quiz_create(request):
    if request.method == "POST":
        form = QuizForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():
            quiz = form.save()

            messages.success(
                request,
                "Quiz created successfully!"
            )

            return redirect("quiz_detail", pk=quiz.pk)
    else:
        form = QuizForm(user=request.user)

    return render(request, "learning/quiz_form.html", {
        "form": form,
    })


@login_required
def quiz_detail(request, pk):
    quiz = get_object_or_404(
        Quiz,
        pk=pk,
        subject__owner=request.user
    )

    questions = quiz.questions.prefetch_related("choices")

    return render(request, "learning/quiz_detail.html", {
        "quiz": quiz,
        "questions": questions,
        "question_form": QuestionForm(),
        "choice_form": ChoiceForm(),
    })


@login_required
@require_POST
def question_create(request, quiz_id):
    quiz = get_object_or_404(
        Quiz,
        pk=quiz_id,
        subject__owner=request.user
    )

    form = QuestionForm(request.POST)

    if form.is_valid():
        question = form.save(commit=False)
        question.quiz = quiz
        question.save()

        messages.success(request, "Question added successfully!")
    else:
        messages.error(request, "Please enter a valid question.")

    return redirect("quiz_detail", pk=quiz.pk)


@login_required
@require_POST
def choice_create(request, question_id):
    question = get_object_or_404(
        Question,
        pk=question_id,
        quiz__subject__owner=request.user
    )

    form = ChoiceForm(request.POST)

    if form.is_valid():
        choice = form.save(commit=False)
        choice.question = question
        choice.save()

        messages.success(
            request,
            "Answer choice added successfully!"
        )
    else:
        messages.error(
            request,
            "Please enter a valid answer choice."
        )

    return redirect("quiz_detail", pk=question.quiz.pk)


@login_required
def quiz_take(request, pk):
    quiz = get_object_or_404(
        Quiz,
        pk=pk,
        subject__owner=request.user
    )

    questions = quiz.questions.prefetch_related("choices")

    if not questions.exists():
        messages.error(
            request,
            "This quiz has no questions yet."
        )
        return redirect("quiz_detail", pk=quiz.pk)

    if request.method == "POST":
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_choice_id = request.POST.get(
                f"question_{question.id}"
            )

            if selected_choice_id:
                correct_choice = question.choices.filter(
                    pk=selected_choice_id,
                    is_correct=True
                ).exists()

                if correct_choice:
                    score += 1

        attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=total_questions
        )

        return redirect("quiz_result", pk=attempt.pk)

    return render(request, "learning/quiz_take.html", {
        "quiz": quiz,
        "questions": questions,
    })


@login_required
def quiz_result(request, pk):
    attempt = get_object_or_404(
        QuizAttempt,
        pk=pk,
        user=request.user
    )

    percentage = 0

    if attempt.total_questions > 0:
        percentage = round(
            attempt.score / attempt.total_questions * 100
        )

    return render(request, "learning/quiz_result.html", {
        "attempt": attempt,
        "percentage": percentage,
    })
