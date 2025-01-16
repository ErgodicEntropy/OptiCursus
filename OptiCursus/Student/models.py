from django.db import models
from pydantic import BaseModel, Field
from typing import Optional, List, Union


# Create your models here.

#USER PROFILE INPUT

class Student(models.Model): 
    ## Preference
    name = models.CharField(max_length=20)
    university = models.CharField(max_length=20)
    domain = models.CharField(max_length=20)
    type = models.CharField(max_length=20)     
    ## Profile
    GPA = models.FloatField(max_length=20)
    Certifications = models.CharField(max_length=20)
    Skills = models.CharField(max_length=20)
    Experience = models.TextField(blank=False, null=True)
    
    
    

#     def Preference():
#         pass
#     def Eligibility(profile, cursus): #text -> LLM
#         pass

