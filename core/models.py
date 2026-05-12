from django.db import models
from django.contrib.auth.models import User

# COURSE
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='-')
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=200, null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


# COURSE MEMBER
ROLE_OPTIONS = [
    ('std', 'Siswa'),
    ('ast', 'Asisten')
]

class CourseMember(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.RESTRICT)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
    roles = models.CharField(max_length=3, choices=ROLE_OPTIONS, default='std')

    def __str__(self):
        return f"{self.user_id} - {self.course_id}"


# COURSE CONTENT
class CourseContent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='-')
    video_url = models.CharField(max_length=200, null=True, blank=True)
    file_attachment = models.CharField(max_length=200, null=True, blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.RESTRICT)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


# COMMENT
class Comment(models.Model):
    content_id = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    member_id = models.ForeignKey(CourseMember, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment


# COMPLETION
class Completion(models.Model):
    member_id = models.ForeignKey(CourseMember, on_delete=models.CASCADE)
    content_id = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    