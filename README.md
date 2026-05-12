# 📚 Simple LMS - Django + Docker

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Compose-lightblue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow)

> 🚀 Implementasi **Simple Learning Management System (LMS)** menggunakan **Django**, berjalan di atas **Docker Compose**, dengan **PostgreSQL** sebagai database utama.

---

## 📌 Deskripsi

Project ini merupakan implementasi LMS sederhana yang mendukung multi-role user (Admin, Instructor, Student), pengelolaan course & lesson, serta tracking progress.  
Dibangun 

## 🚀 Cara Menjalankan

1. Jalankan Docker:
   docker-compose up --build

2. Buka browser:
   http://localhost:8000

3. Login admin:
   http://localhost:8000/admin

---

## ⚙️ Teknologi yang Digunakan

* Django
* PostgreSQL
* Docker & Docker Compose

---

## 🧩 Fitur Utama

* Custom User (Admin, Instructor, Student)
* Category (hierarchy)
* Course & Lesson
* Enrollment
* Progress tracking
* Django Admin Interface

---

## 📸 Screenshot

### 🔹 Django Welcome Page

![Welcome](img/Django%20Wellcome%20Page.png)

### 🔹 Django Login

![Login](img/Django%20Login.png)

### 🔹 Django Admin Dashboard

![Admin](img/Django%20Admin.png)

### 🔹 Input Data (Admin)

![Input](img/Django%20Input.png)

### 🔹 Docker Running

![Docker](img/PS%20Docker%202.png)

---

## ⚡ Query Optimization

Project ini menggunakan:

* select_related()
* prefetch_related()

Untuk menghindari N+1 query problem.

---

## 📦 Database

Menggunakan PostgreSQL dengan konfigurasi:

* DB_NAME=postgres
* DB_USER=postgres
* DB_PASSWORD=postgres
* DB_HOST=db
* DB_PORT=5432

---

## ✅ Hasil

* Django berhasil berjalan di localhost:8000
* PostgreSQL terhubung dengan baik
* Data dapat disimpan dan dikelola melalui admin
* Docker container berjalan dengan normal

---

## 👨‍💻 Author

Nama: Isra Shahzada Azwa Saqiba
NIM : A11.2023.15287
