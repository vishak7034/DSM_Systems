
from django.urls import path

from DSM_App import admin_views
from DSM_App.admin_views import adminIndex, Mentor_regstration, view_Mentor, Assign_Mentor, view_student, \
    Delete_Student, Assigned_mentor, update_mentor, Delete_assiged

urlpatterns = [

    path('',adminIndex.as_view()),
    path('Mentor_reg',Mentor_regstration.as_view()),
    path('view_Mentor',view_Mentor.as_view()),
    path('Assign',Assign_Mentor.as_view()),
    path('view_student',view_student.as_view()),
    path('delete', Delete_Student.as_view()),
    path('Assigned_mentor',Assigned_mentor.as_view()),
    path('update_mentor',update_mentor.as_view()),
    path('Delete_assiged',Delete_assiged.as_view())
    # path('delete/<int:id>', admin_views.delete_student, name='delete-student'),

]


def urls():
    return urlpatterns, 'admin','admin'