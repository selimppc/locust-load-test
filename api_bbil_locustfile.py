"""
LOAD TEST SAMPLE
"""
from locust import HttpUser, task, between, events

# Set your base URL here
BASE_API_URL = ""

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print(f"A new test is starting. env: {environment}")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print(f"A new test is ending. env: {environment}")


class APIUser(HttpUser):
    host = BASE_API_URL
    wait_time = between(1, 5)

    def on_start(self):
        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://localhost.bbil.org/',
        }
        self.client.headers = headers

    @task
    def configuration_api(self):
        """ categories api """
        self.client.get("/product-categories")
        
