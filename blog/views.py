from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Category, Tag, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from profile.models import Profile


def index(request):
    article = Article.objects.order_by('-id')
    articles = Article.objects.all()
    comments = Comment.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    popular_posts = Article.objects.order_by('-id')[:3]
    ctx = {
        'object_list': article,
        'tags': tags,
        'popular_posts': popular_posts,
        'articles': articles,
        'comments': comments,
        'categories': categories,
        'tags': tags

    }
    return render(request, 'wordify/index.html', ctx)


def post_views_up(request, pk):
    article = get_object_or_404(Article, id=pk)
    article.views += 1
    article.save()
    return redirect(reverse('blog:detail', kwargs={"pk": pk}))


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    articles = Article.objects.all()
    comments = Comment.objects.all()
    profile = Profile.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    popular_posts = Article.objects.order_by('-id')[:3]
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("account:login")
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    ctx = {
        'object': article,
        'profile': profile,
        'categories': categories,
        'tags': tags,
        'popular_posts': popular_posts,
        'form': form,
        'articles': articles,
        'comments': comments

    }
    return render(request, 'wordify/blog-single.html', ctx)


def article_list(request):
    article = Article.objects.all().order_by('-id')
    articles = Article.objects.all()
    comments = Comment.objects.all()
    popular_posts = Article.objects.order_by('-id')[:3]
    cat = request.GET.get('cat')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cat:
        article = article.filter(category__title__exact=cat)
    if tag:
        article = article.filter(tags__title__exact=tag)
    if search:
        article = article.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(article, 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
        'articles': articles,
        'comments': comments,
        'popular_posts': popular_posts,
        'categories': categories,
        'tags': tags,



    }
    return render(request, 'wordify/category.html', ctx)
