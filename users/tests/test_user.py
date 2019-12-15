
from django import urls
import pytest

"""
Verify that the registration, login and logout views are publicly accessible
"""
@pytest.mark.django_db
@pytest.mark.parametrize('view_name', ['login', 'register', 'logout'])
def test_public_views(view_name, client):
    url = urls.reverse(view_name)
    resp = client.get(url)
    assert resp.status_code == 200