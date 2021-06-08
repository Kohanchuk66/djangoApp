from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from cart.forms import CartAddProductForm
from testApp.models import Voucher, Order
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def index(request):
    vouchers = Voucher.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, "index.html", {"vouchers": vouchers, 'cart_product_form': cart_product_form})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request, "register.html", {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/profile")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def changeData(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST.get("name")
        user.first_name = request.POST.get("name")
        user.last_name = request.POST.get("surname")
        user.email = request.POST.get("email")
        user.save()
    else:
        return render(request, 'editProfile.html', {})
    return redirect("/")


def profile(request):
    return render(request, 'profile.html', {})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {"orders":orders})

