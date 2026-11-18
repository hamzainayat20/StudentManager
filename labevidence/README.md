# Lab evidence

Screenshots and logs for CSC418 Lab Assignment 4, in hamzainayat20/StudentManager.

- 01_git_log_graph.png - git log graph, showing branches and merges
- 02_tests_successful.png - python -m unittest discover -s tests -v, 6 tests passed
- 03_tests_failed.png - the same test run with a deliberate failing test, local run, 1 failure
- 04_app_menu_demo.png - python main.py, add, empty title rejected, display, complete, delete
- 05_merge_conflict_before.png - PR #9 merge attempt failed with merge conflicts, README lines in conflict
- 06_merge_conflict_after.png - README.md on main after resolving the conflict, Project status: In Progress
- 07_merged_pull_requests.png - merged pull requests #5, #6, #7, #8, #9

The PNG screenshots are in this folder in the local delivery. The text logs below are the same outputs in text form, pushed here so they can be read on GitHub:

- git_log_graph.txt
- test_success.txt
- test_failure.txt
- app_demo.txt
- conflict_before.txt
- conflict_after.txt
- merged_prs.txt

Note: the GitHub Actions workflow file .github/workflows/tests.yml could not be added through the GitHub API (403, workflow files are blocked for this GitHub App). It needs to be added on the GitHub website, after which Actions will run the tests on push to main and on pull requests. The local test runs above show the same tests passing and failing.
