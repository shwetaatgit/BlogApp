from django import forms
from . import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.blog
        fields = ['title','slug','full_content','thumb']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'full_content': forms.Textarea(attrs={'class':'form-control'}),
        }
       