from django.contrib import admin
from .models import Category, Tag, Article, Comment, ArticleText, ArticleImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_date']
    list_filter = ['category', 'tags']
    date_hierarchy = 'created_date'
    filter_horizontal = ['tags', ]
    search_fields = ['title']


@admin.register(ArticleText)
class ArticleTextAdmin(admin.ModelAdmin):
    list_filter = ['id', 'description', 'created_date']
    date_hierarchy = 'created_date'


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_filter = ['id', 'image', 'created_date']
    date_hierarchy = 'created_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ['id', 'author', 'article', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['article__title', 'author__username', 'author__first_name', 'author__last_name']
    autocomplete_fields = ['article', 'author']
