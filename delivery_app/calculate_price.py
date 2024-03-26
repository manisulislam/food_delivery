
from .models import Pricing
from rest_framework.response import Response


def calculate_total_price(zone, total_distance,item_type):
    try:
        pricing = Pricing.objects.get(
            zone=zone, 
            item_type=item_type,
            )
        
        t_distance=int(total_distance)
        b_distance_in_km=int(pricing.base_distance_in_km)
        if t_distance>=b_distance_in_km:
            if item_type=='perishable':
                return int(pricing.fixed_price)+(t_distance-b_distance_in_km)*1.5
            if item_type=='non_perishable':
                return int(pricing.fixed_price)+(t_distance-b_distance_in_km)*1
        else:
            return int(pricing.fixed_price)

    except Pricing.DoesNotExist:
        return Response({"error": "Pricing not found, Please enter valid parameters"}, status=404)
