from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import TemplateView
from xhtml2pdf import pisa

from DSM_App.models import Mentor_reg, Assign, Student_reg, Councelling, mentee_first_meeting, overall, student_profile, \
    mentee_profile, Assignment


class Indexview(TemplateView):
    template_name = 'teacher/index.html'



class Student_under(TemplateView):
    template_name = 'teacher/students.html'


    def get_context_data(self, **kwargs):

        context = super(Student_under,self).get_context_data(**kwargs)
        f = Mentor_reg.objects.get(user_id=self.request.user.id)
        view_pr = Assign.objects.filter(mentor_id=f.id)

        context['view_pr'] = view_pr
        return context


class History(TemplateView):
    template_name = 'teacher/coun_history.html'

    def get_context_data(self, **kwargs):

        context = super(History, self).get_context_data(**kwargs)
        id = self.request.GET['id']

        event = Councelling.objects.filter(student_id=id)
        context['event'] = event
        return context
class Feedback_his(TemplateView):
    template_name = 'teacher/view_feedback.html'

    def get_context_data(self, **kwargs):

        context = super(Feedback_his, self).get_context_data(**kwargs)
        id = self.request.GET['id']

        event = Councelling.objects.get(id=id)
        context['i'] = event
        return context

class student_profile_details(TemplateView):
    template_name = 'teacher/mentee.html'

    def get_context_data(self, **kwargs):
        context = super(student_profile_details, self).get_context_data(**kwargs)
        id = self.request.GET['id']

        event = student_profile.objects.filter(student_id=id)
        e = mentee_profile.objects.filter(student_id=id)
        context['i'] = event
        context['e'] = e

        return context

class AddCounselling_Date(TemplateView):
    template_name = 'teacher/add_date.html'

    def post(self, request, *args, **kwargs):
        me = Mentor_reg.objects.get(user_id=self.request.user.id)

        id = self.request.GET['id']
        date = request.POST['date']
        time = request.POST['time']
        place = request.POST['place']

        fe =Councelling()
        fe.mentor_id=me.id
        fe.student_id=id
        fe.date=date
        fe.time=time
        fe.place=place
        fe.feedback='not added'
        fe.save()
        return render(request, 'teacher/index.html', {'message': "Successfully Updated"})

class Coun_Booking(TemplateView):
    template_name = 'teacher/Counselling_booking.html'

    def get_context_data(self, **kwargs):
        f = Mentor_reg.objects.get(user_id=self.request.user.id)

        fe = Councelling.objects.filter(mentor_id=f.id)
        context = {
            'fe': fe
        }
        return context


class Feedback(TemplateView):
    template_name = 'teacher/feedback.html'

    def post(self, request, *args, **kwargs):

        id = self.request.GET['id']

        ta = request.POST['ts']
        cs = request.POST['cs']
        ist = request.POST['is']
        lq = request.POST['lq']
        team = request.POST['team']

        ca = request.POST['ca']
        ea = request.POST['ea']
        arts = request.POST['arts']
        sg = request.POST['sg']
        beha = request.POST['beha']
        wg = request.POST['wg']
        enter = request.POST['enter']
        si = request.POST['si']

        fe =Councelling.objects.get(id=id)
        fe.tech_skill=ta
        fe.comm_skill=cs
        fe.inter_skill=ist
        fe.leader_quality=lq
        fe.team_working=team
        fe.co_curricular=ca
        fe.Extra_curricular=ea
        fe.arts=arts
        fe.sports_games=sg
        fe.behaviour=beha
        fe.well_groomed_not=wg
        fe.enter_skill=enter
        fe.sugge_improve=si
        fe.save()
        return render(request, 'teacher/index.html', {'message': "Successfully Updated"})

