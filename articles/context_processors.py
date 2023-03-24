from .models import Article

def courses(request):
    l_articles = Article.objects.all()[0:3]
    
    return {'l_articles': l_articles }