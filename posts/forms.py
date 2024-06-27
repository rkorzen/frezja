from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "title",
            "content",
            Submit("submit", "Wyslij"),
        )
