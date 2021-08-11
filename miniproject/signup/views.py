import pyautogui as pu
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        un = request.POST['uname']
        fn = request.POST['fname']
        ln = request.POST['lname']
        email = request.POST['mailid']
        passwd = request.POST['pwd']
        if User.objects.filter(username=un).exists():
            pu.alert("Username already exists")
            return render(request,'signup.html')
        else:
            user = User.objects.create_user(username=un,first_name=fn,last_name=ln,email=email,password=passwd)
            user.save()
            pu.confirm("user created")
            return redirect('/')
    else:
        return render(request,'signup.html')
