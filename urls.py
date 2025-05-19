
from django.contrib import admin
from django.urls import path
from ksapp.views import home,showcourses,addcourses,deletecourses,showstudent,addstudent,deletestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("showcourses/",showcourses,name="showcourses"),
    path("addcourses/",addcourses,name="addcourses"),
    path("deletecourses/<int:id>",deletecourses,name="deletecourses"),
    path("showstudent/",showstudent,name="showstudent"),
    path("addstudent/",addstudent,name="addstudent"),
    path("deletestudent/<int:id>",deletestudent,name="deletestudent"),

]
