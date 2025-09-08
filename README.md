Library Management System
Welcome to the Library Management System, a web-based application built to streamline library operations for schools, colleges, and other institutions. This system simplifies the management of books, members, and borrowing transactions, offering an intuitive interface for librarians and users. It leverages Django for the backend, SQLite for data storage, and React for a dynamic frontend.
Table of Contents

Project Overview
Features
Technologies Used
Installation
Database Setup
Usage
Contributing
License
Contact

Project Overview
The Library Management System automates library operations, such as tracking book availability, managing borrowing and returning processes, and maintaining member records. Built with Django, SQLite, and React, it provides a modern, responsive interface for efficient library management. The system supports role-based access for admins (librarians) and users (students/members), ensuring secure and organized operations. It is ideal for educational institutions or small libraries looking to digitize their workflows.
Features
Admin/Librarian Features

Book Management: Add, update, delete, and view book records (title, author, genre, ISBN, number of copies).
Member Management: Register, update, and remove student/member profiles.
Borrowing and Returning: Issue books to members, track due dates, and manage returns.
Report Generation: Generate reports for issued books, overdue books, and member activities.
Security: Secure user authentication with Django’s built-in authentication system and optional CAPTCHA verification.
Dashboard: View summary statistics of books, members, and transactions.

User/Student Features

Book Search: Search for books by title, author, or ISBN via the React frontend.
View Issued Books: Check borrowed books and their return due dates.
Profile Management: Update personal information and manage account settings.

Technologies Used

Frontend:
React: For building a dynamic and interactive user interface.
HTML5: For structuring the web pages.
CSS3: For styling and responsive design.
Bootstrap: For a responsive and modern UI.
Axios: For making API requests to the Django backend.


Backend:
Django: Python web framework for server-side logic and API development.
Django REST Framework: For building RESTful APIs to connect the React frontend with the backend.


Database:
SQLite: Lightweight relational database for storing book, member, and transaction data.


Other:
Python: Core programming language for the backend.
Node.js and npm: For managing React dependencies and running the frontend.
Django’s Authentication System: For secure user management and password hashing.



Installation
Follow these steps to set up the Library Management System on your local machine.
Prerequisites

Python 3.8 or higher
Node.js and npm (version 14 or higher)
Git
A modern web browser (Chrome, Firefox, Edge, etc.)
Basic knowledge of Django, React, and web development

Steps

Clone the Repository:
git clone https://github.com/itsghali/Library-management.git
cd Library-management


Set Up the Backend (Django):

Navigate to the backend directory (e.g., backend or the folder containing manage.py):cd backend


Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Python dependencies:pip install -r requirements.txt


Note: If requirements.txt is not provided, install Django and Django REST Framework manually:

pip install django djangorestframework




Set Up the Frontend (React):

Navigate to the frontend directory (e.g., frontend or the folder containing package.json):cd ../frontend


Install Node.js dependencies:npm install




Configure Environment Variables:

In the backend directory, check for a .env file or configuration settings in settings.py.
Ensure the SQLite database is referenced correctly (see Database Setup).


Run the Backend:

From the backend directory:python manage.py migrate
python manage.py runserver


The Django server will run at http://localhost:8000.


Run the Frontend:

From the frontend directory:npm start


The React app will run at http://localhost:3000 and connect to the Django backend via API calls.


Access the Application:

Open a web browser and navigate to http://localhost:3000 to use the React frontend.
The frontend communicates with the Django backend at http://localhost:8000.



Database Setup
The system uses SQLite as its database, which is lightweight and requires minimal setup.

Run Migrations:

In the backend directory (where manage.py is located), apply migrations to set up the SQLite database:python manage.py migrate


This creates the db.sqlite3 file in the backend directory.


Verify Database Configuration:

Open settings.py in the backend directory and ensure the database is set to SQLite:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




Create a Superuser (Admin):

Create an admin account to access the Django admin panel:python manage.py createsuperuser


Follow the prompts to set up a username, email, and password.
Access the admin panel at http://localhost:8000/admin to manage books, members, and transactions.


Seed Initial Data (if applicable):

If the repository includes a seed script or data fixtures, load them:python manage.py loaddata initial_data.json


Check the repository for any provided seed files (e.g., initial_data.json).


Test the Database:

Start the Django server (python manage.py runserver) and ensure the application connects to the SQLite database without errors.



Usage

Admin Access:

Log in to the Django admin panel (http://localhost:8000/admin) using the superuser credentials to manage books, members, and transactions.
Alternatively, use the React frontend (http://localhost:3000) to access admin features via a custom dashboard (if implemented).
Example actions:
Add a new book: Navigate to the "Add Book" section, enter details (title, author, ISBN, etc.), and save.
Issue a book: Select a member, choose a book, and set the issue date.




User Access:

Register or log in as a student/member via the React frontend (http://localhost:3000).
Search for books, view issued books, or update your profile.
Example: Search for a book by typing its title in the search bar on the frontend.


Security Features:

The system uses Django’s authentication system for secure user management and password hashing.
Optional CAPTCHA or other security measures may be implemented in the frontend (check repository for details).
Log out after each session to maintain security.



Contributing
We welcome contributions to improve the Library Management System! To contribute:

Fork the Repository:

Click the "Fork" button on the GitHub repository page.


Clone Your Fork:
git clone https://github.com/YOUR_USERNAME/Library-management.git


Create a Branch:
git checkout -b feature/your-feature-name


Make Changes:

Implement your feature or bug fix in either the Django backend or React frontend.
Test thoroughly to ensure compatibility (e.g., run python manage.py test for backend tests or npm test for frontend tests).


Commit and Push:
git add .
git commit -m "Add your commit message"
git push origin feature/your-feature-name


Submit a Pull Request:

Go to the original repository and create a pull request from your branch.
Provide a clear description of your changes.
