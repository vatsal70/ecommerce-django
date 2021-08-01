from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, redirect
from .models import Post, Contact, Category
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from ckeditor.fields import RichTextField
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')



class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-post_id']


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def catmenu(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/catmenu.html', {'cat_menu_list': cat_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, post_id=request.POST.get('like_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blogPost', args=[str(pk)]))

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blogpost.html'


    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, post_id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddBlog(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/addblog.html'
    success_message = 'Your Blog has been added successfully'
    #fields = '__all__'


class UpdateBlog(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    form_class = EditForm
    success_url = reverse_lazy('blogHome')
    success_message = 'Your Blog has been updated successfully'
    #fields = ['title', 'sub_title', 'body', 'pub_date']



class DeleteBlog(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blogHome')
    success_message = 'Your Blog has been deleted successfully'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        data_to_return = super(DeleteBlog, self).delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message % obj.__dict__)
        return data_to_return


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'blog/categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        que = True
        return render(request, 'blog/contact.html', {'que': que})
    return render(request, 'blog/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 90:
        allposts = Post.objects.none()
    else:
        allposts1 = Post.objects.filter(title__icontains=query)
        allposts2 = Post.objects.filter(category__icontains=query)
        allposts = allposts1.union(allposts2)


    if allposts.count() == 0:
        messages.warning(request, 'Sorry User! Please try again.')

    params = {'allposts': allposts, 'query': query}
    return render(request, 'blog/search.html', params)
    #return HttpResponse("Done")

