Library Management System
A web-based application built with Django, SQLite, and React to manage library operations, including books, members, and borrowing processes for schools, colleges, and small libraries.
🚀 Features

Book Management: Add, edit, delete, and view book records (title, author, ISBN, etc.).
Member Management: Register, update, and remove student/member profiles.
Borrowing System: Issue/return books and track due dates with role-based access.
Interactive Dashboard: Real-time statistics and data tables for admins and users.
Configurable Settings: Adjustable parameters for library rules and user roles.

📋 Requirements
python>=3.8
django>=4.0
djangorestframework>=3.13
node>=14.0
react>=17.0

🛠️ Installation

Clone or download the repository:git clone https://github.com/itsghali/Library-management.git
cd Library-management


Install backend dependencies (Django):cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Note: If requirements.txt is missing, install manually:

pip install django djangorestframework


Install frontend dependencies (React):cd ../frontend
npm install


Run the application:
Backend:cd backend
python manage.py migrate
python manage.py runserver


Frontend (in a new terminal):cd frontend
npm start





🎯 Usage
Application Interface
The application provides an intuitive interface with the following controls:
Admin Controls

Book Management: Add/edit books via forms or admin panel.
Member Management: Manage user profiles and roles.
Borrowing: Issue/return books and view transaction history.

User Controls

Search Books: Filter by title, author, or ISBN.
View Loans: Check borrowed books and due dates.
Profile: Update personal details.

Main Features
1. Book Management

Add books with details like title, author, ISBN, and copies.
Edit or delete existing book records.
View available books and their status.

2. Member and Borrowing System

Register members with unique IDs and roles (student/admin).
Issue books to members with due date tracking.
Automate return processing and overdue notifications (
