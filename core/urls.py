from django.urls import path
from .views import courseStat, memberCourse, testing, allCourse, userCourses, userStat

urlpatterns = [
    path('test/', testing),
    path('courses/', allCourse),
    path('user-courses/', userCourses),
    path('course-stat/', courseStat),
    path('user-stat/', userStat),
    path('member-course/', memberCourse),
]