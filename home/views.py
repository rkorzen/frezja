from django.shortcuts import render

from home.models import UserInquiry


# Create your views here.
def home(request):
    return render(
        request, "base.html", {}
    )


def contact(request):

    message = None

    if request.method == "POST":

        print(request.POST)

        adres_email = request.POST.get("email")
        imie = request.POST.get("name")
        content = request.POST.get("content")

        UserInquiry.objects.create(
            name=imie,
            email=adres_email,
            message=content
        )

        message = "Dziekujemy za zgłoszenie. Odpowiadamy na podany adres email."
        message = "Dziękujemy za zgłoszenie!"

    return render(
        request, "contact.html", {"message": message}
    )
