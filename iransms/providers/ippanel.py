import requests
from .provider_base import SMSProviderBase

class IPPanel(SMSProviderBase):
    DEFAULT_URL = "https://api.ippanel.com/v1/sms/send"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self.config.get("url", self.DEFAULT_URL)

    def send_sms(self, to_number, message):
        headers = {
            "Authorization": f"AccessKey {self.config['api_key']}"
        }
        payload = {
            "sender": self.config["from_number"],
            "recipient": to_number,
            "message": message
        }
        try:
            response = requests.post(self.url, json=payload, headers=headers)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": "SMS sent successfully",
                    "provider": "ippanel",
                    "status_code": response.status_code
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to send SMS: {response.text}",
                    "provider": "ippanel",
                    "status_code": response.status_code
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "provider": "ippanel",
                "status_code": 500
            }
