# SmartLearn

SmartLearn is a web-based learning management and progress tracking application built with Django. It helps users organize their learning activities, manage subjects and topics, plan study sessions, take quizzes, and monitor their learning progress in one place.

The main goal of SmartLearn is to provide a simple and organized environment where learners can manage their study plans and keep track of what they have learned.

## Features

### 1. User Authentication
- Users can create an account and log in securely.
- Each user has access to their own learning data.
- Users cannot access or modify another user's private subjects and related information.

### 2. Subject Management
- Users can create subjects for different areas of study.
- Each subject can have a name and description.
- Users can view, edit, and delete their subjects.
- Topics can be organized under each subject.

### 3. Topic Management and Progress Tracking
- Users can add topics to their subjects.
- Topics can be marked as completed.
- Users can edit or delete topics.
- The application automatically calculates learning progress based on completed topics.
- Progress is displayed as a percentage, making it easier to understand how much of a subject has been completed.

### 4. Study Session Planner
- Users can create study sessions for their subjects.
- Each session includes a title, scheduled date and time, and duration.
- Users can view their planned study sessions.
- Sessions can be marked as completed or incomplete.
- The dashboard displays upcoming study sessions.

### 5. Quiz System
- Users can create quizzes associated with their subjects.
- Each quiz can contain multiple questions.
- Questions can have multiple answer choices.
- The creator can identify the correct answer for each question.
- Users can take quizzes and submit their answers.
- The application automatically evaluates submitted answers and calculates the score.
- Quiz results display the number of correct answers and the final percentage.
- Quiz attempts are saved so users can review their previous performance.

### 6. Dashboard
- The dashboard provides an overview of the user's learning activities.
- It displays the number of subjects, upcoming study sessions, and quiz attempts.
- Users can quickly access important sections of the application.
- Learning information is presented in an organized way.

## Distinctiveness and Complexity

SmartLearn is different from a simple task manager or a basic collection of educational pages because it combines several related learning management features in one application.

The application uses multiple interconnected database models to represent subjects, topics, study sessions, quizzes, questions, answer choices, quiz attempts, and scheduled reviews. These relationships allow the application to organize learning information and connect different activities to the appropriate users and subjects.

One important feature is automatic progress calculation. Instead of requiring users to manually enter their progress, the application calculates the percentage of completed topics within a subject.

The quiz system also includes application logic for retrieving questions, processing submitted answers, checking selected choices against the correct answers, calculating scores, and saving quiz attempts.

The study session planner provides another layer of functionality by allowing users to organize their study time and track completed sessions.

The application also uses Django's authentication and permission mechanisms to ensure that users can only access their own learning information.

Together, these features make SmartLearn a learning management application rather than simply a website for storing notes or displaying static educational content.

## Technologies Used

- **Python:** Main programming language.
- **Django:** Web framework used for application logic, routing, authentication, database interaction, and form handling.
- **SQLite:** Database used to store application data during development.
- **HTML5:** Used to structure web pages.
- **CSS3:** Used for styling and responsive page layouts.
- **JavaScript:** Used for client-side interactions.
- **Git and GitHub:** Used for version control and source code hosting.

## Project Structure

The project is organized into separate folders for configuration, application logic, database models, user interface templates, and static assets. This structure keeps the code organized and makes the application easier to maintain and extend.

- `manage.py`: The main Django command-line utility. It is used to run the development server, execute database migrations, create administrator accounts, and run automated tests.

- `config/`: Contains the main configuration of the Django project.
  - `settings.py`: Defines project settings, including installed applications, middleware, database configuration, templates, static files, and security-related settings.
  - `urls.py`: Defines the main URL routes and connects incoming requests to the appropriate application URLs.
  - `asgi.py`: Provides the entry point for ASGI-compatible application servers.
  - `wsgi.py`: Provides the entry point for WSGI-compatible application servers.

