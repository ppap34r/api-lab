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