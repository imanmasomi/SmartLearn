# SmartLearn

SmartLearn is a personal learning management and progress-tracking web application built with Django, Python, JavaScript, HTML, and CSS.

The application helps users organize their learning activities, manage study subjects and topics, schedule study sessions, take quizzes, and track their learning progress.

## Features

### 1. User Authentication
- Users can log in and log out.
- Each user has a personal learning dashboard.
- Users can manage their own learning subjects and study sessions.

### 2. Subject Management
- Create new subjects with a name and description.
- View a list of personal subjects.
- Edit and delete subjects.
- Organize learning topics under each subject.

### 3. Topic Management and Progress Tracking
- Add topics to a subject.
- Edit and delete topics.
- Mark topics as completed or incomplete.
- Automatically calculate learning progress based on completed topics.
- Display progress as a percentage.

### 4. Study Planner
- Create study sessions associated with a subject.
- Set a session title, date, time, and duration.
- View scheduled study sessions.
- Mark sessions as completed or incomplete.

### 5. Quiz System
- Create quizzes for individual subjects.
- Add questions to each quiz.
- Add multiple answer choices to each question.
- Mark the correct answer when creating a choice.
- Take quizzes by selecting answers.
- Automatically evaluate submitted answers.
- Calculate quiz scores and percentages.
- Save quiz attempts with the user's score and completion date.
- Display a result page after completing a quiz.

## Distinctiveness and Complexity

SmartLearn is different from a typical blog, social network, or e-commerce application because its main purpose is personal learning management and progress evaluation.

The application combines several related features into one system. Users can organize subjects, divide them into smaller learning topics, schedule study sessions, and evaluate their knowledge through quizzes.

The project uses a relational database structure with multiple connected Django models:

- `Subject` stores each user's learning subjects.
- `Topic` stores learning topics associated with subjects.
- `StudySession` stores scheduled study activities.
- `Quiz` stores quizzes associated with subjects.
- `Question` stores questions belonging to quizzes.
- `Choice` stores possible answers and identifies correct answers.
- `QuizAttempt` stores quiz results for individual users.
- `Review` represents a model for scheduling topic reviews.

One important part of the application is the quiz evaluation system. When a user submits a quiz, Django checks the selected choices against the correct answers stored in the database, calculates the score, and saves the result as a quiz attempt.

Another important feature is automatic progress calculation. The application calculates the percentage of completed topics for each subject instead of requiring users to update their progress manually.

The project uses Django's server-side functionality for database operations, authentication, form validation, and application logic. HTML templates render the pages, CSS provides responsive styling, and JavaScript supports browser-side interactions.

These connected features and database relationships make SmartLearn a complete learning management application rather than a collection of unrelated pages.

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript

## Project Structure

- `manage.py`: Django command-line utility.
- `config/`: Main Django project configuration, settings, and URL routing.
- `learning/models.py`: Database models.
- `learning/forms.py`: Django forms for user input.
- `learning/views.py`: Application logic and view functions.
- `learning/urls.py`: URL patterns for the learning application.
- `learning/admin.py`: Django administration configuration.
- `learning/migrations/`: Database migration files.
- `templates/`: HTML templates used by the application.
- `templates/learning/`: Templates for subjects, topics, sessions, quizzes, and dashboard pages.
- `templates/registration/`: Authentication templates.
- `static/css/style.css`: Application styling and responsive layout.
- `static/js/app.js`: Client-side JavaScript.
- `requirements.txt`: Python dependencies.
- `db.sqlite3`: SQLite development database.

## Installation and Setup

Follow these steps to run SmartLearn locally.

1. Clone or download the project.

2. Navigate to the directory containing `manage.py`.

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment.

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create an administrator account:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Open the following address in your browser:

   `http://127.0.0.1:8000/`

10. Log in and start organizing your learning activities.

## Database

SmartLearn uses SQLite during development. Django's ORM manages database operations and relationships between subjects, topics, study sessions, quizzes, questions, choices, and quiz attempts.

## Future Improvements

Possible future improvements include:

- A dedicated spaced-repetition review interface.
- More detailed learning statistics.
- Quiz editing and deletion.
- Improved study calendar visualization.
- Additional quiz question types.

## Security and Deployment

This project is configured for local development. Before production deployment, the Django secret key, allowed hosts, debug settings, database configuration, and static-file settings should be adjusted for a secure production environment.
