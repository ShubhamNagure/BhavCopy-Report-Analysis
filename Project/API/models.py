from django.db import models

# Create your models here.

class BhavcopyRec(models.Model):
    sc_code = models.TextField(null=True)
    sc_name = models.TextField(null=True)
    sc_open = models.FloatField(null=True)
    sc_high = models.FloatField(null=True)
    sc_low = models.FloatField(null=True)
    sc_close = models.FloatField(null=True)
    sc_prevclose = models.FloatField(null=True)
    sc_no_of_trades=models.FloatField(null=True)
    sc_no_of_shares=models.FloatField(null=True)
    sc_net_turnover=models.FloatField(null=True)
    report_date=models.TextField(null=False)

    def __str__(self):
        return "{}-{}-{}".format(self.sc_name,self.sc_close,self.sc_no_of_trades)