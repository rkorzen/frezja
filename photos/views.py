from django.shortcuts import HttpResponse, render
from photos.models import Photo, Gallery
from django.core.paginator import Paginator

# Create your views here.

def list(request):

    photos = Photo.objects.all()
    paginator = Paginator(photos, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "photos/list.html",
        dict(page=page_obj)
    )


def details(request, pk):
    return render(
        request,
        "photos/details.html",
        dict(photo=Photo.objects.get(pk=pk))
    )

def galleries(request):
    gls = Gallery.objects.all()
    paginator = Paginator(gls, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(
        request,
        "photos/galleries.html",
        dict(page=page_obj)
    )

def gallery(request, pk):
    g = Gallery.objects.get(pk=pk)
    paginator = Paginator(g.photos.all(), 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "photos/list.html",
        dict(page=page_obj)
    )
