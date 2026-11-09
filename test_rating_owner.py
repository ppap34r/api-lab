
def assert_unchanged(api, auth, rating):
    """The owner reads the rating back and finds it as it was."""
    res = api.get(f"/api/ratings/{rating['id']}", headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot read the rating of the owner.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    res = api.get(f"/api/ratings/{rating['id']}", headers=other_auth)
    print("READ status:", res.status_code)
    assert 400 <= res.status_code <= 499
    assert_unchanged(api, auth, rating)


# Another user cannot change the rating of the owner.
def test_other_user_cannot_update(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 1}, headers=other_auth)
    print("UPDATE status:", res.status_code)
    assert 400 <= res.status_code <= 499
    assert_unchanged(api, auth, rating)


# Another user cannot delete the rating of the owner.
def test_other_user_cannot_delete(api, auth, other_auth, rating):
    res = api.delete(f"/api/ratings/{rating['id']}", headers=other_auth)
    print("DELETE status:", res.status_code)
    assert 400 <= res.status_code <= 499
    assert_unchanged(api, auth, rating)
