from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category
from .forms import CreatePostForm, UpdatePostForm
from django.urls import reverse_lazy

class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date_time']


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request, cat): 
    category_posts = Post.objects.filter(category=cat.replace('-', ' ')).order_by('-post_date_time')
    cat_menu = Category.objects.all()
    return render(request, 'category.html', 
    {'categorys_list':category_posts, 
    'title_cat':cat.replace('-', ' '),
    'cat_menu': cat_menu,
    })


class DetailsPage(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context



class CreatePostPage(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = CreatePostForm

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class DeletePostPage(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class UpdatePostPage(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdatePostForm

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context



