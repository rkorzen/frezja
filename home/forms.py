from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Reset, HTML
import re

id_pattern = re.compile("\d{3}-\w{2}-\d{3}")

class ContactForm(forms.Form):
    id = forms.CharField(max_length=10, required=False)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_id(self):
        id = self.cleaned_data.get("id")
        result = id_pattern.match(id)
        if result is None:
            raise forms.ValidationError("Niepoprawny identyfikator")
        return id

    def clean_name(self):
        name = self.cleaned_data.get("name")
        return name.capitalize()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email.lower()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "id",
            "name",
            HTML("Jakiś dopisek"),
            "email",
            "content",
            Submit("submit", "Wyslij"),
            Reset("reset", "Resetuj"),
            Button("xxx", "XXXX")
        )

