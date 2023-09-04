from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView

from DSM_App.models import Student_reg, student_profile, Councelling, mentee_profile, mentee_details, Accomodation, \
    Qualification, Assignment


class Indexview(TemplateView):
    template_name = 'student/index.html'


class Student_Profile(TemplateView):
    template_name = 'student/student_profile.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        student = Student_reg.objects.get(user_id=self.request.user.id)

        rollnumber = request.POST['rollnumber']
        dob = request.POST['dob']
        age = request.POST['age']
        blood_group = request.POST['group']
        religion = request.POST['religion']
        caste = request.POST['caste']
        pa = request.POST['pa']
        ca = request.POST['ca']
        mn = request.POST['mn']
        tn = request.POST['tn']
        image = request.FILES['image']

        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        fe = student_profile()
        fe.student= student

        fe.rollnumber = rollnumber
        fe.dob = dob
        fe.age =age
        fe.blood_group = blood_group
        fe.religion = religion
        fe.caste = caste
        fe.permanent_address = pa
        fe.contact_address = ca
        fe.mob_number = mn
        fe.telephone_number = tn
        fe.image = filesss

        fe.save()
        return render(request, 'student/index.html', {'message': "Profile Updated"})

class Coun_noti(TemplateView):
    template_name = 'student/notifi.html'

    def get_context_data(self, **kwargs):
        f = Student_reg.objects.get(user_id=self.request.user.id)

        fe = Councelling.objects.filter(student_id=f.id)
        context = {
            'fe': fe
        }
        return context

class History(TemplateView):
    template_name = 'student/his.html'

    def get_context_data(self, **kwargs):

        context = super(History, self).get_context_data(**kwargs)
        f = Student_reg.objects.get(user_id=self.request.user.id)

        event = Councelling.objects.filter(student_id=f.id)
        context['event'] = event
        return context

class profile_update(TemplateView):
    template_name = 'student/profile_update.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        student = Student_reg.objects.get(user_id=self.request.user.id)

        nf = request.POST['nf']
        pf = request.POST['pf']
        af = request.POST['af']
        wf = request.POST['wf']
        mof = request.POST['mof']

        nm = request.POST['nm']
        pm = request.POST['pm']
        mm = request.POST['mm']
        sibi = request.POST['sibi']
        posi = request.POST['posi']
        lg = request.POST['lg']
        ag = request.POST['ag']
        pg = request.POST['pg']
        clg = request.POST['clg']
        mg = request.POST['mg']

        fe =mentee_profile()
        fe.father_name=nf
        fe.father_profession=pf
        fe.father_age=af
        fe.work_place=wf
        fe.father_number=mof
        fe.mother_name=nm
        fe.mother_profession=pm
        fe.mother_number=mm
        fe.siblings_in_SJCET=sibi
        fe.position=posi
        fe.local_guardian=lg
        fe.local_age=ag
        fe.guardian_proffe=pg
        fe.guardian_address=clg
        fe.guardian_number=mg
        fe.student= student

        fe.save()
        return render(request, 'student/index.html', {'message': "Successfully Updated"})


class more_details(TemplateView):
    template_name = 'student/more_details.html'
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        student = Student_reg.objects.get(user_id=self.request.user.id)

        host = request.POST['host']
        fre = request.POST['fre']
        st = request.POST['st']
        con = request.POST['con']
        et = request.POST['et']

        ex = request.POST['ex']
        curi = request.POST['curi']
        lp = request.POST['lp']
        ach = request.POST['ach']
        pg = request.POST['pg']
        go = request.POST['go']
        sg = request.POST['sg']
        str = request.POST['str']
        wee = request.POST['wee']
        op = request.POST['op']
        th = request.POST['th']
        ho = request.POST['ho']
        roll = request.POST['roll']

        fe =mentee_details()
        fe.hostel_or_not=host
        fe.visiting_home=fre
        fe.stay_details=st
        fe.conveyance=con
        fe.entrance_rank=et
        fe.experience=ex
        fe.extra_curricular=curi
        fe.language=lp
        fe.achievements=ach
        fe.personal_goal=go
        fe.professional_goal=pg
        fe.social_goal=sg
        fe.strength=str
        fe.weakness = wee
        fe.opportunity=op
        fe.threats=th
        fe.hobbies=ho
        fe.role_model=roll
        fe.student= student
        fe.save()
        return render(request, 'student/index.html', {'message': "Successfully Updated"})

class Accomodation_Details(TemplateView):
    template_name = 'student/accomodation.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        student = Student_reg.objects.get(user_id=self.request.user.id)

        from1 = request.POST['from']
        to = request.POST['to']
        reason = request.POST['reason']
        stay = request.POST['stay']
        et = request.POST['number']
        fe = Accomodation()
        fe.stay_duration_from = from1
        fe.stay_duration_to = to
        fe.reason = reason
        fe.stay_arranged = stay
        fe.no_hostel_owner=et
        fe.student=student
        fe.save()
        return render(request, 'student/index.html', {'message': "Successfully Updated"})

class Qualification_details(TemplateView):
    template_name = 'student/qualification.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        student = Student_reg.objects.get(user_id=self.request.user.id)

        q = request.POST['q']
        c = request.POST['c']
        b = request.POST['b']
        a = request.POST['a']
        m = request.POST['m']
        fe = Qualification()
        fe.quali = q
        fe.college = c
        fe.university = b
        fe.mark = a
        fe.medium=m
        fe.student=student
        fe.save()
        return render(request, 'student/index.html', {'message': "Successfully Updated"})

class view_feedback(TemplateView):
    template_name = 'student/view_assinment.html'

    def get_context_data(self, **kwargs):

        context = super(view_feedback,self).get_context_data(**kwargs)
        f = Student_reg.objects.get(user_id=self.request.user.id)
        view_pr = Assignment.objects.filter(student_id=f.id)

        context['view_pr'] = view_pr
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        fe = Assignment.objects.get(id=id)
        fe.image = filesss
        fe.save()
        return render(request, 'student/index.html', {'message': "Successfully Updated"})



class assi_feed(TemplateView):
    template_name = 'student/assig_feed.html'

    def get_context_data(self, **kwargs):

        context = super(assi_feed,self).get_context_data(**kwargs)
        f = Student_reg.objects.get(user_id=self.request.user.id)
        view_pr = Assignment.objects.filter(student_id=f.id)

        context['view_pr'] = view_pr
        return context


