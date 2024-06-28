from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm

from .models import Photo


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ["title", "opis", "status", "img"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "id",
            "title",
            "opis",
            "status",
            "img",
            Submit("submit", "Wyslij"),
        )

