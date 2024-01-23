# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("gallery/", views.gallery, name="gallery"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("news/", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]