## Project Structure

The project is organized into separate folders for configuration, application logic, database models, user interface templates, and static assets. This structure keeps the code organized and makes the application easier to maintain and extend.

- `manage.py`: The main Django command-line utility. It is used to run the development server, execute database migrations, create administrator accounts, and run automated tests.

- `config/`: Contains the main configuration of the Django project.
  - `settings.py`: Defines the project settings, including installed applications, middleware, database configuration, templates, static files, and security-related settings.
  - `urls.py`: Defines the main URL routes and connects incoming requests to the appropriate application URLs.
  - `asgi.py`: Provides the entry point for ASGI-compatible application servers.
  - `wsgi.py`: Provides the entry point for WSGI-compatible application servers.

- `learning/`: The main Django application. It contains the core functionality of SmartLearn, including subject management, topic tracking, study sessions, quizzes, and learning progress.
  - `models.py`: Defines the database structure. The models represent subjects, topics, study sessions, quizzes, questions, answer choices, quiz attempts, and scheduled topic reviews. These models define how learning data is stored and how related records are connected.
  - `views.py`: Contains the application logic. Views process user requests, retrieve or update database records, check permissions, calculate learning progress, and return the appropriate pages.
  - `forms.py`: Defines Django forms used to collect and validate user input when creating or editing subjects, topics, study sessions, and quizzes.
  - `urls.py`: Maps URLs belonging to the learning application to their corresponding views.
  - `admin.py`: Registers and configures application models so they can be managed through Django's built-in administration interface.
  - `apps.py`: Contains the configuration for the learning application.
  - `tests.py`: Contains automated tests that check important application behavior, including user permissions, topic progress, completion actions, and quiz scoring.
  - `migrations/`: Stores database migration files. These files record changes to the database structure as application models are created or updated.

- `templates/`: Contains the HTML files used to display the application's pages.
  - `base.html`: Provides the shared page layout, navigation bar, and common structure used by other pages.
  - `learning/`: Contains the pages for the dashboard, subjects, topics, study sessions, and quizzes. These templates display information received from the Django views.
  - `registration/`: Contains authentication-related pages, including the login page.

- `static/`: Stores files used by the browser to control the appearance and interactive behavior of the application.
  - `css/style.css`: Defines the visual design of SmartLearn, including colors, spacing, page layouts, buttons, forms, and responsive styling.
  - `js/app.js`: Contains client-side JavaScript used for browser interactions and interface behavior.

- `requirements.txt`: Lists the Python packages required to run the project. It allows developers to install the necessary dependencies using pip.

- `README.md`: Provides project documentation, including an overview of SmartLearn, its main features, installation instructions, project structure, and technical information.
