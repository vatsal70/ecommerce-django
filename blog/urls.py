from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, BlogDetailView, AddBlog, UpdateBlog, DeleteBlog, CategoryView, LikeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="Home"),
    path("index/", HomeView.as_view(), name="blogHome"),
    path("blogpost/<int:pk>", BlogDetailView.as_view(), name="blogPost"),
    path("edit/<int:pk>", UpdateBlog.as_view(), name="editPost"),
    path("<int:pk>/delete", DeleteBlog.as_view(), name="deletePost"),
    path("addblog/", AddBlog.as_view(), name="blogAdd"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="Contact"),
    path("catmenu/", views.catmenu, name="Catmenu"),
    path("category/<str:cats>/", CategoryView, name="categoryView"),
    path("like/<int:pk>/", LikeView, name="likepost"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)