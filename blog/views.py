from django.shortcuts import render
from blog.models import About, Privacy, Terms, Support

# Create your views here.


def home(request):


    return render(request, 'blog/index.html', {})

def about(request):
    about = About.objects.first()

    return render(request, 'blog/about.html', {'about':about})

def support(request):
    support = Support.objects.first()

    return render(request, 'blog/support.html', {'support':support})

def terms(request):
    terms = Terms.objects.first()
    return render(request, 'blog/terms.html', {'terms':terms})

def privacy(request):
    privacy = Privacy.objects.first()


    return render(request, 'blog/privacy.html', {'privacy':privacy})
