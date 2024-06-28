from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from photos.forms import PhotoForm
from photos.models import Gallery
from photos.models import Photo


# Create your views here.


def list(request):
    photos = Photo.objects.all()
    paginator = Paginator(photos, 20)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "photos/list.html", dict(page=page_obj))


def details(request, pk):
    return render(request, "photos/details.html", dict(photo=Photo.objects.get(pk=pk)))


def create(request):
    if request.method == "GET":
        return render(request, "photos/create.html", {"form": PhotoForm()})
    else:
        try:
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                new_photo = form.save()
                return redirect("photos:details", new_photo.id)
            else:
                return render(
                    request, "photos/create.html", {"form": form, "error": "złe dane!"}
                )
        except ValueError:
            return render(
                request,
                "photos/create.html",
                {"form": PhotoForm(), "error": "złe dane!"},
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



def create_gallery(request):
    return render(request, "photos/create_gallery.html")