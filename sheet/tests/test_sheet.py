
from django import urls
import pytest
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sheet.models import Sheet
from django.test.utils import override_settings
from spells.tests.test_spells import login_registration
from spells.tests.test_spells import path_chromedriver


"""
Verify that the main sheet view is not publicly accessible, but redirects
"""

@pytest.mark.django_db
@pytest.mark.parametrize('view_name', ['index'])
def test_private_view_sheet_not_logged_in(view_name, client):
    url = urls.reverse(view_name)
    resp = client.get(url)
    assert resp.status_code == 302

"""
Verify that the main sheet view is accessible, if logged in
"""

@pytest.mark.django_db
@pytest.mark.parametrize('view_name', ['index'])
def test_private_view_sheet_logged_in(view_name, admin_client):
    url = urls.reverse(view_name)
    resp = admin_client.get(url)
    assert resp.status_code == 200

"""
Verify that if user accesses main sheet view and has no record, exception is handled
"""

@pytest.mark.django_db
@pytest.mark.parametrize('view_name', ['index'])
def test_main_no_expection_logged_in(view_name,client, django_user_model):
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = urls.reverse(view_name)
    response = client.get(url)
    assert response.status_code == 200

"""
Verify that if user accesses main sheet view and has a record, record is returned
"""

class SheetShowRecord(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(path_chromedriver)
        super(SheetShowRecord, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SheetShowRecord, self).tearDown()

    @override_settings(DEBUG=True)
    def test_show_sheet_user_record(self):
        selenium = self.selenium

        # register and login
        selenium = login_registration(selenium, self.live_server_url)

        #check the returned result
        assert 'Imperator__REX' in selenium.page_source



"""
Verify that if user accesses main sheet view and 
--has no record: given empty form
--has record: able to update
"""
class SheetOneRecord(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(path_chromedriver)
        super(SheetOneRecord, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SheetOneRecord, self).tearDown()

    @override_settings(DEBUG=True)
    def test_show_update_sheet_user_record(self):
        selenium = self.selenium

        # register and login
        selenium = login_registration(selenium, self.live_server_url)

        #create form
        field = selenium.find_element_by_id('id_atk_spell_name_1')
        update_button = selenium.find_element_by_id('update_button')
        field.clear()
        field.send_keys('test1')

        update_button.click()

        #update form

        field = selenium.find_element_by_id('id_atk_spell_name_1')
        update_button = selenium.find_element_by_id('update_button')
        field.clear()
        field.send_keys('test2')

        update_button.click()

        assert 1 == 1

"""
Verify necessary elemets are present in HTML for sheet.JS to function 
"""
class ElementsJS(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(path_chromedriver)
        super(ElementsJS, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(ElementsJS, self).tearDown()

    @override_settings(DEBUG=True)
    def test_element_JS_present(self):
        selenium = self.selenium

        # register and login
        selenium = login_registration(selenium, self.live_server_url)

        #check for elements
        element1 = selenium.find_element_by_id('skill_row_last')
        element2 = selenium.find_element_by_class_name('feat_trait')
        element3 = selenium.find_element_by_class_name('feat_trait_txt')
        element4 = selenium.find_element_by_class_name('feat_trait_val')

        assert 1 == 1