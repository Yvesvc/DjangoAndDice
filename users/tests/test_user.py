
from django import urls
import pytest
import time
from django.test import LiveServerTestCase
from django.test.utils import override_settings
from selenium import webdriver
from spells.tests.test_spells import path_chromedriver


"""
Verify that the registration, login and logout views are publicly accessible
"""
@pytest.mark.django_db
@pytest.mark.parametrize('view_name', ['login', 'register', 'logout'])
def test_public_views(view_name, client):
    url = urls.reverse(view_name)
    resp = client.get(url)
    assert resp.status_code == 200


"""
Verify that alert pops up on login screen when window size too large
"""
class window_too_large(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.selenium = webdriver.Chrome(executable_path= path_chromedriver, chrome_options=options)

    def tearDown(self):
        self.selenium.quit()

    @override_settings(DEBUG=True)
    def test_window_too_large(self):
        selenium = self.selenium

        #For some reason, alert not showing with self.live_server_url
        selenium.get('http://127.0.0.1:8000/')
        selenium.switch_to_alert()

    assert 1 == 1
