"""
Load test for API.BBIL.ORG
BASE_API_URL = https://api.bbil.org
"""
from locust import HttpUser, task, between, events

# Set your base URL here
BASE_API_URL = "https://api.ashiquehassan.com"

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
        """ configuration api """
        self.client.get("/api/v1/configurations")
        
    # @task
    # def homepage_api(self):
    #     """ configuration api """
    #     self.client.get("/api/v1/home")

