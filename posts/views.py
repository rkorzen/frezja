
from django.shortcuts import render

from posts.models import Post


# Create your views here.

def list(request):
    posts = Post.objects.all()
    dct = dict()
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = 1

    dct['key'] = lst[index]

    return render(
        request,
        "posts/list.html",
        {"posts": posts}
    )


def details(request, pk):

    post = Post.objects.get(id=pk)

    return render(
        request, "posts/details.html", {"post":post}
    )
