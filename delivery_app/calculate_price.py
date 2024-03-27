
from .models import Pricing,Item
from rest_framework.response import Response
from rest_framework import status





def calculate_total_price(pricing,total_distance):
    try:
        # print(pricing)
        print(pricing.base_distance_in_km)
        # print(total_distance)
        t_distance=int(total_distance)
        print(t_distance)
        print(pricing.item.item_type)
        i_type=pricing.item.item_type
        b_distance_in_km=pricing.base_distance_in_km
        if t_distance>=b_distance_in_km:
            if i_type=='perishable':
                return int(pricing.fixed_price)+(t_distance-b_distance_in_km)*1.5
            if i_type=='non_perishable':
                return int(pricing.fixed_price)+(t_distance-b_distance_in_km)*1
        else:
            return int(pricing.fixed_price)

    except Pricing.DoesNotExist:
        return Response({"error": "Pricing not found, Please enter valid parameters"}, status=404)
