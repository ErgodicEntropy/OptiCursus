from django.db import models

# Create your models here.

class Cursus(models.Model):
    name = models.CharField(max_length=20)
    university = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    tuition = models.IntegerField()
    livingcost = models.IntegerField()
    domain = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    
    def __repr__(self):
        return f'<Cursus {self.id}>'  % self.id

