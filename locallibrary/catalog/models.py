from django.db import models

class ClickCounter(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)

    def __str__(self):
        return f"Click Count: {self.count}"
