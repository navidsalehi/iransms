import requests
from .provider_base import SMSProviderBase

class Kavenegar(SMSProviderBase):
    DEFAULT_URL = "https://api.kavenegar.com/v1/sms/send.json"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self.config.get("url", self.DEFAULT_URL)

    def send_sms(self, to_number, message):
        payload = {
            "receptor": to_number,
            "sender": self.config["from_number"],
            "message": message,
            "api_key": self.config["api_key"]
        }
        try:
            response = requests.post(self.url, data=payload)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": "SMS sent successfully",
                    "provider": "kavenegar",
                    "status_code": response.status_code
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to send SMS: {response.text}",
                    "provider": "kavenegar",
                    "status_code": response.status_code
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "provider": "kavenegar",
                "status_code": 500
            }
