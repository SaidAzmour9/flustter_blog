from .models import Course

def courses(request):
    courses = Course.objects.all()
    l_courses = Course.objects.all()[0:6]
    
    return {'l_courses': l_courses, 'courses': courses}