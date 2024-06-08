# forms.py

from django import forms
from .models import Ebook

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['title', 'author', 'pdf_file', 'thumbnail']
