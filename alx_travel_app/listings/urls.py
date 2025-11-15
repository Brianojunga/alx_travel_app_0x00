from django.urls import path
from .views import ListingAPIView

urlpatterns = [
    path('', ListingAPIView.as_view(), name='listings'),
]
