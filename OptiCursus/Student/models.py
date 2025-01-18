from django.db import models
from django.urls import reverse

# Create your models here.

#USER PROFILE INPUT

class Student(models.Model): 
    ## Preference
    Domains = models.TextField(blank=False, null=True) #Subjects the student enjoys or excels in (e.g., mathematics, literature, biology).
    CareerGoals = models.TextField(blank=False, null=True) #Desired career paths or industries (e.g., software engineering, medicine, finance). 
    Level = models.CharField(max_length=20) #Bachelor, Master, PhD
    ## Profile
    CV = models.FileField(blank=False) #Academic/Industry Background (CV or Resume): Certifications, Skills (Hard and Soft), Experience, Achievements, Projects, Extracurricular Activities, Awards, Linguistic Skills   
    Portfolio = models.URLField(blank=True,null=True)
    MotivationLetter = models.FileField(blank=True, null=True)
    LinkedIn = models.URLField(blank=True,null=True)
    EduLevel = models.CharField(max_length=20) # Bachelor, Master, PhD, Courses taken
    GPA = models.FloatField() #Grades
    Constraints = models.TextField(blank=False, null=True) #Limitations such as budget, time, or accessibility. 
