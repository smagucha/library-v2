from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomUserUpdateForm
from .models import User
def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

def updateprofile(request):

    if request.method =='POST':
        form= CustomUserUpdateForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = CustomUserUpdateForm(instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request, 'accounts/edit_profile.html', {'form': form,})
