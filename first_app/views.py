from urllib import response
from django.shortcuts import render
from django.urls import is_valid_path
from first_app.models import AccessRecord
from . import forms

# Login imports
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register(request):

    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm2(request.POST)
        profile_form = forms.UserProfileInfoForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            
            profile.save()
            
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = forms.UserForm2()
        profile_form = forms.UserProfileInfoForm()
        
    return render(
        request,
        "first_app/registrations.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        }
    )


@login_required
def special(request):
    return HttpResponse("You are Logged In, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("first_app:index"))

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("first_app:index"))
            return HttpResponse("ACCOUNT NOT ACTIVE")
        print("Someone tried login and failed.")
        print("Username: {} and Password: {}".format(username, password))
        return HttpResponse("Invalid login details supplied!!")
    return render(request, "first_app/login.html", {})

def new_user_form(request):
    form = forms.UserForm()
    
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    
    return render(request, "first_app/user_form.html", context={'form': form})


def form_page(request):
    form = forms.FormName()
    response = None
    if request.method=='POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            response = form.cleaned_data
            form.clean()
    return render(request, "first_app/form_page.html", context={'form': form, 'response': response or None})

def first_app_index(request):
    d = {
        "text": "Hey, This is first_app index page.",
        "number": 1000
    }
    return render(request, 'first_app/index.html', context=d)

def index(request):
    d= {}
    return render(request, "index.html", context=d)

def model_page(request):
    webps = AccessRecord.objects.order_by('date')
    d = { "access_records": webps }
    return render(request, "first_app/access_recs.html", context=d)

def help(req):
    return render(req, "first_app/help.html")

