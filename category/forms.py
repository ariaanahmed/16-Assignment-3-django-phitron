from django import forms
from .models import Category
from django.forms.widgets import CheckboxSelectMultiple


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "category_name": forms.TextInput(
                attrs={
                    "style": "border: 1px solid black;",
                }
            ),
            "categories": CheckboxSelectMultiple(
                attrs={
                    "style": "border: 1px solid black; padding: 5px;",
                }
            ),
        }
