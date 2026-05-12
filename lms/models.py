from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# =========================
# USER (Custom User Model)
# =========================
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


# =========================
# CATEGORY (Self Reference)
# =========================
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    def __str__(self):
        return self.name


# =========================
# COURSE QUERYSET (OPTIMIZATION)
# =========================
class CourseQuerySet(models.QuerySet):
    def for_listing(self):
        return self.select_related('instructor', 'category')


# =========================
# COURSE
# =========================
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CourseQuerySet.as_manager()

    def __str__(self):
        return self.title


# =========================
# LESSON (ORDERING)
# =========================
class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"


# =========================
# ENROLLMENT QUERYSET
# =========================
class EnrollmentQuerySet(models.QuerySet):
    def for_student_dashboard(self):
        return self.select_related('course').prefetch_related('course__lessons')


# =========================
# ENROLLMENT (UNIQUE)
# =========================
class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    objects = EnrollmentQuerySet.as_manager()

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"


# =========================
# PROGRESS (TRACK LESSON)
# =========================
class Progress(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='progress'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='progress'
    )
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.lesson.title}"