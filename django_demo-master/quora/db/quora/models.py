from django.db import models

class Result(models.Model):
    marks = models.IntegerField()
    percentage = models.FloatField(max_length=4)

class Department(models.Model):
    name = models.CharField(max_length=124)
    code = models.CharField(max_length=10)

class User(models.Model):
    username = models.CharField(unique=True ,max_length=124, null=False)
    password = models.CharField(max_length=124)
    mobile_number = models.DecimalField(max_digits=10, decimal_places=0)
#    dept = models.ForeignKey(Department, null=True)