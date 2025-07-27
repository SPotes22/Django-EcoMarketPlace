from django.shortcuts import render,redirect
from item.models import Category,Item
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login
from .models import CustomUser
from .forms import CustomUserCreationForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories  = Category.objects.all()
    return render(request,'core/index.html',{
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request,'core/contact.html')



def singup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.ip_address = get_client_ip(request)
            user.save()
            messages.success(request, "Usuario creado correctamente. Espera activación.")
            return redirect('/login/')
    else:
        form = CustomUserCreationForm()
    return render(request,'core/singup.html', {'form': form})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return render(request,'dashboard/index.html')
