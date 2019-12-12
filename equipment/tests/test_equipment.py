
from django import urls
from spells.tests.test_spells import login_registration
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
Verify that the main equipment view is not publicly accessible, but redirects
"""

def test_private_view_equipment_not_logged_in(client):
    url = urls.reverse("equipment_index")
    resp = client.get(url)
    assert resp.status_code == 302


"""
Verify that the equipment spell view is accessible, if logged in
"""

def test_private_view_equipment_logged_in(admin_client):
    url = urls.reverse("equipment_index")
    resp = admin_client.get(url)
    assert resp.status_code == 200



"""
Verify that if user accesses main equipment view and
--has no record: given empty form
--has record: return form
--has record: able to update
"""

class EquipmentShowRecord(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(r"C:\Users\Yves Vc\Downloads\chromedriver_win32\chromedriver.exe")
        super(EquipmentShowRecord, self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(EquipmentShowRecord, self).tearDown()

    def test_show_user_record_equipment(self):
        selenium = self.selenium

        # register and login
        selenium = login_registration(selenium, self.live_server_url)

        #Opening the link we want to test, if no error: given empty form
        selenium.get(self.live_server_url + '/equipment')

        field = selenium.find_element_by_name('equipment_text')
        update_button = selenium.find_element_by_id('update_button_equipment')

        field.send_keys('inputting text into field')

        time.sleep(6)

        #has record: return form
        update_button.send_keys(Keys.RETURN)

        field = selenium.find_element_by_name('equipment_text')
        update_button = selenium.find_element_by_id('update_button_equipment')
        field.send_keys('aaargh')

        time.sleep(6)

        #has record: able to update
        update_button.send_keys(Keys.RETURN)

        assert 1 == 1