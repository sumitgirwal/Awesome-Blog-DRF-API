from django.urls import path
from . import views

urlpatterns = [
	path('posts/', views.posts, name = 'posts'),
	path('posts/<int:pk>/', views.posts_details, name = 'posts_details')
]


