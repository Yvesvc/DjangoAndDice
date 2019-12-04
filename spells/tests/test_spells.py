
from django import urls
import pytest
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from spells.models import Spells5E

"""
Verify that the main spell view is not publicly accessible, but redirects
"""
@pytest.mark.parametrize('view_name', ['index'])
def test_public_views(view_name, client):
    url = urls.reverse(view_name)
    resp = client.get(url)
    assert resp.status_code == 302

"""
Verify that the main spell view is accessible, if logged in
"""
@pytest.mark.parametrize('view_name', ['index'])
def test_private_views_logged_in(view_name, admin_client):
    url = urls.reverse(view_name)
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
        self.selenium = webdriver.Chrome(r"C:\Users\Yves Vc\Downloads\chromedriver_win32\chromedriver.exe")
        super(SpellShowRecord, self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(SpellShowRecord, self).tearDown()

    def test_show_user_record(self):
        selenium = self.selenium

        # register
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

        # login
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_id('login_button')

        username.send_keys('testuser1')
        password.send_keys('Kingsubject1')

        submit.send_keys(Keys.RETURN)

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
        self.selenium = webdriver.Chrome(r"C:\Users\Yves Vc\Downloads\chromedriver_win32\chromedriver.exe")
        super(add_spell_ajax, self).setUp()
        Spells5E.objects.create(name='Aid', level = '2')

    def tearDown(self):
        self.selenium.quit()
        super(add_spell_ajax, self).tearDown()

    @pytest.mark.django_db
    def test_add_spell_ajax(self):
        selenium = self.selenium

        # register
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

        # login
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_id('login_button')

        username.send_keys('testuser1')
        password.send_keys('Kingsubject1')

        submit.send_keys(Keys.RETURN)

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
        self.selenium = webdriver.Chrome(r"C:\Users\Yves Vc\Downloads\chromedriver_win32\chromedriver.exe")
        super(delete_spell_ajax, self).setUp()
        Spells5E.objects.create(name='Aid', level = '2')

    def tearDown(self):
        self.selenium.quit()
        super(delete_spell_ajax, self).tearDown()

    @pytest.mark.django_db
    def test_delete_spell_ajax(self):
        selenium = self.selenium

        # register
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

        # login
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_id('login_button')

        username.send_keys('testuser1')
        password.send_keys('Kingsubject1')

        submit.send_keys(Keys.RETURN)

        selenium.get(self.live_server_url + '/spells')

        selected_spell = selenium.find_element_by_id('id_name')
        add_spell_button = selenium.find_element_by_name('btnSpells5Eform')


        #Add Spell 'Aid'
        for option in selected_spell.find_elements_by_tag_name("option"):
            if option.text == 'Aid':
                option.click()
                add_spell_button.click()
                break

        selenium.refresh()
        time.sleep(6)

        #add another spell in model and also ajax add it

        #refresh url

        #delete spell

        #check that only the chosen spell is deleted



        assert 1 == 2
