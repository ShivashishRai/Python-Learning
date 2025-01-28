

#Report hooks

import pytest

@pytest.hookimpl
def pytest_report_teststatus(report):
    if report.when == "call":
        if report.outcome == "failed":
            return "FAIL", "F", "FAILED"
        elif report.outcome == "passed":
            return "PASS", "P", "PASSED"

def test_something():
    assert 1 + 7 == 2