from django.db import models

class ClickCounter(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField(default="2000-01-01")
    time = models.TimeField(default="00:00:00")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.count)