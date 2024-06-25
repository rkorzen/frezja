from django.shortcuts import render, HttpResponse

# Create your views here.

def list(request):
    return render(
        request,
        "posts/list.html",
        {}
    )


def details(request, pk):
    return render(
        request,
        "posts/details.html",
        {}
    )
