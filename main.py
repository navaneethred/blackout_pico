from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
import network
import time
import urequests

firmware_url = "https://raw.githubusercontent.com/navaneethred/blackout_pico/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

URL = "https://webhook.site/984075aa-5d14-4e1c-a40a-420d379d6b5c"

while True:
    try:
        print("Sending heartbeat...")
        response = urequests.get(URL, timeout=5)
        response.close()
        print("Heartbeat sent successfully.")
    except Exception as e:
        print(f"Failed to send heartbeat: {e}")

    time.sleep(5)
