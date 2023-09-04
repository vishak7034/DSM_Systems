from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from DSM_App.models import UserType,Student_reg
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

class Student_Reg(TemplateView):
    template_name = 'student_reg.html'


    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        address= request.POST['address']

        password = request.POST['password']
        if User.objects.filter(email=email):
            print ('pass')
            return render(request,'student_reg.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='1')
            user.save()
            us = Student_reg()
            us.user=user
            us.phone=phone
            us.address=address
            us.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "student"
            usertype.save()
            return render(request, 'index.html', {'message':"successfully added"})


class loginview(TemplateView):
    template_name = 'login.html'


    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "student":
                    return redirect('/student')
                elif UserType.objects.get(user_id=user.id).type == "mentor":
                    return redirect('/mentor')
                # elif UserType.objects.get(user_id=user.id).type == "public":
                #     return redirect('/public')

            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})
