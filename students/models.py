from django.db import models

# Create your models here.
class College(models.Model):
    college_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name +'--'+ self.location
    
    
    
#Employee Model
class Student(models.Model):
    student_number= models.IntegerField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    field_of_study=models.CharField(max_length=200)
    gpa=models.CharField(max_length=10)
    
    college=models.ForeignKey(College, on_delete=models.CASCADE)
    