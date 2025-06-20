
# NotesApp – CS50x Final Project

### 👤 Author: Vinayak Pandey  
### 🎓 Course: CS50x 2025  
### 🌐 GitHub: [vinayak041205](https://github.com/me50/vinayak041205)  
### 📍 Location: [Mumbai, India]  
### 📅 Date: June 2025

---

### 📽️ Video Demo:
*(https://www.youtube.com/watch?v=r2HyKpxxesw)*

---

### 📄 Project Description

**NotesApp** is a full-stack web application built as my final project for CS50x 2025. It allows users to register, log in, and manage personal notes securely. It is designed to be simple, responsive, and secure, with a focus on user authentication, data privacy, and clean user experience. The project is built using **Python (Flask)** for the backend, **SQLite** for the database, and **HTML, CSS, and Bootstrap** for the frontend.

### 💡 Project Motivation

I chose to build NotesApp because I wanted to create a real-world application that incorporates everything I learned in CS50x — from backend logic and routing, to user authentication and frontend templating. I also wanted a project that showcases a full software development stack, including secure login systems, session handling, and CRUD (Create, Read, Update, Delete) operations.

### 🏗️ Features Overview

- **User Registration and Login**  
- **Create Notes**  
- **Edit Notes**  
- **Delete Notes**  
- **Responsive UI**

### 🧠 Technical Implementation

- **Backend**: Flask handles routing and server logic. Endpoints use decorators for access control.  
- **Database**: SQLite stores user and note data. CS50 SQL library handles queries.  
- **Sessions**: Flask session stores the user's login state.  
- **Frontend**: Jinja2 templates + Bootstrap 5 for clean responsive design.

### 📁 File Structure

- `app.py`: Main logic and routing  
- `templates/`: HTML templates (login, register, notes, layout)  
- `static/`: CSS or JS (if any)  
- `notes.db`: SQLite database  
- `requirements.txt`: Dependencies  
- `README.md`: This file

### 🛠️ Tools and Technologies

- Python 3  
- Flask  
- SQLite  
- Bootstrap  
- Jinja2  
- CS50 SQL Library  
- Werkzeug

### 🔐 Security Considerations

- Passwords hashed using Werkzeug  
- Parameterized SQL to prevent injection  
- User session controls access to data  
- Data access scoped per-user

### 🧪 Testing and Challenges

Tested all routes manually. Key challenges:
- Data access control per user
- Error handling (login issues, editing/deleting invalid notes)
- Making the interface user-friendly

### 🧱 Design Decisions

- Chose Flask with server-rendered templates for simplicity  
- SQLite for lightweight local storage  
- Bootstrap to avoid complex frontend work

### 📦 Deployment Notes

Run with:
```bash
pip install -r requirements.txt
flask run
```
Use CS50 IDE, or deploy on Replit/Heroku.

### 🎯 Learning Outcomes

Learned:
- Backend routing and logic
- Secure user login systems
- SQL data management and Jinja templating
- Full-stack app flow from database to frontend

### ✅ Conclusion

NotesApp is a secure, minimal note management tool that demonstrates core skills in full-stack development. It represents my complete CS50x learning journey.

---

**Thank you!**
