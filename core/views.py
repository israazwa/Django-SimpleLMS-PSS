from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Course
from django.core import serializers
from django.db.models import Count, Avg, Max, Min

def testing(request):

    user_test = User.objects.filter(username="usertesting")

    if not user_test.exists():
        user_test = User.objects.create_user(
            username="usertesting",
            email="user@test.com",
            password="123"
        )

    all_users = serializers.serialize('python', User.objects.all())

    admin = User.objects.get(pk=1)

    user_test.delete()

    after_delete = serializers.serialize('python', User.objects.all())

    return JsonResponse({
        "admin": serializers.serialize('python', [admin])[0],
        "all_users": all_users,
        "after_delete": after_delete
    })


def allCourse(request):
    courses = Course.objects.all()

    result = []

    for c in courses:
        result.append({
            'id': c.id,
            'name': c.name,
            'price': c.price,
            'teacher': {
                'id': c.teacher.id,
                'username': c.teacher.username,
                'email': c.teacher.email,
            }
        })

    return JsonResponse(result, safe=False)


def userCourses(request):
    user = User.objects.get(pk=1)
    courses = Course.objects.filter(teacher=user)

    data = []

    for c in courses:
        data.append({
            'id': c.id,
            'name': c.name,
            'price': c.price
        })

    return JsonResponse({
        'user': user.username,
        'courses': data
    })

def courseStat(request):
    data = Course.objects.aggregate(
        total_course=Count('id'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    return JsonResponse(data)

def userStat(request):
    data = User.objects.aggregate(
        total_user=Count('id')
    )

    return JsonResponse(data)

def memberCourse(request):
    from .models import CourseMember

    data = CourseMember.objects.select_related('course_id', 'user_id')

    result = []

    for m in data:
        result.append({
            'user': m.user_id.username,
            'course': m.course_id.name,
            'role': m.roles
        })

    return JsonResponse(result, safe=False)