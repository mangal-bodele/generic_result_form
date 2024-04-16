from django.db import models

class Result(models.Model):
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    standard = models.CharField(max_length=30)
    date = models.DateField()
    roll = models.IntegerField()
    math = models.IntegerField()
    english = models.IntegerField()
    hindi = models.IntegerField()
    marathi = models.IntegerField()
    obtained = models.IntegerField()
    total = models.IntegerField()
    percentage = models.CharField(max_length=20)


    def __str__(self):
        return self.name
