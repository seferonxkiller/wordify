from django.urls import path
from .views import index, article_detail, article_list, post_views_up

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', article_detail, name='detail'),
    path('detail/views/<int:pk>/', post_views_up, name='post_views_up'),
    path('list/', article_list, name='list')

]