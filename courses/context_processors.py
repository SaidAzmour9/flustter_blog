from .models import Course

def courses(request):
    l_courses = Course.objects.all()[0:3]
    
    return {'l_courses': l_courses}