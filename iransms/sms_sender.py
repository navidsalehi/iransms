from .config import Config
from .providers.kavenegar import Kavenegar
from .providers.dnspanel import DnsPanel
from .providers.ippanel import IPPanel

class SMSSender:
    def __init__(self):
        Config.validate()
        self.provider = self._get_provider()

    def _get_provider(self):
        provider_config = Config.get_provider_config(Config.PROVIDER)
        if Config.PROVIDER == "kavenegar":
            return Kavenegar(**provider_config)
        elif Config.PROVIDER == "dnspanel":
            return DnsPanel(**provider_config)
        elif Config.PROVIDER == "ippanel":
            return IPPanel(**provider_config)
        else:
            raise ValueError("Unsupported provider")

    def send_sms(self, to_number, message):
        return self.provider.send_sms(to_number, message)
