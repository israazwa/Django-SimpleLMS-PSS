import os
import sys
import django
import csv

# Tambahkan path project
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set setting Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simplelms.settings')

# Inisialisasi Django
django.setup()

from django.contrib.auth.models import User
from core.models import Course, CourseMember

print("Mulai import data...")

# =========================
# IMPORT USER
# =========================
try:
    with open('./csv_data/user-data.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not User.objects.filter(username=row['username']).exists():
                User.objects.create_user(
                    username=row['username'],
                    password=row['password'],
                    email=row['email']
                )
                print(f"User {row['username']} berhasil ditambahkan")
except Exception as e:
    print("Error import user:", e)


# =========================
# IMPORT COURSE
# =========================
try:
    with open('./csv_data/course-data.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Course.objects.create(
                name=row['name'],
                description=row['description'],
                price=int(row['price']),
                teacher=User.objects.get(pk=int(row['teacher']))
            )
            print(f"Course {row['name']} berhasil ditambahkan")
except Exception as e:
    print("Error import course:", e)


# =========================
# IMPORT MEMBER
# =========================
try:
    with open('./csv_data/member-data.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            CourseMember.objects.create(
                course_id=Course.objects.get(pk=int(row['course_id'])),
                user_id=User.objects.get(pk=int(row['user_id'])),
                roles=row['roles']
            )
            print(f"Member user_id {row['user_id']} ke course {row['course_id']} berhasil")
except Exception as e:
    print("Error import member:", e)


print("=== IMPORT SELESAI ✅ ===")