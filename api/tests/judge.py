import pytest
from tests import APITestcase, AssertRequest, AssertResponse

ROUTE = "/judge"


with open("api/tests/data.zip", "rb") as file:
    CASES = [
        APITestcase(
            "success",
            AssertRequest(
                "POST",
                ROUTE,
                headers={},
                payload={"uid": "F74094716", "pid": 1, "token": "12345"},
                files={
                    "file": (
                        "data.zip",
                        file.read(),
                        "application/zip",
                    )
                },
            ),
            AssertResponse("OK", 200),
        ),
        APITestcase(
            "fail",
            AssertRequest(
                "POST",
                ROUTE,
                headers={},
                payload={"uid": "F74094716", "pid": 1, "token": "12345"},
                files={"file": ("data.zip", file.read())},
            ),
            AssertResponse("Invalid file type", 400),
        ),
        APITestcase(
            "fail",
            AssertRequest(
                "POST",
                ROUTE,
                headers={},
                payload={"uid": "F74094716", "pid": 1, "token": "54321"},
                files={"file": ("data.zip", file.read())},
            ),
            AssertResponse("Unauthorized", 401),
        ),
    ]


@pytest.mark.parametrize("case", CASES, ids=[case.name for case in CASES])
def test(case: APITestcase):
    case.run()
