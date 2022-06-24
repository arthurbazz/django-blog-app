from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.


class PostListView(ListView):
    # model
    model = Post


class PostCreateView(CreateView):
    # model
    model = Post
    # fields to be displayed
    fields = '__all__'
    success_url = reverse_lazy('blog:all')


class PostDetailView(DetailView):
    # model
    model = Post


class PostUpdateView(UpdateView):
    # model
    model = Post
    # fields to be displayed
    fields = '__all__'
    success_url = reverse_lazy('blog:all')


class PostDeleteView(DeleteView):
    # model
    model = Post
    # fields to be displayed
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
