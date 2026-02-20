from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            
            # 1. Send Notification to Admin
            send_mail(
                subject=f"New Portfolio Inquiry from {contact_msg.name}",
                message=contact_msg.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER], # Sending to self
                fail_silently=True,
            )
            
            # 2. Send Confirmation to User
            send_mail(
                subject="Thanks for contacting Aayush Sharma",
                message="I have received your message and will get back to you shortly.\n\nBest,\nAayush Sharma\nAI/ML Engineer",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[contact_msg.email],
                fail_silently=True,
            )
            
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})