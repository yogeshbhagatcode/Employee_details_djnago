from django.db import models

class EmployeeDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='images')
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name
