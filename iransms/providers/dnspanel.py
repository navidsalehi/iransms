import requests
from .provider_base import SMSProviderBase

class DnsPanel(SMSProviderBase):
    DEFAULT_URL = "https://api.dnspanel.com/send"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self.config.get("url", self.DEFAULT_URL)

    def send_sms(self, to_number, message):
        payload = {
            "username": self.config["username"],
            "password": self.config["password"],
            "from": self.config["from_number"],
            "to": to_number,
            "message": message
        }
        try:
            response = requests.post(self.url, data=payload)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": "SMS sent successfully",
                    "provider": "dnspanel",
                    "status_code": response.status_code
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to send SMS: {response.text}",
                    "provider": "dnspanel",
                    "status_code": response.status_code
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "provider": "dnspanel",
                "status_code": 500
            }
