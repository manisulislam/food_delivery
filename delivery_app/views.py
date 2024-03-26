from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import PricingSerializer
from .calculate_price import calculate_total_price

# Create your views here.
class PricingView(generics.GenericAPIView):
    def post(self, request):
        serializer = PricingSerializer(data=request.data)
        if serializer.is_valid():
            zone=serializer.validated_data.get('zone')
            total_distance=serializer.validated_data.get('total_distance')
            item_type=serializer.validated_data.get('item_type')
            total_price=calculate_total_price(zone,total_distance,item_type)
            return Response({'total_price':total_price}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        