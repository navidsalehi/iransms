class SMSProviderBase:
    def __init__(self, **kwargs):
        self.config = kwargs

    def send_sms(self, to_number, message):
        raise NotImplementedError("Subclasses must implement this method")
