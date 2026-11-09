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
  - 3 tools excluded, Input ["Knife", "Pizza cutter", "Scissors"] — Returned HTTP 500 with an empty response body (Defect 1). This input was moved to test_excluding_all_tools_is_refused and marked as xfail.

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

## Part B
1. Real-server tests can find problems between components, such as the load balancer and login, and actual server errors, such as the HTTP 500 error in Step 0.16. Unit tests with stubs are still useful because they run faster and help identify which function has a problem.

2. Public-token ratings are shared, while creating a new user keeps each test's data separate. In Project 2, each test can create its own user and test data, then clean them up afterward.

3. A session keeps the AWSALB cookie between requests, helping requests stay on the same server. My three runs of Step 0.12 were: failed, passed, then failed. This shows that requests without a session can be unreliable or flaky.

4. The block "all 3 tools excluded". A 500 error with an empty body gives the application no useful message to show the user, while a 400 response can explain what went wrong. The test stays as xfail to keep the defect visible until it is fixed.

5. Base choice coverage needs 9 tests: 1 + 2 + 3 + 1 + 2 = 9. All combinations coverage needs 72 tests: 3 × 4 × 2 × 3 = 72.

6. In my Step A4 tests, GET 404, PUT 400 และ DELETE 400. I expect a consistent not-found response, such as 404, for all three operations. The different status codes are an inconsistency, but the tests confirmed that the owner's rating remained unchanged.

7. The API returned a list of ratings even though the token was fake. This is a security defect because a stranger could access rating data without logging in.

8. My API tests check HTTP status codes, response bodies, and error messages directly. They also run without opening a browser. However, only web page tests can check the actual user interface and what users see on the screen.