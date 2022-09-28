from django.test import SimpleTestCase
from django.urls import reverse, resolve

from RESTAPI.views import CityTemperature


class ApiUrlsTests(SimpleTestCase):

    ''' test for api/locations/{city} '''
    def test_list_url_is_resolved(self):
        url = reverse('locations-temp', args=['city'])
        self.assertEquals(resolve(url).func.view_class,CityTemperature)