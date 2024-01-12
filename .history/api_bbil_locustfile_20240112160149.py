"""
Load test for API.BBIL.ORG
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
            'Authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlMjJjM2FiYS04ZjUyLTQ1M2MtYTBiYy1iNTUwMGY5MDAwMWYiLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUl9CSU9TQ09QRSIsIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6Ijg4MDE5ODgxNTA2NDEiLCJjbGllbnRfbG9naW5faWQiOiI3Yzc2NzE4Zi1jMzJlLTRjZmEtODYyYi02M2Y0ZWM3ZmY5MWEiLCJ1c2VyX3R5cGUiOiJyZWd1bGFyIiwicGxhdGZvcm1faWQiOiJhYmZlYTQ2Mi1mNjRkLTQ5MWUtOWNkOS03NWVlMDAxZjQ1YjAiLCJjbGllbnRfaWQiOm51bGwsImJvbmdvX2lkIjoiY1R2WjdiVGNLaWUiLCJpYXQiOjE2NTA5MDc3MDUsImV4cCI6MTY1ODY4MzcxNS4wfQ.eEgZ92hzBYB47KwZ2U656CMhoqxGBiV6UFn4yDDVnpQB8RXhIxvefwGnuufvKAUk_8_w7Ja7eZTBhyIB2v1wYDSpJuKT5SebkQzjWYTN-2JblBP2BY49gIOLTWIvBMb8Wn07r9zGDOx6_3opSYHvjLWPPxnF7ZqJW_M2flzbUbyViLf9eV-wFFaBl3jdH6LGNSqDm8UmtfLOrkl1CoZINIDVNNWS_IldbD6ThG1fpj7TntOd-5AfDz-EaKgJ9HmqCAEk35Wshb-mkU-fszOIiomHWNBsxDvHVsTDh9nUhe9-20IvMRAHJjr1UEhi0W_SJeZwzwYDC1c5GBrJJiBCXQOMEruYuY-If7FallZ1xe0Cm_cLtjzcBPkCGvgUCEuoJUgYrgLCusLzKSDWhcumD4DupAHfzXc7IHM9KrnIuRBvLPdDuSoUk2K4HMimLO2voo1u44I6Ahf9gSIc65Azcp7IfAg_wRdYvL1E70YEtsRa6veSnhhNG45nqdMhQ5rUcChq9LCSiucTDm34HscfI0NdpE6cYDzgvSuT02HMPgPrXcfnj9tjBKCTDvPidVJOkTrNwx8LTfql_3ESFGN4LjGYXBUWhiCXkg57wE7oQStzV8ckbiY86liuTxFvjvKsAUuuA5sCOk9EiHf85aLyQU-1_NYqNd9DPyFrxF6FONk', # noqa
            'Country-Code': 'QkQ%3D',
            'Accept-Language': 'bn'
        }
        self.client.headers = headers

    @task
    def page_api(self):
        """ page api """
        self.client.get("/api/v1/page/home")

