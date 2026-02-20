from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from projects.models import Project
from contact.models import ContactMessage

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    # Only Admin sees messages and full project controls
    messages_list = None
    if request.user.is_superuser:
        messages_list = ContactMessage.objects.all().order_by('-created_at')
    
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'accounts/dashboard.html', {
        'projects': projects,
        'messages_list': messages_list
    })