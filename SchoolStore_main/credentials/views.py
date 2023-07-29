from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpass']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"The Username is Taken")
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('credentials:login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('credentials:register')
    return render(request,"register.html")

def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('SSapp:newpage')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'credentials:login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('SSapp:home')
