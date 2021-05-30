from django.db import models
from user.models import User
#Create your models here.

# class CourseTable(models.Model):
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
    #NID = models.ForeignKey(NID, on_delete=models.CASCADE)

    #def __str__(self):
   #     return NID.NIDuser
class NID(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    NIDuser = models.CharField(max_length=128)
    NIDpassword = models.CharField(max_length=128)
    #CourseTable = models.ForeignKey(CourseTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.NIDuser

    class Meta:
        ordering = ['NIDuser']


class Course(models.Model):
    NID = models.ForeignKey(NID, on_delete=models.CASCADE)
    #CourseTable = models.ForeignKey(CourseTable,on_delete=models.CASCADE)
    #teacher = models.CharField(max_length=128)

    CourseName = models.CharField(max_length=128)
    #CourseCode = models.IntegerField()
    week = models.IntegerField()
    section = models.IntegerField()

    def __str__(self):
        return self.CourseName

    class Meta:
        ordering = ['section', 'week']

