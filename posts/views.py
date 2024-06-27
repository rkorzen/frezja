from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect

from posts.models import Post
from django.core.paginator import Paginator
from .forms import PostForm


# Create your views here.


def list(request):
    posts = Post.objects.filter(is_published=True).filter(
        publication_date__lte=timezone.now()
    )

    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(
        request,
        "posts/list.html",
        dict(posts=page_obj.object_list, page=page_obj)
    )


def details(request, pk):
    post = Post.objects.get(id=pk)

    return render(
        request, "posts/details.html", {"post": post}
    )


def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, "Dodano posta")
            return redirect("posts:details", post.id)
    return render(
        request, "posts/create.html", {"form": form}
    )
