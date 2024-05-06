from django.shortcuts import render,  redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUp, AddForm
from .models import Record

# Create your views here.
def index(request):
    record = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('index')
        else:
            messages.success(request, "Error occured while logging in.")
            return redirect('index')
    else:
        return render(request, 'layouts/index.html', {'record':record})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You have been registered.")
            return redirect('index')
    else:
        form = SignUp()
        return render(request, 'layouts/register.html', {'form':form})
    
    return render(request, 'layouts/register.html', {'form':form})

def record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = pk)
        return render(request, 'layouts/record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You have to be logged in...")
        return redirect('index')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        deleted_user = Record.objects.get(id = pk)
        deleted_user.delete()
        return redirect('index')
    else:
        messages.success(request, "you have to be logged in")
        return redirect('index')
    
def add_record(request):
    form = AddForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record added")
                return redirect('index')
        else:

            return render(request, 'layouts/add_record.html', {'form':form})
    else:
        messages.success(request, "You have to be logged in")
        return redirect('index')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddForm(request.POST or None, instance=current_record)
        if request.method =='POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated.")
                return redirect('index')
        else:
            return render(request, 'layouts/update_record.html', {'form':form})
    else:
        messages.success(request, "You have to be logged in")
        return redirect('index')            
        