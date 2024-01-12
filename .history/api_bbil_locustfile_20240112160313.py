"""
Load test for API.BBIL.ORG
BASE_API_URL = https://api.bbil.org
"""
from locust import HttpUser, task, between, events


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print(f"A new test is starting. env: {environment}")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print(f"A new test is ending. env: {environment}")


class APIUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        headers = {
            'Content-Type': 'application/json',
            'Country-Code': 'QkQ%3D',
            'Accept-Language': 'bn'
        }
        self.client.headers = headers

    @task
    def page_api(self):
        """ page api """
        self.client.get("/api/v1/configurations")

