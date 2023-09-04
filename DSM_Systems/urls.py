"""DSM_Systems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from DSM_App import admin_urls, student_urls, mentor_urls
from DSM_App.views import Index, Student_Reg, loginview

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',Index.as_view()),
    path('admin/', admin_urls.urls()),
    path('student/', student_urls.urls()),
    path('mentor/',mentor_urls.urls()),

    path('Student_Reg',Student_Reg.as_view()),
    path('login',loginview.as_view())

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)