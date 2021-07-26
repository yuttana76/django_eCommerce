from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render , redirect

from .forms import ContactForm,LoginForm,RegisterForm

def home_page(request):
    context = {
        "title":"Hello World",
        "content": "Welcome to home page."
    }
    if request.user.is_authenticated:
        context['premium_content'] = "YYYYYYYY"
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
        "title":"About page",
        "content": "Welcome to about page."
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact page",
        "content": "Welcome to contact page.",
        "form":contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request,"contact/view.html",context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            context['form'] = LoginForm()
            return redirect('/')
        else:
            # No backend authenticated the credentials
            print('Error')
    
    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create_user(username,email,password)

    return render(request,"auth/register.html",context)