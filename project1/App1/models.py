from django.db import models
import datetime
from django.utils import timezone
class Allcourses(models.Model):
    #creating column name in table or defining class variable
    coursename = models.CharField(max_length = 200)
    insname = models.CharField(max_length = 100)
    startedfrom = models.DateTimeField('Started From')
    def __str__(self):
        return self.coursename
    def was_published_recently(self):
        return self.startedfrom >= timezone.now() -  datetime.timedelta(days=1)

class details(models.Model):
    #when we deleted any course from Allcourses class then it automatically deleted its details from details class
    couse = models.ForeignKey(Allcourses,on_delete=models.CASCADE)
    ct = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ct)

