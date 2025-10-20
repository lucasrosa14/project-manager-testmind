# bugs/forms.py
from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        # Use os campos atuais do modelo Bug
        fields = [
            'name', 
            'project', 
            'author', 
            'assignee_user', 
            'status', 
            'priority'
        ]
