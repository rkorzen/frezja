from django.shortcuts import HttpResponse, render

# Create your views here.

def list(request):
    return render(
        request,
        "photos/list.html",
        {}
    )

def details(request, pk):
    return HttpResponse(f"Tu będą szczegóły zdjęcia o id {pk}")
