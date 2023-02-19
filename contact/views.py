from django.shortcuts import render, redirect
from .forms import ContactForm
from blog.models import Category, Article


def contact(request):
    form = ContactForm(request.POST or None)
    categories = Category.objects.all()
    popular_posts = Article.objects.order_by('-id')[:3]
    if form.is_valid():
        form.save()
        return redirect('contact:index')
    ctx = {
        "form": form,
        "categories": categories,
        "popular_posts": popular_posts
    }
    return render(request, 'wordify/contact.html', ctx)
