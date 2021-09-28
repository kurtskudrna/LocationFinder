from django.db import models

# Create your models here.


class Location(models.Model):
    place = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place
