import requests
import time
import threading


def get_response_codes_in_threads(*url: str) -> list:
    start = time.time()

    response_list: list = []

    def get_response_codes(current_url: str) -> None:

        response = requests.get(element)
        response_list.append(response.status_code)

    pool_threads: list = []

    for element in url:
        thread = threading.Thread(target=get_response_codes, args=(element,))
        pool_threads.append(thread)
        thread.start()

        threading.Thread()

    for t in pool_threads:
        t.join()

    end = time.time()

    response_list.append(end - start)

    return response_list


print(get_response_codes_in_threads('https://coda.io/', 'https://www.google.com/', 'https://robotdreams.cc/'))
