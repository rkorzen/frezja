from django.shortcuts import render


# Create your views here.

def list(request):
    dct = dict()
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = 1

    dct['key'] = lst[index]

    return render(
        request,
        "posts/list.html",
        {"dane": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    )


def details(request, pk):
    return render(
        request, "posts/details.html", {}
    )
