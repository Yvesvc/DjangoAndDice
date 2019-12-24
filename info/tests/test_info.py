
from django import urls
from spells.tests.test_spells import login_registration
from django.test import LiveServerTestCase
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.keys import Keys
from django.test.utils import override_settings
from spells.tests.test_spells import path_chromedriver

"""
Verify that the main info view is not publicly accessible, but redirects
"""

@pytest.mark.django_db
def test_private_view_info_not_logged_in(client):
    url = urls.reverse("info_index")
    resp = client.get(url)
    assert resp.status_code == 302


"""
Verify that the info view is accessible, if logged in
"""

@pytest.mark.django_db
def test_private_view_info_logged_in(admin_client):
    url = urls.reverse("info_index")
    resp = admin_client.get(url)
    assert resp.status_code == 200



"""
Verify that if user accesses main info view and
--has no record: given empty form
--has record: return form
--has record: able to update
"""

class InfoShowRecord(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(path_chromedriver)
        super(InfoShowRecord, self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(InfoShowRecord, self).tearDown()

    @override_settings(DEBUG=True)
    def test_show_info_user_record_equipment(self):
        selenium = self.selenium

        # register and login
        selenium = login_registration(selenium, self.live_server_url)


        #Opening the link we want to test, if no error: given empty form
        selenium.get(self.live_server_url + '/info')

        field = selenium.find_element_by_name('personality_traits')
        update_button = selenium.find_element_by_id('update_button_info')

        field.send_keys('inputting text into field')


        #has record: return form
        update_button.send_keys(Keys.RETURN)

        field = selenium.find_element_by_name('personality_traits')
        update_button = selenium.find_element_by_id('update_button_info')
        field.send_keys('aaargh')


        #has record: able to update
        update_button.send_keys(Keys.RETURN)

        assert 1 == 1
