from django.contrib import messages
from django.shortcuts import render, redirect

from home.models import UserInquiry
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(
        request, "base.html", {}
    )


def contact(request):

    message = None
    form = ContactForm()
    if request.method == "POST":

        form = ContactForm(request.POST)
        if form.is_valid():

            UserInquiry.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["content"]
            )

            messages.add_message(request, messages.SUCCESS, "Zgłoszenie przyjęte")
            return redirect("photos:list")
            # form = ContactForm()
            # render(
            #     request, "contact.html", {"message": message, "form": form}
            # )

    return render(
        request, "contact.html", {"message": message, "form": form}
    )
