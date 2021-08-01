from django.contrib import admin
from django.urls import path, include
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('editprofile/', UserEditView.as_view(), name='editProfile'),
    path('password/', PasswordsChangeView.as_view(template_name = 'registration/change-password.html'), name= 'password')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)