from django.urls import path
from .views import PricingView



urlpatterns=[
    path('pricing/', PricingView.as_view(), name='pricing'),
]