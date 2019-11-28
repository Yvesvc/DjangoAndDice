
from django.urls import resolve
from sheet.views import index

class Test_URL():

    # URL '/' -> views.index
    def test_url_home(self):
        found = resolve('/')
        assert found.func == index

