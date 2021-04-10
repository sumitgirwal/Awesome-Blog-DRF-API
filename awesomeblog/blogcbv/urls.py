from django.urls import path
from . import views
 
urlpatterns = [
    path("posts/",views.ListPostAPIView.as_view(),name="posts_list"),
    path("create/", views.CreatePostAPIView.as_view(),name="posts_create"),
    path("update/<int:pk>/",views.UpdatePostAPIView.as_view(),name="posts_update"),
    path("delete/<int:pk>/",views.DeletePostAPIView.as_view(),name="posts_delete")
]

