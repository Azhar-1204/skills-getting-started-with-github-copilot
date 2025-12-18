def test_get_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    # Should contain at least a few known activities
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_signup_and_unregister(client):
    activity = "Chess Club"
    email = "test_student@example.com"

    # ensure not already present
    resp = client.get(f"/activities")
    assert resp.status_code == 200
    assert email not in resp.json()[activity]["participants"]

    # sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert resp.json()["message"].startswith("Signed up")

    # verify added
    resp = client.get(f"/activities")
    assert email in resp.json()[activity]["participants"]

    # unregister
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert resp.status_code == 200
    assert resp.json()["message"].startswith("Unregistered")

    # verify removed
    resp = client.get(f"/activities")
    assert email not in resp.json()[activity]["participants"]
