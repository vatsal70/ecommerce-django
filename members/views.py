from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfile, PasswordChangingForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView



# Create your views here.


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('blogHome')
    success_message = 'Your password has been updated successfully'


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Your Profile has been updated successfully'



class UserEditView(generic.UpdateView):
    form_class = EditProfile
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy('blogHome')
    
    def get_object(self):
        return self.request.user