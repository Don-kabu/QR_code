from django import forms
from .models import Document, Scan


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            "label",
            "file"
            ]

        widgets = {
            "label": forms.TextInput(attrs={"class": "form-control", "placeholder": "Document label"}),
        }

