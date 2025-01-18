from django.db import models

# Create your models here.

class Cursus(models.Model):
    Title = models.CharField(max_length=20)
    University = models.CharField(max_length=20) 
    Quality = models.CharField(max_length=20, blank=True) #Quality of the cursus program which depends on: University and Cursus
    Tuition = models.IntegerField(blank=True) #Tuition fee
    Domain = models.CharField(max_length=20,blank=True) # Mathematics, Physics, CS...etc
    Level = models.CharField(max_length=20,blank=True) # Bachelor, Master (Professional, Research), PhD
    Requirements = models.TextField(blank=False) # Cursus demands or requirements
    PreferenceScore = models.FloatField() #Alignment score of the user preference (e.g. a dot product)
    EligibilityScore = models.FloatField() #Alignment score (level of risk) of the user eligibility to the program (e.g. a probability value) -> Eligibility = User Profile * Cursus Requirements


    def __repr__(self):
        return f'<Cursus {self.id}>'  % self.id

    