from django.urls import path
from .views import posts, posts_by_id

urlpatterns = [
    path("", posts, name="posts"),
    path("<int:post_id>/", posts_by_id, name="posts_by_id"),
]
