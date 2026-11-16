from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name