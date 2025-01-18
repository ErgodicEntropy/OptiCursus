from django.db import models
from django.urls import reverse

# Create your models here.

#USER PROFILE INPUT

class Student(models.Model): 
    ## Preference
    Domain = models.TextField(blank=False, null=True) #Subjects the student enjoys or excels in (e.g., mathematics, literature, biology).
    CareerGoals = models.TextField(blank=False, null=True) #Desired career paths or industries (e.g., software engineering, medicine, finance). 
    Level = models.CharField(max_length=20) #Bachelor, Master, PhD
    ## Profile
    CV = models.FileField(blank=False) #Academic/Industry Background (CV or Resume): Certifications, Skills (Hard and Soft), Experience, Achievements, Projects, Extracurricular Activities, Awards, Linguistic Skills   
