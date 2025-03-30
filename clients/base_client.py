from typing import Any

import allure
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles

from clients.event_hooks import log_request_event_hook, log_response_event_hook
from config import HTTPClientConfig


class BaseClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        return self.client.patch(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        return self.client.delete(url)


def get_http_client(config: HTTPClientConfig) -> Client:
    return Client(
        timeout=config.timeout,
        base_url=config.client_url,
        event_hooks={
            "request": [log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )
