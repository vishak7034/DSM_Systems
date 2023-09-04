from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)


class Student_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)


class Mentor_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone=models.CharField(max_length=200, null=True)
    college_id=models.CharField(max_length=200, null=True)

    qualification=models.CharField(max_length=200, null=True)



class Assign(models.Model):
    mentor = models.ForeignKey(Mentor_reg, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)

class student_profile(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    rollnumber=models.CharField(max_length=200, null=True)
    dob=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200, null=True)
    blood_group=models.CharField(max_length=200, null=True)
    religion=models.CharField(max_length=200, null=True)
    caste=models.CharField(max_length=200, null=True)
    permanent_address=models.CharField(max_length=200, null=True)
    contact_address=models.CharField(max_length=200, null=True)
    mob_number=models.CharField(max_length=200, null=True)
    telephone_number=models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/', null=True)

class Councelling(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    mentor = models.ForeignKey(Mentor_reg, on_delete=models.CASCADE, null=True)
    date=models.DateField(max_length=200, null=True)
    time=models.TimeField(max_length=200, null=True)
    place=models.CharField(max_length=200, null=True)
    tech_skill=models.CharField(max_length=200, null=True)
    comm_skill=models.CharField(max_length=200, null=True)
    inter_skill=models.CharField(max_length=200, null=True)
    leader_quality=models.CharField(max_length=200, null=True)
    team_working=models.CharField(max_length=200, null=True)
    co_curricular=models.CharField(max_length=200, null=True)
    Extra_curricular=models.CharField(max_length=200, null=True)

    arts=models.CharField(max_length=200, null=True)
    sports_games=models.CharField(max_length=200, null=True)
    behaviour=models.CharField(max_length=200, null=True)
    well_groomed_not=models.CharField(max_length=200, null=True)
    enter_skill=models.CharField(max_length=200, null=True)
    sugge_improve=models.CharField(max_length=200, null=True)

class mentee_profile(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    father_name=models.CharField(max_length=200, null=True)
    father_profession=models.CharField(max_length=200, null=True)
    father_age=models.CharField(max_length=200, null=True)
    work_place=models.CharField(max_length=200, null=True)
    father_number=models.CharField(max_length=200, null=True)
    mother_name=models.CharField(max_length=200, null=True)
    mother_profession=models.CharField(max_length=200, null=True)
    mother_number=models.CharField(max_length=200, null=True)
    siblings_in_SJCET=models.CharField(max_length=200, null=True)
    position=models.CharField(max_length=200, null=True)
    local_guardian=models.CharField(max_length=200, null=True)
    local_age=models.CharField(max_length=200, null=True)
    guardian_proffe=models.CharField(max_length=200, null=True)
    guardian_address=models.CharField(max_length=200, null=True)
    guardian_number=models.CharField(max_length=200, null=True)

class mentee_details(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    hostel_or_not=models.CharField(max_length=200, null=True)
    visiting_home=models.CharField(max_length=200, null=True)
    stay_details=models.CharField(max_length=200, null=True)
    conveyance=models.CharField(max_length=200, null=True)
    entrance_rank=models.CharField(max_length=200, null=True)
    experience=models.CharField(max_length=200, null=True)
    extra_curricular=models.CharField(max_length=200, null=True)
    language=models.CharField(max_length=200, null=True)
    achievements=models.CharField(max_length=200, null=True)
    personal_goal=models.CharField(max_length=200, null=True)
    professional_goal=models.CharField(max_length=200, null=True)
    social_goal=models.CharField(max_length=200, null=True)
    strength=models.CharField(max_length=200, null=True)
    weakness=models.CharField(max_length=200, null=True)
    opportunity=models.CharField(max_length=200, null=True)
    threats=models.CharField(max_length=200, null=True)
    hobbies=models.CharField(max_length=200, null=True)
    role_model=models.CharField(max_length=200, null=True)


class mentee_first_meeting(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    mentor = models.ForeignKey(Mentor_reg, on_delete=models.CASCADE, null=True)

    first_impression=models.CharField(max_length=200, null=True)
    sourceof_income=models.CharField(max_length=200, null=True)
    background=models.CharField(max_length=200, null=True)
    parental_harmony=models.CharField(max_length=200, null=True)
    relationship=models.CharField(max_length=200, null=True)
    atmosphere=models.CharField(max_length=200, null=True)
    morality=models.CharField(max_length=200, null=True)
    social_outlook=models.CharField(max_length=200, null=True)
    rd_habit=models.CharField(max_length=200, null=True)
    behaviour=models.CharField(max_length=200, null=True)
    skills=models.CharField(max_length=200, null=True)
    weakness=models.CharField(max_length=200, null=True)
    adjustment=models.CharField(max_length=200, null=True)
    addiction=models.CharField(max_length=200, null=True)
    improvement=models.CharField(max_length=200, null=True)
    concern=models.CharField(max_length=200, null=True)
    language_lab=models.CharField(max_length=200, null=True)
    fitness_for_mca=models.CharField(max_length=200, null=True)
    life_goals=models.CharField(max_length=200, null=True)
    competency=models.CharField(max_length=200, null=True)
    representations=models.CharField(max_length=200, null=True)

class Assignment(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    mentor = models.ForeignKey(Mentor_reg, on_delete=models.CASCADE, null=True)
    assignment_description=models.CharField(max_length=200, null=True)
    submission_date=models.CharField(max_length=200, null=True)
    feedback=models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/', null=True)


class Accomodation(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    stay_duration_from=models.DateField(max_length=200, null=True)
    stay_duration_to=models.DateField(max_length=200, null=True)
    reason=models.CharField(max_length=200, null=True)
    stay_arranged=models.CharField(max_length=200, null=True)
    no_hostel_owner=models.CharField(max_length=200, null=True)

class Qualification(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    quali=models.CharField(max_length=200, null=True)
    college=models.CharField(max_length=200, null=True)
    university=models.CharField(max_length=200, null=True)
    mark=models.CharField(max_length=200, null=True)
    medium=models.CharField(max_length=200, null=True)

class overall(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE, null=True)
    mentor = models.ForeignKey(Mentor_reg, on_delete=models.CASCADE, null=True)
    introvert_or_extrovert=models.CharField(max_length=200, null=True)
    abnormal_behaviour=models.CharField(max_length=200, null=True)
    health_condition=models.CharField(max_length=200, null=True)
    stability=models.CharField(max_length=200, null=True)
    hyperactive=models.CharField(max_length=200, null=True)
    personal_hygiene=models.CharField(max_length=200, null=True)
    addiction=models.CharField(max_length=200, null=True)