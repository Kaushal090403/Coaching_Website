from django.shortcuts import render
from .forms import CourseForm,StudentForm
from .models import CourseModel,StudentModel

def home(request):
    return render(request,"home.html")

def showcourses(request):
    data=CourseModel.objects.all()
    return render(request, "showcourses.html", {"data":data})

def addcourses(request):
    if request.method=="POST":
        data=CourseForm(request.POST)
        if data.is_valid():
            data.save()
            fm=CourseForm()
            return render(request,"addcourses.html",{"fm":fm,"msg":"Course added"})
        else:
            return render(request, "addcourses.html", {"fm":data,"msg":"Check Issue"})
    else:
        fm=CourseForm()
        return render(request, "addcourses.html",{"fm":fm})
def deletecourses(request):
    pass

def showstudent(request):
    data=StudentModel.objects.all()
    return render(request,"showstudent.html",{"data":data})

def addstudent(request):
    if request.method == "POST":
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
            fm = StudentForm()
            return render(request, "addstudent.html", {"fm": fm, "msg": "Student added"})
        else:
            return render(request, "addstudent.html", {"fm": data, "msg": "Check Issue"})
    else:
        fm = StudentForm()
        return render(request, "addstudent.html", {"fm": fm})


def deletestudent(request):
    pass

# Create your views here.
