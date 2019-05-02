from django.db import models

class OurUser(models.Model):
    first_name = models.CharField("Name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    def __str__(self):
        return self.last_name + " " + self.first_name
