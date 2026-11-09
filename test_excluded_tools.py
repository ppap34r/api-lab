import pytest


# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize(
    "excluded",
    [[], ["Knife"], ["Scissors"], ["Knife", "Scissors"], ],
)
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

# Excluding every tool should be refused with a 400 error.
@pytest.mark.xfail(
    reason="Defect 1: API returns HTTP 500 with an empty body when all tools are excluded.",
    strict=True,
)
def test_excluding_all_tools_is_refused(api, auth):
    excluded = ["Knife", "Pizza cutter", "Scissors"]
    body = {"excludedTools": excluded}

    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 400
    assert "error" in res.json()
