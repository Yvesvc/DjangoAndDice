
from django import urls

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
