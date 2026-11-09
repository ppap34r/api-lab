import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"
DECIMAL_ERROR = (
    "json: cannot unmarshal number 3.5 into Go struct field "
    "Rating.stars of type int"
)
TEXT_ERROR = (
    "json: cannot unmarshal string into Go struct field "
    "Rating.stars of type int"
)


# Base choice: 3 stars as a whole number, an existing pizza, and the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id


# C1: A number of stars below 1 or above 5 is refused.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}


# C2: Decimal values are refused.
def test_stars_decimal_is_refused(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3.5}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": DECIMAL_ERROR}


# C2: Text values are refused.
def test_stars_text_is_refused(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": "3"}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": TEXT_ERROR}


# C2: A request without the stars field is refused.
def test_stars_missing_is_refused(api, auth, pizza_id):
    new = {"pizza_id": pizza_id}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}


# C3: A rating for a pizza that does not exist is refused.
def test_nonexistent_pizza_is_refused(api, auth):
    new = {"pizza_id": 999999999, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": "pizza ID 999999999 not found"}


# C4: A request without an Authorization header is refused.
def test_rating_without_token_is_refused(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# C4: A request with a wrong-length token is refused.
def test_rating_with_short_token_is_refused(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    short_auth = {"Authorization": "token short"}
    res = api.post("/api/ratings", json=new, headers=short_auth)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}