from django.db import models

# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    emp_id = models.IntegerField()
    def __str__(self):
        return self.firstname