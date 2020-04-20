from django.db import models

# Create your models here.
class Demo(models.Model):

    student_name=models.CharField(max_length=15)
    student_address=models.CharField(max_length=20)
    student_hobbies=models.CharField(max_length=15)
