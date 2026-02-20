from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border rounded bg-gray-50', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 border rounded bg-gray-50', 'placeholder': 'your@email.com'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-3 border rounded bg-gray-50', 'rows': 5, 'placeholder': 'How can I help you?'}),
        }