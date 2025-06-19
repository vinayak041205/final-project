# NotesApp

#### Video Demo: <[https://youtu.be/your-demo-video-url](https://www.youtube.com/watch?v=r2HyKpxxesw)>
#### GitHub Repo: <https://github.com/vinayak041205/final-project>

#### Description:

NotesApp is a secure, full-stack web application built as my final project for CS50x 2025. It allows users to create, manage, and store their personal notes securely. Each user must register and log in to access their notes.

### 🧠 Features:

- User registration and secure login (with password hashing)
- Add, edit, and delete personal notes
- Timestamp each note
- All notes stored in a SQLite database
- Secure session handling using Flask-Session
- Bootstrap-based UI for responsiveness

### 🔧 Technologies:

- Python (Flask)
- SQLite (CS50 SQL library)
- HTML, CSS, Bootstrap
- Jinja2 for templating
- Flask-Session and Werkzeug for auth/security

### 🗂 File Overview:

| File / Folder           | Purpose                                      |
|-------------------------|----------------------------------------------|
| `app.py`                | Main Flask app with all route definitions   |
| `templates/`            | HTML templates with Jinja2 syntax           |
| ├ `layout.html`         | Base layout template                        |
| ├ `login.html`          | Login form                                  |
| ├ `register.html`       | Registration form                           |
| ├ `notes.html`          | Home/dashboard showing user notes           |
| ├ `add_note.html`       | Form for adding new notes                   |
| └ `edit_note.html`      | Form for editing existing notes             |
| `static/style.css`      | Basic styling for cards and layout          |
| `requirements.txt`      | Python dependencies                         |
| `README.md`             | This file (project documentation)           |

### 🔍 Design Decisions:

- I chose SQLite because it's lightweight and easy to integrate with CS50's SQL library.
- I used session handling via Flask-Session to ensure user data privacy across pages.
- I used Bootstrap to ensure a clean, responsive design for all screen sizes.

### 💡 What I Learned:

Building this app helped me understand routing, HTTP methods, SQL database relationships, user authentication, and full-stack integration using Flask. I also learned to debug HTML/JS errors and how to think through UI/UX from a user's perspective.

### 🚀 Future Improvements:

- Add note categories and search
- Add note sharing or collaboration
- Use PostgreSQL and deploy on a cloud server
- Integrate dark mode toggle for better UX

---

Thank you CS50 for this incredible journey!
