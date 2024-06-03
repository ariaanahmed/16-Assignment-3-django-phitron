from django import forms
from .models import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title"}),
            
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                    "rows": 3,
                    "style": "resize: none;",
                }
            ),

            "add_a_category": forms.CheckboxSelectMultiple(
                attrs={
                    "style": "border: 1px solid black;",
                }
            ),

            "is_completed": forms.CheckboxInput(
                attrs={
                    "style": "border: 1px solid black;",
                }
            ),

            "assign_date": forms.DateInput(attrs={"type": "date"}),
        }
