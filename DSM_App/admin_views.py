from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from DSM_App.models import Student_reg, UserType, Mentor_reg, Assign


class adminIndex(TemplateView):
    template_name = 'admin/index.html'


class Mentor_regstration(TemplateView):
    template_name = 'admin/mentor_reg.html'
    def get_context_data(self, **kwargs):

        context = super(Mentor_regstration,self).get_context_data(**kwargs)
        stu = Student_reg.objects.all()
        context['stu'] = stu
        return context


    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        # student= request.POST['student']
        qualification= request.POST['Qualification']
        college_id=request.POST['college_id']
        password = request.POST['password']
        if User.objects.filter(email=email):
            print ('pass')
            return render(request,'admin/index.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='1')
            user.save()
            us = Mentor_reg()
            us.user=user
            us.phone=phone
            us.college_id=college_id
            # us.student_id=student
            us.qualification=qualification
            us.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "mentor"
            usertype.save()
            return render(request, 'admin/index.html', {'message':"successfully added"})

class view_Mentor(TemplateView):
    template_name = 'admin/mentor_views.html'
    def get_context_data(self, **kwargs):

        context = super(view_Mentor,self).get_context_data(**kwargs)
        mentor = Mentor_reg.objects.all()
        context['mentor'] = mentor
        return context


class Assign_Mentor(TemplateView):
    template_name = 'admin/assign_student.html'

    def get_context_data(self, **kwargs):
        context = super(Assign_Mentor, self).get_context_data(**kwargs)
        mentor = Mentor_reg.objects.all()
        student = Student_reg.objects.all()

        context['mentor'] = mentor
        context['student'] = student

        return context

    def post(self, request, *args, **kwargs):

        mentor = request.POST['mentor']
        student = request.POST['student']
        fe = Assign()

        fe.mentor_id = mentor
        fe.student_id = student
        fe.save()
        return render(request, 'admin/index.html', {'message': "Successfully Assigned"})

class view_student(TemplateView):
    template_name = 'admin/student_view.html'
    def get_context_data(self, **kwargs):

        context = super(view_student,self).get_context_data(**kwargs)
        student = Student_reg.objects.all()
        context['student'] = student
        return context

class Delete_Student(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id1 = request.GET['userid']

        student=User.objects.get(id=id1)
        if request.method == 'POST':
            student.delete()

            return render(request, 'admin/index.html',{'message': "Successfully Deleted"})
        context = {
            'student': student,
        }
        return render(request, 'admin/delete.html',context)
#
# def delete_student(request, id):
#     student = Student_reg.objects.get(id=id)
#
#     if request.method == 'POST':
#         student.delete()
#         return redirect('view_student')
#
#     context = {
#         'student': student,
#     }
#     return render(request, 'delete.html', context)
class Delete_Mentor(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id1 = request.GET['userid']

        mentor=User.objects.get(id=id1)
        if request.method == 'POST':
            mentor.delete()

            return render(request, 'admin/index.html',{'message': "Successfully Deleted"})
        context = {
            'mentor': mentor,
        }
        return render(request, 'admin/mentor_delete.html',context)



class Assigned_mentor(TemplateView):
    template_name = 'admin/assiged_teacher.html'
    def get_context_data(self, **kwargs):

        employees = Assign.objects.all()
        context = {
            'mentor': employees,
        }
        return context

class update_mentor(TemplateView):
    template_name = 'admin/update_mentor.html'

    def get_context_data(self, **kwargs):

        mentor = Mentor_reg.objects.all()
        context = {
            'mentor': mentor,
        }
        return context

    def post(self, request, *args, **kwargs):

        id = self.request.GET['id']
        assign = Assign.objects.get(pk=id)
        mentor = request.POST['mentor']
        assign.mentor_id=mentor
        assign.save()
        return render(request, 'admin/index.html', {'message': "Successfully Updated"})


class Delete_assiged(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id1 = request.GET['userid']

        assing=Assign.objects.get(id=id1)
        if request.method == 'POST':
            assing.delete()

            return render(request, 'admin/index.html',{'message': "Successfully Deleted"})
        context = {
            'assign': assing,
        }
        return render(request, 'admin/assign_delete.html',context)

