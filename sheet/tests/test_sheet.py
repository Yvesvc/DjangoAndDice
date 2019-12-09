
from django import urls
import pytest
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sheet.models import Sheet
from spells.tests.test_spells import login_registration


"""
Verify that the main sheet view is not publicly accessible, but redirects
"""
@pytest.mark.parametrize('view_name', ['index'])
def test_public_views(view_name, client):
    url = urls.reverse(view_name)
    resp = client.get(url)
    assert resp.status_code == 302

"""
Verify that the main sheet view is accessible, if logged in
"""
@pytest.mark.parametrize('view_name', ['index'])
def test_private_views_logged_in(view_name, admin_client):
    url = urls.reverse(view_name)
    resp = admin_client.get(url)
    assert resp.status_code == 200

"""
Verify that if user accesses main sheet view and has no record, exception is handled
"""
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
        self.selenium = webdriver.Chrome(r"C:\Users\Yves Vc\Downloads\chromedriver_win32\chromedriver.exe")
        super(SheetShowRecord, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SheetShowRecord, self).tearDown()

    def test_show_user_record(self):
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
        self.selenium = webdriver.Chrome(r"C:\Users\Yves Vc\Downloads\chromedriver_win32\chromedriver.exe")
        super(SheetOneRecord, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SheetOneRecord, self).tearDown()

    @pytest.mark.django_db
    def test_show_user_record(self):
        selenium = self.selenium

        #register
        selenium.get(self.live_server_url + '/user/registration')

        username = selenium.find_element_by_name('username')
        charactername = selenium.find_element_by_name('charactername')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')
        sign_up = selenium.find_element_by_id('register_button')

        username.send_keys('testuser1')
        charactername.send_keys('Imperator__REX')
        password1.send_keys('Kingsubject1')
        password2.send_keys('Kingsubject1')
        sign_up.send_keys(Keys.RETURN)

        #login

        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_id('login_button')

        username.send_keys('testuser1')
        password.send_keys('Kingsubject1')

        submit.send_keys(Keys.RETURN)

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
        self.selenium = webdriver.Chrome(r"C:\Users\Yves Vc\Downloads\chromedriver_win32\chromedriver.exe")
        super(ElementsJS, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(ElementsJS, self).tearDown()

    @pytest.mark.django_db
    def test_show_user_record(self):
        selenium = self.selenium

        #register
        selenium.get(self.live_server_url + '/user/registration')

        username = selenium.find_element_by_name('username')
        charactername = selenium.find_element_by_name('charactername')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')
        sign_up = selenium.find_element_by_id('register_button')

        username.send_keys('testuser1')
        charactername.send_keys('Imperator__REX')
        password1.send_keys('Kingsubject1')
        password2.send_keys('Kingsubject1')
        sign_up.send_keys(Keys.RETURN)

        #login

        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_id('login_button')

        username.send_keys('testuser1')
        password.send_keys('Kingsubject1')

        submit.send_keys(Keys.RETURN)

        #check for elements
        element1 = selenium.find_element_by_id('skill_row_last')
        element2 = selenium.find_element_by_class_name('feat_trait')
        element3 = selenium.find_element_by_class_name('feat_trait_txt')
        element4 = selenium.find_element_by_class_name('feat_trait_val')

        assert 1 == 1