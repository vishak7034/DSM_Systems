
from django.urls import path

from DSM_App.student_views import Indexview, Student_Profile, Coun_noti, History, profile_update, more_details, \
    Accomodation, Accomodation_Details, Qualification_details, view_feedback, assi_feed

urlpatterns = [

    path('',Indexview.as_view()),
    path('Student_Profile',Student_Profile.as_view()),
    path('Coun_noti',Coun_noti.as_view()),
    path('History',History.as_view()),
    path('profile_update',profile_update.as_view()),
    path('more_details',more_details.as_view()),
    path('Accomodation',Accomodation_Details.as_view()),
    path('Qualification',Qualification_details.as_view()),
    path('view_feedback',view_feedback.as_view()),
    path('assi_feed',assi_feed.as_view())


]


def urls():
    return urlpatterns, 'student','student'