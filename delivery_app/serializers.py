from rest_framework import serializers
from .models import Pricing



class PricingSerializer(serializers.ModelSerializer):
    total_distance = serializers.CharField()
    class Meta:
        model = Pricing
        fields = ['zone','total_distance','item_type']