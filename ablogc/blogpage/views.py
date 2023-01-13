from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import CreatePostForm, UpdatePostForm
from django.urls import reverse_lazy

class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date_time']



class DetailsPage(DetailView):
    model = Post
    template_name = 'detail.html'



class CreatePostPage(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = CreatePostForm


class DeletePostPage(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home-page')


class UpdatePostPage(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdatePostForm



def CategoryView(request, cat): 
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))
    return render(request, 'category.html', {'categorys_list':category_posts, 'title_cat':cat.replace('-', ' ')})