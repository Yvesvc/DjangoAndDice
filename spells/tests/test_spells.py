
from django import urls
import pytest
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.test.utils import override_settings
from spells.models import Spells5E
from selenium.common.exceptions import NoSuchElementException

#Path to Chrome Webdriver
path_chromedriver = r"C:\Users\Yves Vc\Downloads\chromedriver_win32\79\chromedriver.exe"


#login and registration
def login_registration(selenium, server_url):

    # register
    selenium.get(server_url + '/user/registration')

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

    # login
    username = selenium.find_element_by_name('username')
    password = selenium.find_element_by_name('password')
    submit = selenium.find_element_by_id('login_button')

    username.send_keys('testuser1')
    password.send_keys('Kingsubject1')

    submit.send_keys(Keys.RETURN)


    return selenium


"""
Verify that the main spell view is not publicly accessible, but redirects
"""

@pytest.mark.django_db
def test_private_view_spells_not_logged_in(client):
    url = urls.reverse("spells_index")
    resp = client.get(url)
    assert resp.status_code == 302

"""
Verify that the main spells view is accessible, if logged in
"""

@pytest.mark.django_db
def test_private_view_equipment_logged_in(admin_client):
    url = urls.reverse("spells_index")
    resp = admin_client.get(url)
    assert resp.status_code == 200



"""
Verify that if user accesses main spell view and
--has no record: given empty form
--has record: return form
--has record: able to update
"""

class SpellShowRecord(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(path_chromedriver)
        super(SpellShowRecord, self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(SpellShowRecord, self).tearDown()

    @override_settings(DEBUG=True)
    def test_show_spells_user_record(self):
        selenium = self.selenium

        # register and login
        selenium = login_registration(selenium, self.live_server_url)

        #Opening the link we want to test, if no error: given empty form
        selenium.get(self.live_server_url + '/spells')

        field = selenium.find_element_by_name('lvl1_total')
        update_button = selenium.find_element_by_id('btnmetadataform')

        field.send_keys('5')

        #has record: return form
        update_button.send_keys(Keys.RETURN)

        field = selenium.find_element_by_name('lvl9_total')
        update_button = selenium.find_element_by_id('btnmetadataform')
        field.send_keys('4')

        #has record: able to update
        update_button.send_keys(Keys.RETURN)

        assert 1 == 1


"""
Verify add Spell AJAX (spells.js): Spell added immediately
"""
class add_spell_ajax(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(path_chromedriver)
        super(add_spell_ajax, self).setUp()
        Spells5E.objects.create(name='Aid', level = '2')

    def tearDown(self):
        self.selenium.quit()
        super(add_spell_ajax, self).tearDown()

    @override_settings(DEBUG=True)
    def test_add_spell_ajax(self):
        selenium = self.selenium

        #register and login
        selenium = login_registration(selenium, self.live_server_url)

        selenium.get(self.live_server_url + '/spells')

        selected_spell = selenium.find_element_by_id('id_name')
        add_spell_button = selenium.find_element_by_name('btnSpells5Eform')


        #Add Spell 'Aid' and check if added to my spell list
        for option in selected_spell.find_elements_by_tag_name("option"):
            if option.text == 'Aid':
                option.click()
                add_spell_button.click()
                added_spell = selenium.find_element_by_class_name('my_spells_spell')
                add_spell_value = added_spell.text
                break
        assert 'Aid' == add_spell_value


"""
Verify delete Spell AJAX (spells.js): Spell deleted immediately
"""
class delete_spell_ajax(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(path_chromedriver)
        super(delete_spell_ajax, self).setUp()
        Spells5E.objects.create(name='Aid', level = '2')
        Spells5E.objects.create(name='Absorb Elements', level='1')
        Spells5E.objects.create(name='Animal Friendship', level='1')

    def tearDown(self):
        self.selenium.quit()
        super(delete_spell_ajax, self).tearDown()

    @override_settings(DEBUG=True)
    def test_delete_spell_ajax(self):
        selenium = self.selenium

        # register and login
        selenium = login_registration(selenium, self.live_server_url)

        selenium.get(self.live_server_url + '/spells')

        selected_spell = selenium.find_element_by_id('id_name')
        add_spell_button = selenium.find_element_by_name('btnSpells5Eform')


        #Add Spells 'Aid', 'Absorb Elements' and 'Animal Friendship'
        for option in selected_spell.find_elements_by_tag_name("option"):
            if option.text == 'Aid' or option.text == 'Absorb Elements' or option.text == 'Animal Friendship':
                option.click()
                add_spell_button.click()


        selenium.refresh()

        #Delete spell Animal Friendship
        delete_animal_friendship = selenium.find_element_by_xpath("/html/body/div[@class='container']/div[@class='my_spells']/div[@id='my_spells_lvl1']/div[@class='my_spells_spell'][2]/div[@class='my_spells_spell_del my_spells_spell_row']/i[@class='fa fa-minus-circle']")
        delete_animal_friendship.click()
        alert_window = selenium.switch_to_alert()
        alert_window.accept()

        selenium.refresh()

        #If other spells deleted, selenium will throw error and test fails
        absorb_elements = selenium.find_element_by_xpath("/html/body/div[@class='container']/div[@class='my_spells']/div[@id='my_spells_lvl1']/div[@class='my_spells_spell'][1]/div[@class='my_spells_spell_name my_spells_spell_row']")
        aid = selenium.find_element_by_xpath("/html/body/div[@class='container']/div[@class='my_spells']/div[@id='my_spells_lvl2']/div[@class='my_spells_spell']")

        #if spell Animal Friendsip found, assert error
        try:
            animal_friendship = selenium.find_element_by_xpath("/html/body/div[@class='container']/div[@class='my_spells']/div[@id='my_spells_lvl1']/div[@class='my_spells_spell'][2]/div[@class='my_spells_spell_name my_spells_spell_row']")
            assert 2 == 1

        # if spell Animal Friendsip not found, assert correct
        except NoSuchElementException:
            assert 1 == 1



