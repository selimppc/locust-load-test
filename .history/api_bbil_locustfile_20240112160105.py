"""
Load test for API.BBIL.ORG
"""
from locust import HttpUser, task, between, events

client_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiNTM0NDg5Mi1lNWM3LTQ2ODUtOWM4NS1lNTFjNzY3MzM4YzYiLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUl9CSU9TQ09QRSIsIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6Ijg4MDE4MzE4MDMyNTUiLCJjbGllbnRfbG9naW5faWQiOiI2ZDI5YWI1MC1kNmJmLTQ5MWItYTMwYS0xZmZkZmQ0ZTQzODIiLCJ1c2VyX3R5cGUiOiJyZWd1bGFyIiwicGxhdGZvcm1faWQiOiJhYmZlYTQ2Mi1mNjRkLTQ5MWUtOWNkOS03NWVlMDAxZjQ1YjAiLCJjbGllbnRfaWQiOm51bGwsImJvbmdvX2lkIjoiN1MzNFRxS1pFSEwiLCJpYXQiOjE2NTAyMzMyMDUsImV4cCI6MTY1ODAwOTIxNS4wfQ.s_qOSTqqsS-zAYyE6QYFNudw61PhGdC0h5VbhqYTAggD29ms6dogFOBE6UScQqXLOVZKuaCeqsSkVsVtRP7VPrpErKG9C6xE_jdvEsE2wPifXkbOwi8q1TYlfE2llm1wLnkZT89GdrLC5jRdWHi47MKaYN55wGZD88W1j7P0AWdRpIGghE9MPguB74wu8E8D0flgwJ-j5xSRMIaK79e8Oxt4NLkCsLAbebMWYoBD7OkvqpsqXZG9pKhxEVBl_dM4tms_HjoInmLnjVPpQo7mhZvgRW_DywzYB6Y4GX6QFB_GDmwVwjJvPGHLZ5aH3nmqk5Y33QNH6AhbUG2Hy2_u_5ylMdl18wIYzsJVKo9IBw8hCqfmBvyjMyFjMhgeSqIl_6y2ysb2g_7JLznxs8MY_VGNlH6oRM95v0HT1J0-6fPVTmr0GDVZuf3p9MaQ0HijZZhhUXpQWd62Q1-E18MfZWi8glbDGKmT-cU7SqsSRi7E4peosDdcQ4cEEOugPyGsl7BALQ3sp7Hccoga15r3xD3IPPvMU4h4nJKz3gaH1i3ziEUfIDJhSmETJzZxB7piTZkSRQabaRKVZja6elXueXsTk2vp66cP0CGly044vca_ZUJ8UBT1yoea_2OG79vybqkK7OUWHsUwu78Ri01h_nGbRwU1kGmZvaxXgqxDsII"  # noqa
internal_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJBTlRNQU4iLCJpYXQiOjE2NTA4NTgzNzQuMDUwMDc5OCwiZXhwIjoxODY2ODU4Mzc0LjA1MDA3OTgsImNsaWVudF9pZCI6ImE4ZGVhZTE5M2MwOTQ3NDNhN2QxM2Q3YTEzNGVhNDZmIiwiY2xpZW50X3R5cGUiOiJpbnRlcm5hbF9jbGllbnRfZmFjaW5nX2FwcCIsInNjb3BlIjoic2VhcmNoX3NlcnZpY2Uuc2VhcmNoLGlyb25tYW4uZ2V0X2NvbnRlbnRfbGlzdCxtbF9zZXJ2aWNlLnJlYWQiLCJkYXRhIjp7fX0.e26vh4DOH3ODza0Bheg-9HUceXoGyuh9L783tDqJ0Aq4RxkpuMPYAcN6jRrKbtO31Les7VhnTgLlOfeNELUhvSZfIafzyHE-2eTWeDeAvaYcTmvtwwlZ7uoac0hX3b4GmQdLeezvw-mIOD-eKHgm1ogUAvzBlJfWMMuuWCBauri0iK-1LxtzLHtP22uup_5u1JlSMat7f6DqZNVi3yqOGcCcBrXoIePZmFoCVu_bQfaFbHp_jbrxSYmXVOrh_JrhoswqBvOeV_MS9jn_cvEPnX5TkE4fm-ykV3zecDL1uK0M7oxztXaHCcJE_u4iwazUtPXy-5btiEtRHTI58AjcRQ"  # noqa
country_code = "QkQ%3D"
accept_language = "en"

client_headers = {
    "Authorization": client_token,
    "Country-Code": country_code,
    "Accept-Language": accept_language,
}

internal_headers = {
    "Authorization": internal_token,
    "Country-Code": country_code,
    "Accept-Language": accept_language,
}


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print(f"A new test is starting. env: {environment}")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print(f"A new test is ending. env: {environment}")


class IronManUser(HttpUser):
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

