# myapp/models.py

from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)  # Adding last_name if needed
    password=models.CharField(max_length=6000)
    e_mail=models.EmailField(max_length=5000,null=False)

    def __str__(self):
        return self.first_name
