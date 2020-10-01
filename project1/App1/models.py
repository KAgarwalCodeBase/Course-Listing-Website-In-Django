from django.db import models
class Allcourses(models.Model):
    #creating column name in table or defining class variable
    coursename = models.CharField(max_length = 200)
    insname = models.CharField(max_length = 100)
    def __str__(self):
        return self.coursename
class details(models.Model):
    #when we deleted any course from Allcourses class then it automatically deleted its details from details class
    couse = models.ForeignKey(Allcourses,on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)
    def __str__(self):
        return self.sp
