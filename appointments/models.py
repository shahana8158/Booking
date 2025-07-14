from django.db import models
from django.contrib.auth.models import User

# Create your models here.


GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
    ('U','Unknown/Prefer Not to Say')
]

DOCTORS_CHOICES=[
    ('Dr . Anna Joseph','Dr . Anna Joseph'),
    ('Dr . Mahadhev','Dr . Mahadhev'),
    ('Dr . Supritha','Dr . Supritha'),
    ('Dr . Mruthula','Dr . Mruthula'),
    ('Dr . Shihab','Dr . Shihab'),
    ('Dr . Rajesh','Dr . Rajesh'),
    ('Dr . Jamsheer','Dr . Jamsheer'),
    ('Dr . Kumar','Dr . Kumar'),
    ('Dr . Meenakshi','Dr . Meenakshi'),
    ('Dr . Kavi','Dr . Kavi'),
    ('Dr . Baburaj','Dr . Baburaj'),
    ('Dr . Lakshmi','Dr . Lakshmi'),
    ('Dr . Maya','Dr . Maya'),
    ('Dr . Favas','Dr . Favas'),
    ('Dr . Rishad','Dr . Rishad'),
    ('Dr . Biju Lal','Dr . Biju Lal'),
    ('Dr . kishor kumar','Dr . kishor kumar'),
    ('Dr . Jose Antony','Dr . Jose Antony'),
    ('Dr . Sunaina','Dr . Sunaina'),
    ('Dr . Subash','Dr . Subash'),
    ('Dr . Kiran','Dr . Kiran'),
    ('Dr . Ramadas','Dr . Ramadas'),
    ('Dr . Kavitha','Dr . Kavitha'),
    ('Dr . Ravi kumar','Dr . Ravi kumar'),
    ('Dr . Anupama','Dr . Anupama'),
    ('Dr . Riya subash','Dr . Riya subash'),
    ('Dr . Jayapal Jose','Dr . Jayapal Jose'),
    ('Dr . Gogul','Dr . Gogul'),
    ('Dr . veena','Dr . veena'),
    ('Dr . Rahul Sharma','Dr . Rahul Sharma')
]
TIME_PERIOD_CHOICES = [
        ('AM', 'AM'),
        ('PM', 'PM'),
    ]


class services(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField (max_length=3000)
    image=models.ImageField(upload_to='products')
   
    def __str__(self):
        return self.title
    
class staff(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField (max_length=3000,default=1)

    def __str__(self):
        return self.title
    

class category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class doctors(models.Model):
    name = models.CharField(max_length=30)
    details = models.TextField()
    image=models.ImageField(upload_to='products')
    ctry= models.ForeignKey(category,on_delete=models.CASCADE)
    us= models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_name =models.CharField (max_length=30,null=True,blank=True)
    first_name =models.CharField (max_length=30,null=True,blank=True)
    last_name =models.CharField (max_length=30,null=True,blank=True)
    Email = models.EmailField (max_length=30,null=True,blank=True)
    phone = models.IntegerField ()
    image = models.ImageField(upload_to='profilepic')

    def __str__(self):
        return str(self.user)
    

class booking(models.Model):
    Doctorname= models.CharField (max_length=100,choices=DOCTORS_CHOICES,null=True,blank=True)
    Patientname= models.CharField (max_length=60)
    Gender=models.CharField(max_length=6,choices=GENDER_CHOICES,null=True,blank=True)
    Age = models.IntegerField()
    Phone = models.IntegerField()
    Email=models.EmailField(max_length=30)
    Place=models.CharField(max_length=30)
    Date=models.DateField(null=True,blank=True)
    Time=models.TimeField(null=True,blank=True)  
    us=models.ForeignKey(User,on_delete=models.CASCADE,default=1) 
    

    def __str__(self):
        return str(self.us)

    