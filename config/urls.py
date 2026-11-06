
from django.urls import path
from . import views

urlpatterns = [

    # Registration
    path(
        "register/",
        views.register,
        name="register"
    ),

    # Dashboard
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    # Subject URLs
    path(
        "subjects/",
        views.subject_list,
        name="subjects"
    ),

    path(
        "subjects/new/",
        views.subject_create,
        name="subject_create"
    ),

    path(
        "subjects/<int:pk>/edit/",
        views.subject_edit,
        name="subject_edit"
    ),

    path(
        "subjects/<int:pk>/delete/",
        views.subject_delete,
        name="subject_delete"
    ),

    # Topic URLs
    path(
        "subjects/<int:subject_id>/topics/",
        views.topic_list,
        name="topic_list"
    ),

    path(
        "subjects/<int:subject_id>/topics/new/",
        views.topic_create,
        name="topic_create"
    ),

    path(
        "subjects/<int:subject_id>/topics/<int:pk>/edit/",
        views.topic_edit,
        name="topic_edit"
    ),

    path(
        "subjects/<int:subject_id>/topics/<int:pk>/delete/",
        views.topic_delete,
        name="topic_delete"
    ),

    path(
        "subjects/<int:subject_id>/topics/<int:pk>/toggle/",
        views.topic_toggle,
        name="topic_toggle"
    ),

    # Study Session URLs
    path(
        "sessions/",
        views.session_list,
        name="sessions"
    ),

    path(
        "sessions/new/",
        views.session_create,
        name="session_create"
    ),

    path(
        "sessions/<int:pk>/toggle/",
        views.session_toggle,
        name="session_toggle"
    ),

    # Quiz URLs
    path(
        "quizzes/",
        views.quiz_list,
        name="quizzes"
    ),

    path(
        "quizzes/new/",
        views.quiz_create,
        name="quiz_create"
    ),

    path(
        "quizzes/<int:pk>/",
        views.quiz_detail,
        name="quiz_detail"
    ),

    path(
        "quizzes/<int:quiz_id>/questions/new/",
        views.question_create,
        name="question_create"
    ),

    path(
        "questions/<int:question_id>/choices/new/",
        views.choice_create,
        name="choice_create"
    ),

    path(
        "quizzes/<int:pk>/take/",
        views.quiz_take,
        name="quiz_take"
    ),

    path(
        "quiz-results/<int:pk>/",
        views.quiz_result,
        name="quiz_result"
    ),
]
