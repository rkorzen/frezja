from django.shortcuts import HttpResponse, render

# Create your views here.

def list(request):
    return render(
        request,
        "posts/list.html",
        {"dane": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    )


def details(request, pk):
    return render(
        request,"posts/details.html",{}
    )
