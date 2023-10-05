from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils import timezone
from django.http import Http404
from .models import Post, Category

NUMBER_OF_POSTS_VISIBLE = 5


def get_request():
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now())
    return post_list


def index(request):
    """Page output index"""
    post_list = get_request().order_by('-pub_date')[:NUMBER_OF_POSTS_VISIBLE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Page output"""
    context = {'post': get_object_or_404(get_request(), pk=post_id)}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Page output category_posts"""
    category = Category.objects.filter(slug=category_slug)
    if category and not category.first().is_published:
        raise Http404
    posts = Post.objects.filter(
        category__is_published=True,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__slug=category_slug,
    )
    context = {'post_list': posts, 'category__slug': category_slug}
    return render(request, 'blog/category.html', context)
