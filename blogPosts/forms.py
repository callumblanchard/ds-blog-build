from .models import BlogPost, Comment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )
