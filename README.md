# SmartLearn

SmartLearn is a web-based learning management application built with Django. It helps individual learners organize their subjects, divide their learning into manageable topics, plan study sessions, monitor their progress, and evaluate their knowledge through quizzes.

The application provides a personal workspace for each registered user. After creating an account and logging in, a learner can manage their own learning materials and activities through a dashboard and a collection of dedicated pages. The main purpose of SmartLearn is to bring learning organization, progress tracking, study planning, and knowledge assessment together in one application.

## Distinctiveness and Complexity

SmartLearn is designed as a personal learning management system rather than a simple collection of static pages or a basic CRUD application. Its main distinction is the way several related learning activities are connected through a common data model and a user-specific workspace.

A learner begins by creating subjects. Each subject can contain multiple topics, allowing a large learning area to be divided into smaller and more manageable units. Topics can be marked as completed or incomplete. The application calculates the completion percentage for each subject from the number of completed topics and the total number of topics. This progress is displayed visually, giving users a straightforward way to understand how much of a subject they have completed.

The application also includes a study planning component. Users can create study sessions, associate each session with one of their subjects, select a scheduled date and time, and specify its duration. Sessions have completion status, so users can distinguish planned activities from completed ones. The dashboard brings together useful information from different parts of the application, including the number of subjects, incomplete study sessions, and recent quiz attempts.

Another important component is the quiz system. Users can create quizzes associated with their subjects, add questions, and create answer choices for each question. They can identify the correct answer while managing the quiz. When a learner takes a quiz, the application evaluates the submitted answers, calculates the score, records the attempt, and displays a result page with the percentage and the number of correct answers.

The project involves more than displaying and saving form data. Its backend contains related database models, ownership relationships, form validation, authentication, permission checks, database queries, and score calculation. For example, subjects and study sessions belong to individual users. Views filter records by the authenticated user, and related operations check ownership before allowing access. This prevents one user from accessing another user's private learning data through ordinary application routes.

The quiz implementation also contains specific validation logic. When an answer is submitted, the application checks whether the selected choice belongs to the question being evaluated and whether that choice is marked as correct. This prevents a choice belonging to another question from being incorrectly counted as a correct answer. Quiz attempts are stored with the user's score, total question count, and completion timestamp, allowing the application to present recorded results.

The dashboard, subject pages, topic progress display, study planner, quiz management pages, and quiz result page are connected parts of the same learning workflow. This combination of related features, user-specific data handling, relational database design, and server-side logic is what makes SmartLearn distinct from a simple task list or a basic content website.

The frontend uses Django templates, custom CSS, and a small JavaScript file. The layout includes reusable navigation and message areas, consistent page components, forms, status indicators, progress bars, and responsive styling for smaller screens. The application is primarily implemented with Django and server-rendered HTML rather than relying on a separate frontend framework.

## Main Features

- User registration, login, and logout.
- A personal dashboard showing learning activity and summary counts.
- Subject creation, listing, editing, and deletion.
- Topic creation, editing, deletion, and completion tracking.
- Automatic calculation and display of subject topic progress.
- Study session creation and scheduling.
- Study session completion tracking.
- Quiz creation for a user's subjects.
- Question and answer-choice management.
- Correct-answer identification.
- Quiz participation and automatic score calculation.
- Recorded quiz attempts and result pages.
- User-specific access control for learning data.

## Technologies

- Python
- Django 5.2
- SQLite
- HTML
- CSS
- JavaScript
- Django Template Language

## Project Structure and File Documentation

The following sections describe the files that make up the application and the purpose of each file.

### Root Files

- `manage.py`: Django's command-line utility. It is used to run the development server, execute database migrations, run tests, and perform other Django management commands.
- `requirements.txt`: Lists the Python dependency required by the project. It specifies Django with the version range `>=5.2,<6.0`.
- `.gitignore`: Specifies files and directories that should not be tracked by Git, such as local development files and generated files.
- `README.md`: Provides the project overview, feature descriptions, technical information, setup guidance, and documentation of the project files.

### Configuration Package: `config/`

- `config/__init__.py`: Marks the configuration directory as a Python package.
- `config/settings.py`: Contains the main Django configuration, including installed applications, middleware, template settings, database configuration, authentication settings, static-file settings, timezone, and allowed hosts.
- `config/urls.py`: Defines the main URL configuration. It connects Django's administration interface, authentication URLs, and the URL patterns of the learning application.
- `config/asgi.py`: Provides the ASGI application entry point for servers that support the Asynchronous Server Gateway Interface.
- `config/wsgi.py`: Provides the WSGI application entry point for deployment through servers that support the Web Server Gateway Interface.

### Learning Application: `learning/`

