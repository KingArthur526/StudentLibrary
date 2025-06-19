Django Library Management System

This is a web-based Library Management System built with Django. It allows users to manage books, library members, and book borrowing activities through a clean and simple interface. Users can perform CRUD operations on books and members, track book issues and returns, and display book covers and member photos.

Features

- Add and manage books with metadata and cover images
- Register new library members with profile photos
- Issue books to members and track return dates
- View uploaded book covers and member photos
- Organized tables for books, members, and issued records
- Built-in form validations and date pickers for user input

Tech Stack

Backend: Python, Django  
Frontend: HTML, CSS (inline styling)  
Database: SQLite  
Media Handling: Django’s file/image upload system

Project Structure

library/
├── models.py         - Book, BookIssue, Lib_Member models  
├── forms.py          - ModelForms for Book, Issue, Member  
├── views.py          - Handles HTTP requests and form logic  
├── urls.py           - Route definitions  
├── templates/
│   ├── home.html
│   ├── book_table.html
│   ├── Booksform.html
│   ├── member.html
│   ├── member_table.html
│   ├── borrow.html
│   ├── issue_table.html
│   └── menu.html
└── media/
    ├── images/
    │   ├── books/
    │   └── members/
    └── Bg/

Templates Summary

- home.html – Homepage with navigation
- Booksform.html – Add/edit book details with image upload
- book_table.html – Display all books
- member.html – New member registration form
- member_table.html – List of registered members
- borrow.html – Issue book form
- issue_table.html – Book issue list
- menu.html – Navigation menu

How to Run

1. Clone the repository:
   git clone https://github.com/yourusername/django-library-management.git
   cd django-library-management

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate (or venv\Scripts\activate on Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py migrate

5. Create an admin user:
   python manage.py createsuperuser

6. Start the server:
   python manage.py runserver

7. Visit the application at:
   http://localhost:8000/library/home.html

Notes

- Ensure the media/ directory is present and properly configured in Django settings.
- Static and media files should be served correctly in development.

License

This project is open source and available for use and modification.
