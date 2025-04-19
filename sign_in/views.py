from django.shortcuts import render
from .forms import UserForm
from django.shortcuts import get_object_or_404
from .models import User

def user_dashboard(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    success_message = None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            success_message = "Profile updated successfully!"
    else:
        form = UserForm(instance=user)

    return render(request, 'user_dashboard.html', {'form': form, 'success_message': success_message})


def register_user(request):
    success_message = None

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "User registered successfully!"
            form = UserForm()  # Clear the form
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form, 'success_message': success_message})

