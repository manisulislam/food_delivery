from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import DeliverCostSerializer
from .calculate_price import calculate_total_price
from .models import Organization,Item,Pricing

# Create your views here.
class PricingView(generics.GenericAPIView):
    def post(self, request):
        serializer = DeliverCostSerializer(data=request.data)
        if serializer.is_valid():
            zone=serializer.validated_data.get('zone')
            organization_name=serializer.validated_data.get('organization_name')
            total_distance=serializer.validated_data.get('total_distance')
            item_type=serializer.validated_data.get('item_type')

            organization=Organization.objects.create(name=organization_name)
            item=Item.objects.create(item_type=item_type)
            pricing=Pricing.objects.create(organization=organization, item=item,zone=zone)

            total_price=calculate_total_price(pricing,total_distance)

            return Response({'total_price':total_price}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        