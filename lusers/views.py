from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        
        user = authenticate(request, username = loginusername, password = loginpassword)
        
        
        if user is not None:
            login(request, user)
            return redirect('userlogin')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
     
    return render(request, 'lusers/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')