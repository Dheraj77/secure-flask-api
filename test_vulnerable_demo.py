from vulnerable_demo import app

def test_own_profile_allowed():
    client = app.test_client()
    response = client.get("/profile/101")
    assert response.status_code == 200

def test_other_profile_blocked():
    client = app.test_client()
    response = client.get("/profile/102")
    assert response.status_code == 403