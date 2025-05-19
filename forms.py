from django import forms
from .models import CourseModel,StudentModel

class CourseForm(forms.ModelForm):
    class Meta:
        model=CourseModel
        fields="__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields="__all__"