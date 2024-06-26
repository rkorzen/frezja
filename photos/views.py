from django.shortcuts import HttpResponse, render
from photos.models import Photo

# Create your views here.

def list(request):
    return render(
        request,
        "photos/list.html",
        dict(photos=Photo.objects.all())
    )


def details(request, pk):
    return render(
        request,
        "photos/details.html",
        dict(photo=Photo.objects.get(pk=pk))
    )
