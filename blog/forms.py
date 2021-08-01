from django import forms
from .models import Post, Category


cat_choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in cat_choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'sub_title', 'body', 'category', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User', 'value': '', 'id': 'auth', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Sub-Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Content'}),
            

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'sub_title', 'body', 'category', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Sub-Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Content'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),

        }