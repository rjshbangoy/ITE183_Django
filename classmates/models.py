from django.db import models

# Create your models here.

class Classmate(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=6, default="", choices=[("male", "Male"), ("female", "Female")])

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})


