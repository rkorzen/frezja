
from django.shortcuts import render

from posts.models import Post
from django.core.paginator import Paginator

# Create your views here.

def list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(
      request,
     "posts/list.html",
      dict(posts=page_obj.object_list, page=page_obj)
    )


def details(request, pk):

    post = Post.objects.get(id=pk)

    return render(
        request, "posts/details.html", {"post":post}
    )
