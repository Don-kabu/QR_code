from django import forms
from .models import Document, Scan


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            "id",
            "label",
            "created_At",
            "unique_id",
            "file"
            ]

        widgets = {
            "id": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Document ID"}),
            "label": forms.TextInput(attrs={"class": "form-control", "placeholder": "Document label"}),
            "created_At": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "unique_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "Unique Identifier"}),
        }

