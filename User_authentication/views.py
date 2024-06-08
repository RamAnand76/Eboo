import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def password_strength(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    return True, ""

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            is_strong, message = password_strength(password)
            if not is_strong:
                messages.info(request, message)
                return redirect('signup')

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('profile')
        else:
            messages.info(request, "Passwords do not match")
            return redirect("signup")
    else:
        return render(request, "signup.html")
  
def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials...!")
            return redirect("signin")
    else:
        return render(request, "login.html")

@login_required(login_url="signin")
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('/')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = ProfileUpdateForm(instance=user_profile)

    user_type = "Both" if user_profile.is_reader and user_profile.is_author else "Reader" if user_profile.is_reader else "Author"

    context = {
        'form': form,
        'user_profile': user_profile,
        'user_type': user_type,
    }
    
    return render(request, "profile.html", context)

@login_required(login_url="signin") 
def index(request):
    return render(request, 'home.html')

@login_required(login_url="signin")    
def logout(request):

    auth.logout(request)
    return redirect("signin")