from rest_framework import serializers

from .models import BhavcopyRec

class BhavcopyRecSerializer(serializers.Serializer):

    sc_code = serializers.CharField(null=True)
    sc_name = serializers.CharField(null=True)
    sc_open = serializers.FloatField(null=True)
    sc_high = serializers.FloatField(null=True)
    sc_low = serializers.FloatField(null=True)
    sc_close = serializers.FloatField(null=True)
    sc_prevclose = serializers.FloatField(null=True)
    sc_no_of_trades=serializers.FloatField(null=True)
    sc_no_of_shares=serializers.FloatField(null=True)
    sc_net_turnover=serializers.FloatField(null=True)
    report_date=serializers.CharField(null=False)