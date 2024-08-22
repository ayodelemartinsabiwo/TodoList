# README for Todo List App

## Overview

This Django-based Todo List web application allows users to create, edit, delete, and manage to-do items. The app includes a user authentication system where users can sign up, log in, and update their profiles, including uploading an avatar. Users can search their to-do items, mark tasks as important, and see a list of their important items on the dashboard. The interface is built with Bootstrap, and the backend uses Django’s form and authentication system.

## Features

- **User Registration & Login:** Users can sign up, log in, and log out.
- **User Profile:** Users can upload avatars, which are displayed on the dashboard.
- **Task Management:** Users can add, edit, and delete tasks.
- **Marking Importance:** Users can mark tasks as important, which will be highlighted in the important items section.
- **Search Functionality:** Users can search for specific to-do items by title.
- **Task Completion Tracking:** Tasks can be marked as done or not done.
- **Responsive UI:** The interface is designed using Bootstrap, making it responsive and visually appealing.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.x
- MySQL database
- Virtualenv (recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/todolist.git
   cd todolist
   ```

2. **Create and Activate Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration:**

   Ensure that MySQL is installed and running. Update the `DATABASES` configuration in `settings.py` with your MySQL credentials.

5. **Migrate the Database:**

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the App:**

   Open your browser and navigate to `http://127.0.0.1:8000`.

### Media and Static Files Setup

To serve media files during development, ensure `MEDIA_URL` and `MEDIA_ROOT` are properly configured in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Ensure that static files are collected before deploying to production:

```bash
python manage.py collectstatic
```

## URL Structure

The app includes several key URL patterns:

- `/todolst/` - Displays a basic time-based response (can be customized).
- `/` - Home page.
- `/join/` - Registration page for new users.
- `/login/` - Login page.
- `/welcome/` - User dashboard, displaying their to-do items and important tasks.
- `/delete/<int:item_id>/` - Deletes a specific to-do item.
- `/update-importance/<int:item_id>/<str:importance>/` - Updates the importance status of a specific to-do item.

## Views

The key views include:

- **`home`:** Renders the homepage.
- **`join`:** Handles user registration with form validation.
- **`login`:** Manages user login with form validation.
- **`welcome`:** The user dashboard, showing the list of tasks, search results, and important items.
- **`delete_item`:** Handles the deletion of a specific task.
- **`update_importance`:** Toggles the importance status of a to-do item.

## Models

- **TodoItem:**
  - Fields: `user`, `title`, `description`, `due_date`, `completed`, `important`
  - Relationships: Linked to the `User` model with a foreign key.

- **UserProfile:**
  - Fields: `user`, `avatar`
  - Relationships: Linked to the `User` model with a one-to-one relationship.

## Forms

- **LoginForm:** Handles user login with custom validation for credentials.
- **TodoItemForm:** Allows users to create and edit their to-do items, with widgets for custom styles.
- **UserProfileForm:** Manages user profile updates, including avatar upload.

## Admin

The Django admin panel provides access to manage users, to-do items, and user profiles. The admin site is accessible at `/admin/`.

- **UserProfileAdmin:** Displays user and avatar information for management.

## Static and Media Files

- **Static Files:** Served from the `static/` directory, where CSS and JavaScript files are stored.
- **Media Files:** User-uploaded files (avatars) are stored in the `media/` directory.

## API

- **`update_importance` (POST):** Receives AJAX requests to toggle the importance of a to-do item. It returns a JSON response indicating success or failure.

## Security

Ensure that the `SECRET_KEY` in `settings.py` is kept confidential and updated for production environments. The `DEBUG` setting should be set to `False` in production for enhanced security.

## Deployment

1. Set up your production server (e.g., using Gunicorn and Nginx).
2. Update your database configurations to match your production database.
3. Collect static files with:

   ```bash
   python manage.py collectstatic
   ```

4. Configure your server to serve media and static files.
5. Ensure you have a secure SSL configuration for HTTPS.

## Future Enhancements

- **Notifications:** Add a feature for users to receive email or SMS notifications when tasks are due soon.
- **Tags:** Allow users to categorize tasks by tags.
- **Task Priority:** Introduce a priority system for tasks.
- **Mobile App:** Extend the web app into a mobile-friendly app using responsive design or a framework like React Native.

---

This project provides a flexible and user-friendly to-do list app that can be easily extended and enhanced based on user needs.
