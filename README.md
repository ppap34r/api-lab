# api-lab

API tests for QuickPizza (https://quickpizza.grafana.com), written with pytest and requests for the ITCS386 API lab.

## Install and run

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

To save the output of a full run as an HTML report:

```bash
pytest -v --html=report.html --self-contained-html
```

Every test that changes data logs in a new user of its own (fixtures in `conftest.py`), so the tests are independent and can run alone or in any order.

## Part A — Input Space Partitioning

## Input domain model for POST /api/ratings

| Characteristic | Blocks | Values in the tests |
|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short |

## Input domain model for POST /api/ratings

| Characteristic | Blocks | Values in the tests | Covering test |
|---|---|---|---|
| C1 Value of stars | below 1 | 0 | `test_stars_out_of_range[0]` |
| C1 Value of stars | 1 to 5 (base) | 3 | `test_base_choice_is_saved` |
| C1 Value of stars | above 5 | 6 | `test_stars_out_of_range[6]` |
| C2 Type of stars | whole number (base) | 3 | `test_base_choice_is_saved` |
| C2 Type of stars | decimal | 3.5 | `test_stars_decimal_is_refused` |
| C2 Type of stars | text | "3" | `test_stars_text_is_refused` |
| C2 Type of stars | missing | no field | `test_stars_missing_is_refused` |
| C3 Pizza | exists (base) | a new pizza | `test_base_choice_is_saved` |
| C3 Pizza | does not exist | 999999999 | `test_nonexistent_pizza_is_refused` |
| C4 Token | user's own (base) | from auth | `test_base_choice_is_saved` |
| C4 Token | none | no header | `test_rating_without_token_is_refused` |
| C4 Token | wrong length | token short | `test_rating_with_short_token_is_refused` |