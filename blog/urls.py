
from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='starting-page'),
    path('posts/', views.posts, name="posts-page"),
    path('posts/<slug:slug>/', views.posts_detail, name="posts-detail-page"),
]
