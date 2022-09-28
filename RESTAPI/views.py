from django.http import JsonResponse
from statistics import median

from rest_framework import generics, permissions

from RESTAPI.utils import WeatherAPI


class CityTemperature(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        city_name = self.kwargs['slug']
        num_days = request.query_params['number_of_days']
        temperature_results = city_temperature(city_name, num_days)
        return JsonResponse(temperature_results)

'''
this method interfaces with the WeatherAPI  and returns temperature for the specified city 
for the duration given by num_days
'''
def city_temperature(city, num_days):
    weather_data = WeatherAPI().fetch_weather_data(city, num_days)
    new_info = weather_data['forecast']['forecastday']
    all_data = []
    sum_average_data = 0
    max_val = -float("inf")
    min_val = float("inf")
    count = 0
    for new_data in new_info:
        date_today = new_data['date']
        max_temp_c = new_data['day']['maxtemp_c']
        min_temp_c = new_data['day']['mintemp_c']
        avg_temp_c = new_data['day']['avgtemp_c']
        if max_temp_c > max_val:
            max_val = max_temp_c

        if min_temp_c < min_val:
            min_val = min_temp_c

        count += 1
        sum_average_data += avg_temp_c
        all_data.append(max_temp_c)
        all_data.append(min_temp_c)

    median_temp = median(all_data)
    average_temp = sum_average_data / count

    final_data = {
        "maximum": max_val,
        "minimum": min_val,
        "average": average_temp,
        "median": median_temp,
    }

    return final_data
