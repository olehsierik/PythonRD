import requests
import time


def get_response_codes(*url: str) -> list:
    start = time.time()

    response_list: list = []

    for element in url:
        response = requests.get(element)
        response_list.append(response.status_code)

    end = time.time()

    response_list.append(end - start)

    return response_list


print(get_response_codes('https://coda.io/', 'https://www.google.com/', 'https://robotdreams.cc/'))
