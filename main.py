from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
import network
import time
import urequests

firmware_url = "https://raw.githubusercontent.com/navaneethred/blackout_pico/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

URL = "https://webhook.site/984075aa-5d14-4e1c-a40a-420d379d6b5c"
SECRET_KEY="OvFmiQxVrvMj0oydYFnapKfmmpi0tlNs"

# def ensure_wifi_connection():
#     """Checks Wi-Fi status and reconnects if necessary."""
#     if not wlan.isconnected():
#         print("Wi-Fi connection lost. Reconnecting...")
#         wlan.disconnect()
#         wlan.connect(SSID, PASSWORD)
#         while not wlan.isconnected():
#             print(".")
#             time.sleep(1)
#         print("Wi-Fi reconnected! IP:", wlan.ifconfig()[0])

while True:
    try:
        print("Sending heartbeat...")
        response = urequests.get(f"{URL}?key={SECRET_KEY}", timeout=5)
        response.close()
        print("Heartbeat sent successfully.")
    except Exception as e:
        print(f"Failed to send heartbeat: {e}")

    time.sleep(5)
