from django import forms
from . import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.blog
        fields = ['title','slug','full_content','thumb']