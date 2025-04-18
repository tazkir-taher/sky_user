from django.shortcuts import render, redirect
from .forms import UserForm

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

