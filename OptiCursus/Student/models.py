from django.db import models
from pydantic import BaseModel, Field
from typing import Optional, List, Union


# Create your models here.

#USER PROFILE INPUT

class Student(models.Model): 
    ## Preference
    #Subjects the student enjoys or excels in (e.g., mathematics, literature, biology).
    favorite_subject = models.TextField(blank=False, null=True)
    #Desired career paths or industries (e.g., software engineering, medicine, finance). 
    career_goals = models.TextField(blank=False, null=True)
    #Limitations such as budget, time, or accessibility. 
    constraints = models.TextField(blank=False, null=True) 
    ## Profile
    GPA = models.FloatField()

    Certifications = models.CharField(max_length=20)
    Skills = models.CharField(max_length=20) #Technical or soft skills (e.g., programming, public speaking, teamwork).
    Experience = models.TextField(blank=False, null=True)
    Academic_Background = 0 #Grades, courses taken, standardized test scores, prerequisite courses, certifications, projects, and academic achievements (CV, Resume, Potrfolio).
    Achievements = 0    #Awards, certifications, or extracurricular activities.
    
