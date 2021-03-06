"""Testing module"""
from dataclasses import dataclass
from re import Pattern
from typing import Union

from app import APP
from fastapi.testclient import TestClient

CLIENT = TestClient(APP)


@dataclass
class AssertRequest:
    """
    API request assertion class
    Attributes:
        method (str): method of request
        url (str): url of request
        headers (Union[dict, None]): Headers of request
        payload (Union[dict, None]): Payload of request (for GET)
    """

    method: str
    url: str
    files: Union[bytes, None] = None
    headers: Union[dict, None] = None
    payload: Union[dict, None] = None


@dataclass
class AssertResponse:
    """
    API response assertion class
    Attributes:
        body (Union[dict, str]): The expected body of response
        status_code (int): The expected status code of response
    """

    body: Union[dict, str, Pattern]
    status_code: int


@dataclass
class APITestcase:
    """
    API testcase assertion class
    Attributes:
        name (str): Test case's name
        request (AssertRequest): Asserted Request
        response (AssertResponse): Asserted Response
    """

    name: str
    request: AssertRequest
    response: AssertResponse

    def run(self):
        if self.request.files:
            resp = CLIENT.request(
                self.request.method,
                self.request.url,
                headers=self.request.headers,
                params=None if self.request.method != "GET" else self.request.payload,
                data=None if self.request.method == "GET" else self.request.payload,
                files=self.request.files,
            )
        else:
            resp = CLIENT.request(
                self.request.method,
                self.request.url,
                headers=self.request.headers,
                params=None if self.request.method != "GET" else self.request.payload,
                json=None if self.request.method == "GET" else self.request.payload,
            )

        if isinstance(self.response.body, str):
            assert (
                resp.text == self.response.body
            ), f"{resp.text} does not match {self.response.body}"
        elif isinstance(self.response.body, Pattern):
            assert self.response.body.match(
                resp.text
            ), f"{resp.text} does not match {self.response.body}"
        else:
            assert (
                resp.json() == self.response.body
            ), f"{resp.json} does not match {self.response.body}"
        assert (
            resp.status_code == self.response.status_code
        ), f"{resp.status_code} does not match {self.response.status_code}"
