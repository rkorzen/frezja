from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Reset, HTML

from .models import Photo


# class PhotoForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ModelForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update({'class': 'form-control'})
#         self.fields['opis'].widget.attrs.update({'class': 'form-control'})
#         self.fields['status'].widget.attrs.update({'class': 'form-control'})
#         self.fields['img'].widget.attrs.update({'class': 'form-image-input'})
#         self.fields['tags'].widget.attrs.update({'class': 'form-control'})
#
#     class Meta:
#         model = Photo
#         fields = ['title', 'opis', 'status', 'img', 'tags']
#         labels = {
#             'title': ('Tytuł'),
#             'img': ('Zdjęcie'),
#         }
#         widgets = {'opis': Textarea(attrs={'rows': 4}),
#                    }


class PhotoForm(ModelForm):

    # id = forms.CharField(max_length=10, required=False)
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # content = forms.CharField(widget=forms.Textarea)

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
