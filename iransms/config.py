from django.conf import settings

class Config:
    SMS_CONFIG = getattr(settings, "IRANSMS_CONFIG", {})

    PROVIDER = SMS_CONFIG.get("provider", "ippanel").lower()

    @staticmethod
    def get_provider_config(provider):
        if provider == "kavenegar":
            return {
                "api_key": Config.SMS_CONFIG.get("kavenegar_api_key"),
                "from_number": Config.SMS_CONFIG.get("kavenegar_from_number"),
                "url": Config.SMS_CONFIG.get("kavenegar_url")
            }
        elif provider == "dnspanel":
            return {
                "username": Config.SMS_CONFIG.get("dnspanel_username"),
                "password": Config.SMS_CONFIG.get("dnspanel_password"),
                "from_number": Config.SMS_CONFIG.get("dnspanel_from_number"),
                "url": Config.SMS_CONFIG.get("dnspanel_url")
            }
        elif provider == "ippanel":
            return {
                "api_key": Config.SMS_CONFIG.get("ippanel_api_key"),
                "from_number": Config.SMS_CONFIG.get("ippanel_from_number"),
                "url": Config.SMS_CONFIG.get("ippanel_url")
            }
        else:
            raise ValueError("Unsupported provider")

    @staticmethod
    def validate():
        supported_providers = ["kavenegar", "dnspanel", "ippanel"]
        if Config.PROVIDER not in supported_providers:
            raise ValueError(f"Unsupported provider. Supported providers: {supported_providers}")

        provider_config = Config.get_provider_config(Config.PROVIDER)
        if not all(provider_config.values()):
            raise ValueError(f"Missing credentials for {Config.PROVIDER}")