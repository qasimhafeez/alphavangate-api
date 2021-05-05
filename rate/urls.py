from django.urls import path
from .views import GetRate


urlpatterns = [
    path('api/v1/rate/', GetRate.as_view(), name='get_rate'),
    ]