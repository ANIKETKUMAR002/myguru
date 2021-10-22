from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student_management(models.Model):
    name = models.CharField(max_length=50,default=None, blank=False)
    mobile = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=15, default=None, blank=False)
    state = models.CharField(max_length=50,default=None, blank=False)
    city = models.CharField(max_length=50,default=None, blank=False)
    profile_pic = models.ImageField(upload_to='profile_pic/Student/', null=True, blank=True)
    Add_password = models.CharField(max_length=15,default=None, blank=False)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.name

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class Aptitude_category_management(models.Model):
    category_name = models.CharField(max_length=50)


    def __str__(self):
        return self.category_name

class Aptitude_test_management(models.Model):
    aptitude_test_name = models.CharField(max_length=50, default=None)
    aptitude_test_Duration = models.DateTimeField(auto_now=True)
    test_amount = models.IntegerField(default=None)
    total_questions= models.CharField(max_length=50, default=None)



    def __str__(self):
        return self.aptitude_test_name

class Question(models.Model):
    category=models.ForeignKey(Aptitude_test_management,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student_management,on_delete=models.CASCADE)
    exam = models.ForeignKey(Aptitude_category_management,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
