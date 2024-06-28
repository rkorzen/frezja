from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm, modelformset_factory

from .models import Photo, Gallery


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

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ["title", "description"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "title",
            "description",
            Submit("submit", "Wyslij"),
        )

PhotoFormSet = modelformset_factory(
    Photo,
    form=PhotoForm,
    extra=1,
    can_delete=True,
)