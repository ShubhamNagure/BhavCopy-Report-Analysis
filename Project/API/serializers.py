from django.db import models
from django.db.models import fields
from django.db.models.fields import Field
from rest_framework import serializers

from MainApp.models import BhavcopyRec

class BhavcopyRecSerializer(serializers.ModelSerializer):
    class Meta:
        model=BhavcopyRec
        fields=['sc_code','sc_name','sc_open','sc_high','sc_low','sc_close','sc_prevclose','sc_no_of_trades','sc_no_of_shares','sc_net_turnover','report_date']





    