- `learning/__init__.py`: Marks the learning directory as a Python package.
- `learning/admin.py`: Registers the project's database models with Django's administration interface, including subjects, topics, study sessions, quizzes, questions, choices, quiz attempts, and reviews.
- `learning/apps.py`: Defines the Django application configuration for the learning application.
- `learning/models.py`: Defines the database structure and relationships. It contains the models for Subject, Topic, StudySession, Quiz, Question, Choice, QuizAttempt, and Review. These models represent the main learning data and connect users, subjects, topics, study sessions, questions, answer choices, and quiz results.
- `learning/forms.py`: Defines Django forms used to create and edit subjects, topics, study sessions, quizzes, questions, and answer choices. It also filters subject selections in relevant forms so users can select their own subjects and validates study-session duration.
- `learning/views.py`: Contains the main application logic. It handles the dashboard, registration, subject management, topic management, progress calculation, study sessions, quiz creation and management, quiz participation, answer evaluation, and result display. It also applies authentication and ownership checks to protect user-specific data.
- `learning/urls.py`: Defines the URL patterns for the learning application. These routes connect browser requests to views for the dashboard, subjects, topics, study sessions, quizzes, questions, answer choices, and quiz results.
- `learning/tests.py`: Contains automated tests for important application behavior. The tests cover topic progress calculation, user access restrictions, POST-only topic completion changes, subject ownership assignment, quiz score recording, and rejection of an answer choice belonging to a different question.

### Database Migrations: `learning/migrations/`

- `learning/migrations/__init__.py`: Marks the migrations directory as a Python package.
- `learning/migrations/0001_initial.py`: Defines the initial database migration. It creates the database tables and relationships for the learning application's models, including subjects, topics, study sessions, quizzes, questions, choices, quiz attempts, and reviews.

### Static Files: `static/`

- `static/css/style.css`: Contains the application's custom visual styling. It defines typography, colors, navigation, buttons, panels, cards, forms, lists, progress bars, status indicators, dashboard components, and responsive layouts for smaller screens.
- `static/js/app.js`: Contains the JavaScript entry point loaded by the base template. It listens for the DOM content-loaded event and logs a message indicating that SmartLearn is ready.

### Base Template: `templates/`

- `templates/base.html`: The shared layout used by the application's pages. It loads static CSS and JavaScript, provides the navigation bar, displays Django messages, and defines the content block extended by other templates. It also displays different navigation options depending on whether the user is authenticated.

### Learning Templates: `templates/learning/`

- `templates/learning/dashboard.html`: Displays the user's dashboard, including summary information about subjects, incomplete study sessions, quiz attempts, and links to the main application sections.
- `templates/learning/subjects.html`: Displays the authenticated user's subjects, their descriptions, topic counts, and links for viewing topics, editing subjects, and deleting them.
- `templates/learning/subject_form.html`: Provides the form page for creating a subject.
- `templates/learning/subject_confirm_delete.html`: Displays a confirmation page before deleting a subject.
- `templates/learning/topics.html`: Displays the topics belonging to a subject. It includes the progress percentage, completed-topic count, a form for adding topics, and controls for editing, deleting, and changing topic completion status.
- `templates/learning/topic_edit.html`: Provides the form for editing an existing topic.
- `templates/learning/topic_confirm_delete.html`: Displays a confirmation page before deleting a topic.
- `templates/learning/sessions.html`: Lists the user's study sessions, including their subject, scheduled date and time, duration, completion status, and controls for changing that status.
- `templates/learning/session_form.html`: Provides the form for creating a study session, including its subject, title, scheduled date and time, and duration.
- `templates/learning/quizzes.html`: Displays the quizzes associated with the user's subjects and provides links to create and manage quizzes.
- `templates/learning/quiz_form.html`: Provides the form for creating a quiz and associating it with one of the user's subjects.
- `templates/learning/quiz_detail.html`: Provides the quiz management interface. It displays the quiz questions, allows new questions and answer choices to be added, identifies correct answers, and provides controls for deleting questions and choices.
- `templates/learning/quiz_take.html`: Displays the questions and answer choices for a quiz. It provides the form through which a user submits answers.
- `templates/learning/quiz_result.html`: Displays the result of a completed quiz attempt, including the percentage score, correct-answer count, total number of questions, and completion information.

### Authentication Templates: `templates/registration/`

- `templates/registration/login.html`: Provides the login form and displays authentication errors and a link to account registration.
- `templates/registration/register.html`: Provides the account registration form, including username, password, and password confirmation fields.

## Database Design

SmartLearn uses Django's ORM and an SQLite database.

The main relationships are:

- A user can own multiple subjects.
- A subject can contain multiple topics.
- A user can have multiple study sessions.
- Each study session is associated with a subject.
- A subject can contain multiple quizzes.
- A quiz can contain multiple questions.
- A question can contain multiple answer choices.
- A user can have multiple quiz attempts.
- Each quiz attempt is associated with a quiz and records its score and total number of questions.
- A topic can be associated with review records in the database model.

The application uses Django model relationships and cascading deletion where configured, so related records are handled consistently when their parent records are deleted.

## Running the Project

1. Install Python and create or activate a virtual environment.
2. Install the project dependency:

   `pip install -r requirements.txt`
3. Apply database migrations:

   `python manage.py migrate`
4. Start the development server:

   `python manage.py runserver`
5. Open the local development address shown by Django in your browser.

Users can create an account through the registration page and then log in to access their personal learning workspace.

## Testing

The project includes automated Django tests for important functionality and data-protection behavior.

Run the test suite with:

`python manage.py test`

The tests cover progress calculation, ownership restrictions, topic completion behavior, subject creation, quiz scoring, and answer validation.

## Design Goal

SmartLearn aims to make independent learning easier to organize and evaluate. By connecting subjects, topics, study sessions, and quizzes in one application, it gives learners a structured way to plan their work, monitor progress, and check their understanding over time.
