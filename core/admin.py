from django.contrib import admin
from .models import Course, CourseMember, CourseContent, Comment, Completion

admin.site.register(Course)
admin.site.register(CourseMember)
admin.site.register(CourseContent)
admin.site.register(Comment)
admin.site.register(Completion)