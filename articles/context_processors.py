from .models import Article

def articles(request):
    l_articles = Article.objects.all()[0:6]
    
    return {'l_articles': l_articles }