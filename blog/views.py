from django.views.generic import ListView

from .models import BlogModel


class BlogView(ListView):
    model = BlogModel
    template_name = 'blog/index.html'
    context_object_name = 'post'
