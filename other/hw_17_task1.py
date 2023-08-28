import requests
import time
import threading


# Завдання 1
def get_response_codes(*args):
    start_time = time.time()
    response_codes = []

    for site in args:
        try:
            response = requests.get(site)
            response_codes.append(response.status_code)
        except requests.RequestException as e:
            response_codes.append(f"Error for {site}: {e}")

    elapsed_time = time.time() - start_time
    response_codes.append(f"Function executed in {elapsed_time:.2f} seconds.")

    return response_codes
