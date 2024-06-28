from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _

from home.models import UserInquiry
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, "base.html", {})


def contact(request):

    message = None
    form = ContactForm()
    if request.method == "POST":

        form = ContactForm(request.POST)
        if form.is_valid():

            UserInquiry.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["content"],
            )

            messages.add_message(request, messages.SUCCESS, "Zgłoszenie przyjęte")
            return redirect("photos:list")
            # form = ContactForm()
            # render(
            #     request, "contact.html", {"message": message, "form": form}
            # )

    return render(request, "contact.html", {"message": message, "form": form})


def about(request):
    return render(request, "about.html", {})



def set_language(request):
    user_language = 'pl'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect('/')

def check_spelling(request):
    response_data = _('This Url does not exist. Check spelling.')
    return HttpResponse(response_data)