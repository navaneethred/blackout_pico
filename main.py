from WIFI_CONFIG import SSID, PASSWORD
import network
import time
import urequests

WIFI_SSID = SSID
WIFI_PASSWORD = PASSWORD
URL = "https://blk.wfrk.net/heartbeat"
SECRET_KEY="OvFmiQxVrvMj0oydYFnapKfmmpi0tlNs"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def ensure_wifi_connection():
    if not wlan.isconnected():
        print("Wi-Fi connection lost. Reconnecting...")
        wlan.disconnect()
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            print(".")
            time.sleep(1)
        print("Wi-Fi reconnected! IP:", wlan.ifconfig()[0])

ensure_wifi_connection()

while True:
    ensure_wifi_connection()

    try:
        print("Sending heartbeat...")
        response = urequests.get(URL, params={"key": SECRET_KEY}, timeout=5)
        response.close()
        print("Heartbeat sent successfully.")
    except Exception as e:
        print(f"Failed to send heartbeat: {e}")

    time.sleep(5)
