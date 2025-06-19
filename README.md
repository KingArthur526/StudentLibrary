# Django Library Management System

A web-based Library Management System built with Django. It enables librarians and users to manage books, members, and book borrowing records through a simple and functional interface.

## Features

- Add and manage books with metadata and cover images
- Register new library members with photos
- Issue books to members and set return dates
- Display uploaded book and member images
- View all entries in structured HTML tables
- Built-in date pickers and form validation

## Tech Stack

- Backend: Python, Django  
- Frontend: HTML, CSS (inline styling)  
- Database: SQLite (default Django DB)  
- Media Handling: Django file/image uploads

## Project Structure
```
library/
├── models.py # Book, BookIssue, Lib_Member models
├── forms.py # Forms for Book, Issue, Member
├── views.py # View logic and routing
├── urls.py # URL patterns
├── templates/
│ ├── home.html
│ ├── book_table.html
│ ├── Booksform.html
│ ├── member.html
│ ├── member_table.html
│ ├── borrow.html
│ ├── issue_table.html
│ └── menu.html
└── media/
└── images/
├── books/
└── members/
└── Bg/
```

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
