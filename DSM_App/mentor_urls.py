
from django.urls import path

from DSM_App.mentor_views import Indexview, Student_under, History, AddCounselling_Date, Coun_Booking, Feedback, \
    Feedback_his, Students, first_meeting, Overall_ob, student_profile, student_profile_details, Add_assignment, \
    view_assigment, First_impression_view, overall_view, Generate

urlpatterns = [

    path('',Indexview.as_view()),
    path('Student_under',Student_under.as_view()),
    path('History',History.as_view()),
    path('date',AddCounselling_Date.as_view()),
    path('Booking',Coun_Booking.as_view()),
    path('Feedback',Feedback.as_view()),
    path('Feedback_his',Feedback_his.as_view()),
    path('Students',Students.as_view()),
    path('first_meeting',first_meeting.as_view()),
    path('Overall',Overall_ob.as_view()),
    path('student_profile',student_profile_details.as_view()),
    path('Add_assignment',Add_assignment.as_view()),
    path('view_assigment',view_assigment.as_view()),
    path('first',First_impression_view.as_view()),
    path('overall_view',overall_view.as_view()),
    path('Generate',Generate.as_view())



]


def urls():
    return urlpatterns, 'mentor','mentor'