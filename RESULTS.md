# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Cute Margherita
- Step 0.12, results of the three runs without a session (optional): FAILED, PASSED, FAILED
- Step 0.16, blocks of "how many of the three tools are excluded":
  - 0 tools excluded, input [] - PASSED
  - 1 tool excluded, Inputs ["Knife"] and ["Scissors"] — PASSED. The original test covered only this block.
  - 2 tools excluded, Input ["Knife", "Scissors"] — PASSED
  - 3 tools excluded, Input ["Knife", "Pizza cutter", "Scissors"] — Returned HTTP 500 with an empty response body (Defect 1). This input was moved to test_all_tools_excluded_is_refused and marked as xfail.

## Defect report
- Title: Excluding all three tools returns 500 instead of 400
- Request: POST /api/pizza with a logged-in user's token and the following JSON body:
{
  "excludedTools": ["Knife", "Pizza cutter", "Scissors"]
}
- Expected result: HTTP 400 with a JSON error message because no pizza can be made when all available tools are excluded.
- Actual result: HTTP 500 Internal Server Error with an empty response body.
- Severity: Medium. No data is lost, but the application returns a server error for a normal customer choice and provides no error message to display to the user.

## Part A
- Step A4, Status Codes When Another User Accesses a Rating
status codes when the other user reads, changes and deletes:
  - read (GET): 404, body - PASSED
  - change (PUT): 400, body - PASSED
  - delete (DELETE): 400, body - PASSED