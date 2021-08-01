from django.contrib import admin

# Register your models here.
from .models import Post, Contact, Category


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Category)
