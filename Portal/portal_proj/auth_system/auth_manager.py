from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()  # Fetch CustomUser model

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # First check in Django's built-in authentication (SuperAdmin)
        user = authenticate(request, username=email, password=password)
        
        if not user:
            try:
                # If not a SuperAdmin, check in the CustomUser table
                user = User.objects.get(email=email)
                if user.check_password(password):  # Verify hashed password
                    login(request, user)
                else:
                    messages.error(request, "Invalid password!")
                    return redirect('login')
            except User.DoesNotExist:
                messages.error(request, "User does not exist!")
                return redirect('login')

        return redirect('dashboard')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
