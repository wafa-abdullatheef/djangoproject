from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import RegisterForm,LoginForm,UpdateForm,ChangePasswordForm,GalleryForm
from . models import Signup,Gallery
from project18 import settings
from django.core.mail import send_mail

from django.contrib import messages
from django.contrib.auth import logout as logouts
def index(request):
    text=" to gtec"
    return render(request,'index.html',{'data':text}) #context

# def signup(request):
#     form=RegisterForm()
#     return render(request,'signup.html',{'form':form})
def signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'email already exists.')
                return redirect('/Signup')
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/Signup')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"successfully saved")
                return redirect('/')
    else:
                form=RegisterForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
        
            try:
                user=Signup.objects.get(Email=email)
                if not user:
                    messages.warning(request,'account does not exists')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'incorrect password')
                    return redirect('/login')
                else:
                    messages.success(request,"welcome")
                    return redirect('/home/%s' % user.id )
            except:
                messages.warning(request,'email or password incorrect')
                return redirect('/login')
    else:
            form=LoginForm()
    return render(request,'login.html',{'form':form})


def home(request,id):
     user=Signup.objects.get(id=id)
     return render(request,'home.html',{'user':user})
def showusers(request):
     users=Signup.objects.all()
     return render(request,'showusers.html',{'users':users})
def update(request,id):
    users=Signup.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=users)
        if form.is_valid():
            form.save()
            messages.success(request,'updated')
            return redirect('/showusers')
    else:
         form=UpdateForm(instance=users)
    return render(request,'update.html',{'form':form,'users':users})
def delete(request,id):
     user=Signup.objects.get(id=id)
     user.delete()
     messages.success(request,"successfully deleted")
     return redirect('/showusers')
def changepassword(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            newpassword=form.cleaned_data['NewPassword']

            if user.Password!=oldpassword:
                messages.warning(request,'password doesnt match')
                return redirect('/changepassword/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,'password is similar to old password')
                return redirect('/changepassword/%s' % user.id)
            elif newpassword!=confirmpassword:
                 messages.warning(request,'doesnt match')
                 return redirect('/changepassword/%s' % user.id)
            
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,"password changed")  
                return redirect('/home/%s' % user.id) 
    else:
         form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'user':user})
            
def logout(request):
     logouts(request)
     messages.success(request,'logged out successfully')
     return redirect('/')
def gallery(request):
    if request.method=='POST':
        form=GalleryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Gallery.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'email already exists.')
                return redirect('/gallery')
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/gallery')
            else:
                tab=Gallery(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"successfully saved")
                return redirect('/')
    else:
                form=GalleryForm()
    return render(request,'gallery.html',{'form':form})
def showimages(request):
     images=Gallery.objects.all()
     return render(request,'showimages.html',{'images':images})
def mail(request):
     if request.method=='POST':
          cname=request.POST.get('contact_name')
          cemail=request.POST.get('contact_email')
          cmessage=request.POST.get('contact_message')
          toemail='wafaaslam95@gmail.com'
          res    =send_mail(cname, cmessage, settings.EMAIL_HOST_USER, [toemail],fail_silently=False)
          if(res==1):
               msg= "Mail sent Successfully"
          else:
               msg= "mail could not send"
          return HttpResponse(msg)
     else:
          return render(request,'index.html')