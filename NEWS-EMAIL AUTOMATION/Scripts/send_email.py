import yagmail

import sys
import os


# Add the root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.api_keys import WEATHER_API_KEY

from config.settings import EMAIL, PASSWORD, RECIPIENTS

def send_email(subject, content):
    try:
        yag = yagmail.SMTP(EMAIL, PASSWORD)
        yag.send(to=RECIPIENTS, subject=subject, contents=content)
        return "Email sent successfully."
    except Exception as e:
        return f"Error sending email: {e}"
