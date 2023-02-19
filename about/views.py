from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from blog.models import Article, Category


def about(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    categories = Category.objects.all()
    popular_posts = Article.objects.order_by('-id')[:3]
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
        'categories': categories,
        'popular_posts': popular_posts
    }
    return render(request, 'wordify/about.html', ctx)