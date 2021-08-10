import pyautogui
from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method=='POST':
        user1=request.POST['uname']
        pass1=request.POST['pwd']
        from django.contrib import auth
        user=auth.authenticate(username=user1,password=pass1)
        if user is not None:
            auth.login(request,user)
            from .models import uploads
            d=uploads.objects.all()
            return render(request, 'login.html', {'d':d})
        else:
            pyautogui.alert("Wrong username or password")
            return render(request,'loginpage.html')
    else:
        return render(request,'loginpage.html')

def upload(request):
    p=request.FILES['image']
    from .models import uploads
    d=uploads(pic=p)
    d.save()
    pyautogui.alert("Upload Done")
    d=uploads.objects.all()
    return render(request,'login.html',{'d':d})