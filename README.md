Library Management System
A web-based application to manage library operations, built with Django, SQLite, and React. It streamlines book management, member tracking, and borrowing processes for schools, colleges, and small libraries.
Table of Contents

Overview
Features
Technologies
Setup
Database Configuration
Usage
Contributing
License

Overview
The Library Management System automates library tasks like managing books, members, and borrowing records. It offers a responsive React frontend and a robust Django backend with SQLite for data storage. The system supports admin (librarian) and user (student) roles, ensuring secure and efficient library operations.
Features
Admin Features

Manage books: Add, edit, delete, and view book details (title, author, ISBN, etc.).
Manage members: Register, update, or remove student profiles.
Handle borrowing: Issue/return books and track due dates.
Generate reports: View issued books, overdue items, and member activity.
Admin dashboard: Display key statistics.

User Features

Search books: Find books by title, author, or ISBN.
View borrowed books: Check loan status and due dates.
Update profile: Manage personal details and account settings.

Technologies

Frontend: React, HTML5, CSS3, Bootstrap, Axios (for API calls)
Backend: Django, Django REST Framework
Database: SQLite
Other: Python 3.8+, Node.js 14+, Django authentication for security

Setup
Prerequisites

Python 3.8+
Node.js 14+ and npm
Git
Web browser (Chrome, Firefox, etc.)

Installation

Clone the Repository:
git clone https://github.com/itsghali/Library-management.git
cd Library-management


Backend Setup (Django):

Navigate to the backend directory (containing manage.py):cd backend


Create and activate a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Note: If requirements.txt is missing, install core packages:

pip install django djangorestframework




Frontend Setup (React):

Navigate to the frontend directory (containing package.json):cd ../frontend


Install dependencies:npm install




Run the Application:

Start the Django backend:cd backend
python manage.py runserver


Start the React frontend in a new terminal:cd frontend
npm start


Access the app at http://localhost:3000 (frontend) and http://localhost:8000 (backend API).



Database Configuration

Apply Migrations:

In the backend directory:python manage.py migrate


This creates the db.sqlite3 file.


Verify Settings:

Ensure settings.py uses SQLite:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




Create Admin User:

Set up a superuser for the Django admin panel:python manage.py createsuperuser


Access the admin panel at http://localhost:8000/admin.


Seed Data (if available):

Load any provided data fixtures:python manage.py loaddata initial_data.json





Usage

Admin: Log in at http://localhost:8000/admin or use the frontend admin dashboard to manage books, members, and loans.
User: Register/login via http://localhost:3000 to search books, view loans, or update profiles.
Security: Django’s authentication ensures secure logins; log out after use.

Contributing

Fork the repository on GitHub.
Clone your fork:git clone https://github.com/YOUR_USERNAME/Library-management.git


Create a branch:git checkout -b feature/your-feature


Make and test changes (backend: python manage.py test, frontend: npm test).
Commit and push:git add .
git commit -m "Your message"
git push origin feature/your-feature


Submit a pull request with a clear description.
Report issues via GitHub Issues.

