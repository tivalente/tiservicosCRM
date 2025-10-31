from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(request):
    return render(request, "login.html")


def submit_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            messages.error(
                request, "Usuário ou senha inválidos. Por favor, tente novamente."
            )

    return redirect("login")


def logout(request):
    auth_logout(request)
    return redirect("login")