- `learning/`: The main Django application. It contains the core functionality of SmartLearn, including subject management, topic tracking, study sessions, quizzes, and learning progress.
  - `models.py`: Defines the database structure. The models represent subjects, topics, study sessions, quizzes, questions, answer choices, quiz attempts, and scheduled topic reviews. These models define how learning data is stored and how related records are connected.
  - `views.py`: Contains the application logic. Views process user requests, retrieve or update database records, check permissions, calculate learning progress, and return the appropriate pages.
  - `forms.py`: Defines Django forms used to collect and validate user input when creating or editing application data.
  - `urls.py`: Maps URLs belonging to the learning application to their corresponding views.
  - `admin.py`: Registers and configures application models so they can be managed through Django's built-in administration interface.
  - `apps.py`: Contains the configuration for the learning application.
  - `tests.py`: Contains automated tests that check important application behavior, including user permissions, topic progress, completion actions, and quiz scoring.
  - `migrations/`: Stores database migration files. These files record changes to the database structure as application models are created or updated.

- `templates/`: Contains the HTML files used to display the application's pages.
  - `base.html`: Provides the shared page layout, navigation bar, and common structure used by other pages.
  - `learning/`: Contains pages for the dashboard, subjects, topics, study sessions, and quizzes. These templates display information received from the Django views.
  - `registration/`: Contains authentication-related pages, including the login page.

- `static/`: Stores files used by the browser to control the appearance and interactive behavior of the application.
  - `css/style.css`: Defines the visual design of SmartLearn, including colors, spacing, page layouts, buttons, forms, and responsive styling.
  - `js/app.js`: Contains client-side JavaScript used for browser interactions and interface behavior.

- `requirements.txt`: Lists the Python packages required to run the project. It allows developers to install the necessary dependencies using pip.

- `README.md`: Provides project documentation, including an overview of SmartLearn, its main features, installation instructions, project structure, and technical information.

## Installation and Setup

Follow these steps to run SmartLearn locally.

### 1. Clone the Repository

```bash
git clone https://github.com/imanmasomi/SmartLearn.git
cd SmartLearn
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

On Linux or macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create an administrator account.

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## Database

SmartLearn uses Django's ORM to manage application data through database models.

The main models include:

- **Subject:** Represents a learning subject owned by a user.
- **Topic:** Represents an individual learning topic belonging to a subject.
- **StudySession:** Stores planned study activities, including their scheduled date, duration, and completion status.
- **Quiz:** Represents a quiz associated with a subject.
- **Question:** Stores questions belonging to a quiz.
- **Choice:** Stores possible answers for each question and identifies the correct answer.
- **QuizAttempt:** Records a user's quiz result, score, and completion time.
- **Review:** Stores scheduled review information associated with a topic.

These models use relationships such as foreign keys to connect related records and maintain an organized database structure.

## Testing

SmartLearn includes automated tests for important application functionality.

The tests cover:

- Correct calculation of topic completion progress.
- Protection against users accessing another user's subjects and topics.
- Validation of topic completion actions.
- Assignment of newly created subjects to the currently authenticated user.
- Correct evaluation and recording of quiz attempts.

To run the automated tests, execute:

```bash
python manage.py test
```

To check the project for common configuration problems, execute:

```bash
python manage.py check
```

## Future Improvements

Possible improvements for future versions include:

- Adding a dedicated spaced-repetition review interface.
- Allowing users to edit and delete existing quizzes.
- Adding more detailed learning statistics and progress charts.
- Supporting additional question types.
- Adding notifications and reminders for scheduled study sessions.
- Improving the user interface and adding more customization options.

## Security and Deployment

SmartLearn uses Django's built-in authentication system and user-based data ownership to protect private learning information.

The application is currently configured for local development. Before production deployment, the secret key should be stored securely in environment variables, debug mode should be disabled, allowed hosts should be configured for the deployment domain, and production database and static file settings should be applied.

The development database and local environment files should not be committed to the public repository.