class first_meeting(TemplateView):
    template_name = 'teacher/first_meeting.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        me = Mentor_reg.objects.get(user_id=self.request.user.id)
        id = self.request.GET['id']

        f = request.POST['f']
        s = request.POST['s']
        e = request.POST['e']
        p = request.POST['p']
        r = request.POST['r']

        a = request.POST['a']
        at = request.POST['at']
        so = request.POST['so']
        re = request.POST['re']
        beha = request.POST['beha']
        sk = request.POST['sk']
        we = request.POST['we']
        ad = request.POST['ad']
        add = request.POST['add']
        im = request.POST['im']
        sp = request.POST['sp']
        rl = request.POST['rl']
        mca = request.POST['mca']
        life = request.POST['life']
        core = request.POST['core']
        inter = request.POST['inter']
        if mentee_first_meeting.objects.filter(student_id=id):
            return render(request, 'teacher/index.html', {'message': "already done"})
        else:
            fe = mentee_first_meeting()
            fe.student_id = id
            fe.mentor = me
            fe.first_impression = f
            fe.sourceof_income = s
            fe.background = e
            fe.parental_harmony = p
            fe.relationship = r
            fe.atmosphere = a
            fe.morality = at
            fe.social_outlook = so
            fe.rd_habit = re
            fe.behaviour = beha
            fe.skills = sk
            fe.weakness = we
            fe.adjustment = ad
            fe.addiction = add
            fe.improvement = im
            fe.concern = sp
            fe.language_lab = rl
            fe.fitness_for_mca = mca
            fe.life_goals = life
            fe.competency = core
            fe.representations = inter
            fe.save()
            return render(request, 'teacher/index.html', {'message': "Successfully Updated"})


class Students(TemplateView):
    template_name = 'teacher/student_first.html'


    def get_context_data(self, **kwargs):

        context = super(Students,self).get_context_data(**kwargs)
        f = Mentor_reg.objects.get(user_id=self.request.user.id)
        view_pr = Assign.objects.filter(mentor_id=f.id)

        context['view_pr'] = view_pr
        return context


class Overall_ob(TemplateView):
    template_name = 'teacher/overall.html'
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        me = Mentor_reg.objects.get(user_id=self.request.user.id)
        id = self.request.GET['id']

        i = request.POST['i']
        a = request.POST['a']
        he=request.POST['he']
        e = request.POST['e']
        h = request.POST['h']

        p = request.POST['p']
        add = request.POST['add']
        if overall.objects.filter(student_id=id):
            return render(request, 'teacher/index.html', {'message': "already done"})
        else:
            fe = overall()
            fe.student_id = id
            fe.mentor = me
            fe.introvert_or_extrovert = i
            fe.abnormal_behaviour = a
            fe.health_condition = he
            fe.stability = e
            fe.hyperactive = h
            fe.personal_hygiene = p
            fe.addiction = add
            fe.save()
            return render(request, 'teacher/index.html', {'message': "Successfully added"})



class Add_assignment(TemplateView):
    template_name = 'teacher/assignemnt.html'
    def post(self, request, *args, **kwargs):
        id = self.request.GET['id']
        me = Mentor_reg.objects.get(user_id=self.request.user.id)
        desc = request.POST['desc']
        date = request.POST['date']

        fe = Assignment()
        fe.student_id = id
        fe.mentor = me
        fe.submission_date=date
        fe.assignment_description=desc
        fe.save()
        return render(request, 'teacher/index.html', {'message': "Successfully added"})



class view_assigment(TemplateView):
    template_name = 'teacher/view_assign.html'


    def get_context_data(self, **kwargs):

        context = super(view_assigment,self).get_context_data(**kwargs)
        f = Mentor_reg.objects.get(user_id=self.request.user.id)
        view_pr = Assignment.objects.filter(mentor_id=f.id)

        context['view_pr'] = view_pr
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        image = request.POST['feed']

        fe = Assignment.objects.get(id=id)
        fe.feedback = image
        fe.save()
        return render(request, 'teacher/index.html', {'message': "Successfully Updated"})




class First_impression_view(TemplateView):
    template_name = 'teacher/first.html'

    def get_context_data(self, **kwargs):
        context = super(First_impression_view, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        e = mentee_first_meeting.objects.get(student_id=id)
        context['e'] = e

        return context


class overall_view(TemplateView):
    template_name = 'teacher/over_all-view.html'

    def get_context_data(self, **kwargs):
        context = super(overall_view, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        e = overall.objects.get(student_id=id)
        context['e'] = e

        return context


class Generate(TemplateView):


    def dispatch(self, request, *args, **kwargs):
        worker = Mentor_reg.objects.get(user_id=self.request.user.id)
        id = self.request.GET['id']

        template_path = 'teacher/report1.html'
        jo =Councelling.objects.get(id=id)
        context={'i':jo}

        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response