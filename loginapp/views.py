from django.shortcuts import render

from.models import RegistrationData
from.forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse
def main_page_view(request):
    return render(request,'main_page.html')
def reg_view(request):
    if request.method == "POST":
        rform =RegistrationForm(request.POST)
        if rform.is_valid():
            first_name = rform.cleaned_data.get('first_name','')
            last_name = rform.cleaned_data.get('last_name','')
            user_name = rform.cleaned_data.get('user_name','')
            password = rform.cleaned_data.get('password','')
            mobile = rform.cleaned_data.get('mobile','')
            email = rform.cleaned_data.get('email','')
            data = RegistrationData(
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                password=password,
                mobile=mobile,
                email=email
            )
            data.save()
            rform=RegistrationForm()
            return render(request,'registration_page.html',{'rform':rform})
        else:
            return HttpResponse("User Invalid Data")
    else:
         rform=RegistrationForm()
         return render(request,'registration_page.html',{'rform':rform})
    return render(request,'registration_page.html')
def login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('User Name','')
            password = request.POST.get('Password','')
            uname1 = RegistrationData.objects.filter(user_name=uname)
            password1 =RegistrationData.objects.filter(password=password)
            if uname1 and password1:
                return HttpResponse("Correct User And Password")
            else:
                return HttpResponse("Wrong User And Password")
        else:
            return  HttpResponse("Invalid Data")
    else:
        lform = LoginForm()
        return render(request,'login_form.html',{'lform':lform})