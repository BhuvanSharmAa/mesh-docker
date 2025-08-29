import time
import requests

SERVICE_B_URL = "http://service-b:5000/work"

if __name__ == "__main__":
    while True:
        try:
            r = requests.get(SERVICE_B_URL)
            print(f"Response from service-b: {r.text}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)
