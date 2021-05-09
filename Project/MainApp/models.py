from django.db import models

# Create your models here.

class BhavcopyRec(models.Model):
    sc_code = models.TextField()
    sc_name = models.TextField()
    sc_open = models.FloatField()
    sc_high = models.FloatField()
    sc_low = models.FloatField()
    sc_close = models.FloatField()

    def __str__(self):
        return self.sc_name