from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import NewUser


def home(request):
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def users(request):
    total = NewUser.objects.all()
    count = NewUser.objects.count()
    context = {"count": count, "total": total}
    return render(request, "users.html", context)



def details(request, user_id):
    total = NewUser.objects.all()
    user_detail = NewUser.objects.get(pk=user_id)
    context = {"user_detail": user_detail, "total": total}
    return render(request, "userdetail.html", context)


def password(request):
    return render(request, "password_done.html")


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]
        about = request.POST["about"]
        age = request.POST["age"]
        birth_date = request.POST["birth_date"]
        if password1 == password2:
            if NewUser.objects.filter(user_name=user_name).exists():
                messages.info(request, "Username Taken")
                return redirect("signup")
            elif NewUser.objects.filter(email=email).exists():
                messages.info(request, "User already exists")
                return redirect("signup")
            else:
                user = NewUser.objects.create_user(
                    user_name=user_name,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    about=about,
                    age=age,
                    birth_date=birth_date,
                )
                user.save()
                print("User created")
                return redirect("login")
        else:
            messages.info(request, "Password not matching")
            return redirect("signup")
    else:
        return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")
