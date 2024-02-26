from django.db import models


# Create your models here.

class ToDo(models.Model):
    do = models.CharField(max_length=200)
    prio = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.do
