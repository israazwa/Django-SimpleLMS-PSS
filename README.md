# Simple LMS - Django Docker

## 📌 Deskripsi

Project ini merupakan implementasi Simple Learning Management System (LMS) menggunakan Django yang dijalankan dengan Docker Compose dan PostgreSQL sebagai database.

---

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

Nama: Ravicenna Mahardhika
NIM : A11.2023.15296
