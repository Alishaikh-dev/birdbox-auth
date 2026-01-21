# birdbox-auth
Secure authentication system with login and signup using FastAPI and password hashing.

# 🐦 BirdBox – Authentication System (FastAPI)

> *A simple and secure authentication app built with FastAPI.*

BirdBox is a beginner-friendly authentication project that implements **user signup and login** using **secure password hashing**.
All core logic is intentionally written in a **single file (`main.py`)** to keep the flow easy to read and understand.

This project focuses on **doing authentication the right way**, without unnecessary complexity.

---

## ✨ Features

* User Signup
* User Login
* Secure Password Hashing
* Database Integration
* Clean and readable logic
* Single-file implementation for learning clarity

Simple by design. Solid by principle.

---

## 🔐 Security Approach

BirdBox follows basic but essential security rules:

* Passwords are **hashed before storing**
* Plain text passwords are **never saved**
* Login verifies passwords using hash comparison

No shortcuts. No insecure patterns.

---

## 🛠️ Tech Stack

* **Backend**: Python (FastAPI)
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Password Hashing**: Passlib
* **API Type**: REST

Traditional backend concepts, modern tooling.

---

## 📂 Project Structure

```
birdbox/
│
├── main.py        # Complete application (auth + DB + routes)
└── README.md
```

Everything in one place. Easy to follow.

---

## 🚀 Application Flow

### Signup

1. User submits signup data
2. Password is hashed
3. Hashed password is stored in the database

### Login

1. User submits login credentials
2. Password is verified against stored hash
3. Login succeeds if credentials match

Clear. Predictable. Maintainable.

---

## ▶️ How to Run the Project

```bash
pip install fastapi uvicorn sqlalchemy passlib psycopg2
```

```bash
uvicorn main:app --reload
```

Open your browser at:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Why This Project?

Many authentication examples online are either:

* Over-engineered
* Or insecure

BirdBox is built to:

* Help beginners understand auth logic
* Show proper password handling
* Keep everything readable in one file

A strong foundation beats fancy shortcuts.

---

## 📌 Future Enhancements

* JWT Authentication
* OAuth (Google Login)
* Token refresh flow
* Project modularization

First correctness. Then scale.

---

## ⭐ Final Words

If this project helped you learn authentication concepts,
consider giving it a ⭐ on GitHub.

Small repo. Big fundamentals.


