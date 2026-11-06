# SmartLearn

## Overview

SmartLearn is a web-based learning management and progress tracking application built with Django. It helps users organize their learning materials, manage study sessions, track topic completion, and evaluate their knowledge through quizzes.

The application provides a personal dashboard where users can manage their learning activities and monitor their progress.

## Distinctiveness and Complexity

SmartLearn is more than a simple CRUD application. It combines several connected features into one learning platform.

The project includes user authentication, subject and topic management, study session planning, quiz creation, quiz evaluation, and progress tracking.

Its database structure uses relationships between models to organize subjects, topics, questions, choices, and quiz attempts. The application also ensures that users can access only their own learning data.

The quiz system evaluates submitted answers and records each user's results. Automated tests are included to verify important functionality and prevent certain invalid operations.

## Features

### User Authentication
- Users can log in and access their personal learning dashboard.
- Learning data is associated with the authenticated user.

### Subject Management
- Create, edit, view, and delete subjects.
- Organize learning materials by subject.

### Topic Management
- Add topics to subjects.
- Edit and delete topics.
- Mark topics as completed or incomplete.
- Track learning progress through topic completion.

### Study Session Management
- Schedule study sessions.
- Set a title, date, and duration for each session.
- Mark sessions as completed or incomplete.

### Quiz System
- Create quizzes for subjects.
- Add questions and answer choices.
- Identify correct answers.
- Take quizzes and receive results.
- Store quiz attempts and scores.

### Dashboard
- View subjects and learning progress.
- See upcoming study sessions.
- Review recent quiz attempts.

## Technologies Used

- **Python:** Main programming language.
- **Django:** Web framework.
- **SQLite:** Database.
- **HTML5:** Page structure.
- **CSS3:** Styling and layout.
- **JavaScript:** Basic client-side functionality.
- **Git and GitHub:** Version control and project hosting.

## Project Structure

The project is organized into the following main directories and files:

- `manage.py`: Django project management utility.
- `config/`: Main Django project configuration, including settings and URL configuration.
- `learning/`: Main application containing models, views, forms, URLs, tests, and admin configuration.
- `templates/`: HTML templates used to render application pages.
- `static/`: Static files, including CSS and JavaScript.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Installation and Setup

Follow these steps to run SmartLearn locally.

### 1. Clone the repository

```bash
git clone https://github.com/imanmasomi/SmartLearn.git
```

### 2. Navigate to the project directory

```bash
cd SmartLearn
```

If the Django project files are inside a nested directory, navigate to the directory containing `manage.py`.

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Linux or macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

`http://127.0.0.1:8000/`

## Database Models

SmartLearn uses Django models to store and organize application data.

The main models include:

- **Subject:** Stores subjects created by users, including their names and descriptions.
- **Topic:** Represents individual learning topics belonging to a subject and stores their completion status.
- **StudySession:** Stores scheduled study sessions, including their dates, durations, and completion status.
- **Quiz:** Represents quizzes associated with subjects.
- **Question:** Stores questions belonging to quizzes.
- **Choice:** Stores answer choices for questions and identifies correct answers.
- **QuizAttempt:** Records quiz attempts, scores, and completion dates for users.
- **Review:** Stores scheduled review information for a topic, including its due date and completion status. The model is currently defined but does not yet have a dedicated user interface or review workflow.

These models use relationships such as foreign keys to connect related records and maintain an organized database structure.

## Testing

SmartLearn includes automated tests for important application functionality and security.

The tests cover:

- Correct calculation of topic completion progress.
- Protection against users accessing another user's subjects and topics.
- Validation of topic completion actions.
- Assignment of newly created subjects to the currently authenticated user.
- Correct evaluation and recording of quiz attempts.
- Protection against accepting an answer choice belonging to another question.

To run the automated tests, execute:

```bash
python manage.py test
```

To check the project for common configuration problems, execute:

```bash
python manage.py check
```

All six automated tests pass successfully.

## Future Improvements

Possible future improvements include:

- Implementing a spaced repetition review system with a dedicated review interface.
- Adding options to edit and delete existing quizzes.
- Providing more detailed learning statistics and progress charts.
- Supporting additional question types.
- Adding study session reminders and notifications.
- Improving the user interface and overall user experience.

## Security and Deployment

SmartLearn is currently configured for local development using Django's development server and SQLite.

Before deploying the application to a production environment, the following changes should be considered:

- Set `DEBUG` to `False`.
- Configure a secure `SECRET_KEY` using environment variables.
- Configure allowed hosts.
- Use an appropriate production database.
- Configure static files for production.
- Set up HTTPS and other production security settings.

## License

This project was developed as a CS50 Web Programming with Python and JavaScript final project.

## Detailed File Documentation

### Django Configuration

- `manage.py`: Provides the command-line interface for managing the Django project.
- `config/settings.py`: Contains project settings, installed applications, database configuration, templates, static files, and security settings.
- `config/urls.py`: Defines the main URL routes and connects the learning application and Django authentication routes.
- `config/asgi.py`: Provides the ASGI application entry point.
- `config/wsgi.py`: Provides the WSGI application entry point.
- `config/__init__.py`: Identifies the configuration directory as a Python package.

### Learning Application

- `learning/models.py`: Defines the database models for subjects, topics, study sessions, quizzes, questions, choices, quiz attempts, and reviews.
- `learning/views.py`: Implements the application logic, including authentication, dashboard display, learning management, quiz creation, quiz submission, and result calculation.
- `learning/urls.py`: Maps application URLs to their corresponding views.
- `learning/forms.py`: Defines forms used to collect and validate user input.
- `learning/admin.py`: Configures application models for Django administration.
- `learning/apps.py`: Contains the application configuration.
- `learning/tests.py`: Contains automated tests for application functionality, data validation, and user access restrictions.
- `learning/migrations/`: Contains database migration files used to create and update the database schema.

### Frontend Files

- `templates/base.html`: Provides the shared layout and navigation structure.
- `templates/registration/`: Contains the registration and login pages.
- `templates/learning/dashboard.html`: Displays the user's learning dashboard.
- `templates/learning/subjects.html`: Displays the user's subjects.
- `templates/learning/subject_form.html`: Provides the subject creation and editing form.
- `templates/learning/subject_confirm_delete.html`: Displays the subject deletion confirmation page.
- `templates/learning/topics.html`: Displays topics and learning progress.
- `templates/learning/topic_edit.html`: Provides the topic editing interface.
- `templates/learning/topic_confirm_delete.html`: Displays the topic deletion confirmation page.
- `templates/learning/sessions.html`: Displays study sessions.
- `templates/learning/session_form.html`: Provides the study session form.
- `templates/learning/quizzes.html`: Displays available quizzes.
- `templates/learning/quiz_form.html`: Provides the quiz creation and editing form.
- `templates/learning/quiz_detail.html`: Displays quiz questions and answer choices and provides question and choice management.
- `templates/learning/quiz_take.html`: Displays the quiz-taking interface.
- `templates/learning/quiz_result.html`: Displays the result of a submitted quiz attempt.
- `static/css/style.css`: Contains the visual styling and responsive layout rules.
- `static/js/app.js`: Contains client-side JavaScript functionality.

### Additional Files

- `requirements.txt`: Lists the Python packages required to run the project.
- `.gitignore`: Excludes local files, virtual environments, and database files from version control.
- `README.md`: Documents the project's purpose, features, complexity, installation, structure, and testing.

