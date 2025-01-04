# IranSMS

A Python package to send SMS via multiple Iranian providers (Kavenegar, DnsPanel, IPPanel). Easily integrated with Django.

---

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
   - [Sending an SMS](#sending-an-sms)
   - [Using in Django](#using-in-django)
   - [Using in Celery Tasks](#using-in-celery-tasks)
4. [Providers](#providers)
   - [Kavenegar](#kavenegar)
   - [DnsPanel](#dnspanel)
   - [IPPanel](#ippanel)
5. [Testing](#testing)
6. [Contributing](#contributing)
7. [License](#license)

---

## Installation

Install the package using `pip`:

```bash
pip install iransms
```

# Configuration
Add the ```IRANSMS_CONFIG``` dictionary to your Django ```settings.py``` file to configure the SMS provider and credentials.

### Example Configuration
# settings.py

```python
IRANSMS_CONFIG = {
    "provider": "kavenegar",  # or "dnspanel" or "ippanel"
    "kavenegar_api_key": "your_api_key",
    "kavenegar_from_number": "your_from_number",
    "dnspanel_username": "your_username",
    "dnspanel_password": "your_password",
    "dnspanel_from_number": "your_from_number",
    "ippanel_api_key": "your_api_key",
    "ippanel_from_number": "your_from_number",
}
```

# Usage
## Sending an SMS
### You can send an SMS using the SMSSender class.

```python
from iransms import SMSSender

sender = SMSSender()
result = sender.send_sms(to_number="9876543210", message="Hello from IranSMS!")

if result["success"]:
    print(f"SMS sent successfully via {result['provider']}")
else:
    print(f"Failed to send SMS via {result['provider']}: {result['message']}")
```

## Using in Django

### Example: Sending an SMS in a Django View


```python
# views.py

from django.http import JsonResponse
from iransms import SMSSender

def send_sms_view(request):
    sender = SMSSender()
    result = sender.send_sms(to_number="9876543210", message="Hello from Django!")

    if result["success"]:
        return JsonResponse({"status": "SMS sent successfully!"})
    else:
        return JsonResponse({"status": f"Failed to send SMS: {result['message']}"}, status=500)
```

### Example: Sending an SMS in a Django Model

```python
# models.py

from django.db import models
from iransms import SMSSender

class Order(models.Model):
    customer_phone = models.CharField(max_length=15)
    status = models.CharField(max_length=50)

    def send_status_update(self):
        sender = SMSSender()
        message = f"Your order status is now {self.status}."
        result = sender.send_sms(to_number=self.customer_phone, message=message)
        return result["success"]
```

## Using in Celery Tasks
### If you’re using Celery for background tasks, you can send SMS asynchronously.

```python
# tasks.py

from celery import shared_task
from iransms import SMSSender

@shared_task
def send_sms_async(to_number, message):
    sender = SMSSender()
    result = sender.send_sms(to_number=to_number, message=message)
    return result
```


# Providers
## Kavenegar
- API Key: Required.
- From Number: Required.
- Default URL: https://api.kavenegar.com/v1/sms/send.json

## DnsPanel
- Username: Required.
- Password: Required.
- From Number: Required.
- Default URL: https://api.dnspanel.com/send

## IPPanel
- API Key: Required.
- From Number: Required.
- Default URL: https://api.ippanel.com/v1/sms/send

## Testing
To run the unit tests, navigate to the project directory and ru

```bash
python -m unittest discover tests
```

# Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeatureName).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeatureName).
5. Open a pull request.



# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.


### Enjoy using IranSMS! 🚀
