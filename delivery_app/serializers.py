from rest_framework import serializers
from .models import Pricing



class DeliverCostSerializer(serializers.Serializer):
    zone=serializers.CharField()
    organization_name=serializers.CharField()
    total_distance = serializers.CharField()
    item_type=serializers.CharField()
   