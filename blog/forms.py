from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['article', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            "class": "form-control",
            "cols": 30,
            "rows": 10,
            "id": "message"
        })

