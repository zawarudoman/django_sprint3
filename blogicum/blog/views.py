from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils import timezone

from .models import Post


def index(request):
    """Page output index"""
    """READY"""
    template_homepage = 'blog/index.html'
    post_list = Post.objects.all().filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template_homepage, context)


def post_detail(request, pk):
    """Page output"""
    template = 'blog/detail.html'
    context = {'post': get_object_or_404(
        Post,
        pk=pk,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True)}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Page output category_posts"""
    template_category = 'blog/category.html'
    post_list = get_list_or_404(Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
    ), category__slug=category_slug)
    context = {'post_list': post_list}
    return render(request, template_category, context)
