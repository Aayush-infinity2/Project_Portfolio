from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'tech_stack', 'github_link', 'live_link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 4}),
            'tech_stack': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Python, Django, ML'}),
            'github_link': forms.URLInput(attrs={'class': 'w-full p-2 border rounded'}),
            'live_link': forms.URLInput(attrs={'class': 'w-full p-2 border rounded'}),
        }