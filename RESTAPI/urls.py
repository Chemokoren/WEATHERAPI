from django.urls import path, include

from RESTAPI.views import city_temperature,CityTemperature
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('locations/<slug:slug>/', CityTemperature.as_view() , name='locations-temp'),

    #jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

