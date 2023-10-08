from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

NUMBER_OF_POSTS_VISIBLE = 5


def get_request():
    return Post.objects.select_related(
        "category",
        "location",
        "author"
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    """Page output index"""
    post_list = get_request()[:NUMBER_OF_POSTS_VISIBLE]
    context = {"post_list": post_list}
    return render(request, "blog/index.html", context)


def post_detail(request, post_id):
    """Page output"""
    context = {"post": get_object_or_404(get_request(), pk=post_id)}
    return render(request, "blog/detail.html", context)


def category_posts(request, category_slug):
    """Page output category_posts"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_request().filter(category=category)
    context = {"post_list": posts, }
    return render(request, "blog/category.html", context)
