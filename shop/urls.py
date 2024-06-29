from django.urls import path
from .views import (KlassCreateAPIView, KlassUpdateDeleteAPIView, MehmonxonaCreateAPIView,
                     MehmonxonaUpdateDeleteAPIView, TravelCreateAPIView, TravelUpdateDeleteAPIView)

app_name = 'shop'

urlpatterns = [
    path('api/v1/klass/', KlassCreateAPIView.as_view(), name='klass'),
    path('api/v1/mehmonxona/', MehmonxonaCreateAPIView.as_view(), name='mehmonxona'),
    path('api/v1/travel/', TravelCreateAPIView.as_view(), name='travel'),

    path('api/v1/klass/<int:pk>/', KlassUpdateDeleteAPIView.as_view(), name='klass'),
    path('api/v1/mehmonxona/<int:pk>/', MehmonxonaUpdateDeleteAPIView.as_view(), name='mehmonxona'),
    path('api/v1/travel/<int:pk>/', TravelUpdateDeleteAPIView.as_view(), name='travel'),

]