from django.db import models

class CourseModel(models.Model):
    cno=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=30)
    cfees=models.FloatField()
    def __str__(self):
        return self.cname+" / "+str(self.cfees)

class StudentModel(models.Model):
    rno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
