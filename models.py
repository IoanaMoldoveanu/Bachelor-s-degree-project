
from django.contrib.auth.models import User
from django.db import models



class appointments(models.Model):
    nume = models.CharField(max_length=45)
    prenume= models.CharField(max_length=45)
    data_preferinta= models.CharField(max_length=45)
    ora_preferinta= models.CharField(max_length=45)
    favStylist =models.CharField(max_length=45)
    favStylistName= models.CharField(max_length=45)
    telefon = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    selected_services = models.CharField(max_length=150) 

    class Meta:
        db_table = 'accounts_appointments'

    def __str__(self):
        return f"{self.nume} {self.prenume}"

