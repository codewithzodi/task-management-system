<!-- ===================== BANNER ===================== -->

<h1 align="center">🚀 Task Management System</h1>

<p align="center">
Modern Full Stack Task Manager built with Flask & MySQL
</p>

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-UI-purple?style=for-the-badge&logo=bootstrap)
![MVC](https://img.shields.io/badge/MVC-Architecture-success?style=for-the-badge)

---

## 🌟 Project Overview

Task Management System is a **Full Stack Web Application** designed to manage daily workflow efficiently.

The system supports **multi-user authentication**, **task tracking**, and a **powerful admin dashboard** with full system control.

✅ Secure Login System  
✅ User Task Management  
✅ Admin Control Panel  
✅ Premium Dashboard UI  

---

## 🏗️ MVC Architecture

Model → MySQL Database
View → HTML + Bootstrap Templates
Controller → Flask Routes

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python
- Flask Framework

### 🔹 Frontend
- HTML5
- Bootstrap 5
- Jinja2 Templates
- Font Awesome Icons

### 🔹 Database
- MySQL

### 🔹 Version Control
- Git & GitHub

---

## 👤 User Features

✅ User Registration & Login  
✅ Password Hashing Security  
✅ Create Tasks  
✅ View Personal Tasks  
✅ Update Tasks  
✅ Delete Tasks  
✅ Search Tasks  
✅ Status Tracking  

---

## 👑 Admin Panel

### Admin Login
```bash
admin@gmail.com
```
```bash
password
```

### Admin Capabilities:

✅ View All Users  
✅ Monitor All Tasks  
✅ Edit Any Task  
✅ Delete Any Task  
✅ System Dashboard  
✅ Task Statistics  

---

## 📋 Task Attributes

| Attribute | Description |
|------------|-------------|
| Title | Task Name |
| Description | Task Details |
| Due Date | Deadline |
| Status | Pending / Progress / Completed |
| Remarks | Notes |
| Created On | Timestamp |
| Updated On | Timestamp |
| Created By | User |
| Updated By | User |

---
---

## 🗄️ Database Design

### 📌 ER Diagram

The system follows a relational database structure where each user can create and manage multiple tasks.

![ER Diagram](https://raw.githubusercontent.com/codewithzodi/task-management-system/main/er-diagram.png)---

### 📖 Data Dictionary

#### Users Table

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id | INT (PK) | Unique User Identifier |
| name | VARCHAR(100) | User Full Name |
| email | VARCHAR(100) | User Email |
| password | VARCHAR(255) | Encrypted Password |
| role | VARCHAR(20) | User Role (Admin/User) |

#### Tasks Table

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id | INT (PK) | Unique Task Identifier |
| title | VARCHAR(255) | Task Title |
| description | TEXT | Task Description |
| due_date | DATE | Task Deadline |
| status | VARCHAR(50) | Task Status |
| remarks | TEXT | Additional Notes |
| created_on | DATETIME | Creation Timestamp |
| updated_on | DATETIME | Last Updated Timestamp |
| created_by | INT (FK) | Task Creator ID |
| updated_by | INT (FK) | Last Updater ID |

---

### ⚡ Index Documentation

- Primary Key indexing is applied on `id` fields for faster record retrieval.
- Foreign Key indexing is implemented on `created_by` and `updated_by`.
- Search operations are optimized using indexed task title and status fields.

---


## 🔐 Authentication System

- Session Based Authentication
- Secure Password Hashing (Werkzeug)
- Route Protection
- Admin Authorization

---

## 🎨 Premium UI Features

✨ Modern Dashboard  
✨ Bootstrap Cards  
✨ Responsive Layout  
✨ Status Badges  
✨ Admin Analytics View  
✨ Clean Navigation  

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/codewithzodi/task-management-system.git
```
### 2️⃣ Navigate Project
```bash
cd task-management-system
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Setup Database
```bash
CREATE DATABASE taskdb;
```

### Update credentials inside:

**app/config.py**

### 5️⃣ Run Application
```bash
python run.py
```

### Open Browser:

```bash
http://127.0.0.1:5000
```

### 📁 Project Structure
```bash
task-manager/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── db.py
│ ├── config.py
│ │
│ └── templates/
│ ├── base.html
│ ├── index.html
│ ├── create_task.html
│ ├── edit_task.html
│ ├── login.html
│ ├── register.html
│ └── admin_dashboard.html
│
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧩 CRUD Operations

| Operation | Endpoint | Method | Description |
|------------|-----------|--------|-------------|
| Create | `/create` | POST | Create a new task |
| Read | `/` | GET | View all tasks |
| Update | `/edit/<id>` | POST | Update existing task |
| Delete | `/delete/<id>` | GET | Delete a task |
| Search | `/search` | POST | Search tasks by title or status |

---

---

## 👨‍💻 Developer Credits

### 🚀 Project Lead & Developer

**Yash Kumar (Zodi Bhai)**  
💻 Python Developer | 🔐 Cyber Security Enthusiast  

- 🔗 GitHub: [@CodeWithZodi](https://github.com/codewithzodi)  
- 📧 Email: mailzodibhai@gmail.com  

---

### 🤝 Contributors

Currently, this project is independently developed and maintained.

> Contributions, suggestions, and improvements are welcome for future versions.

---

⭐ *If you found this project useful, consider giving it a star on GitHub!*

---
