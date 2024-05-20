import requests
from requests.exceptions import HTTPError
from .settings import Identifier

MAX_RETRIES = 3

class Requester:    
    def __init__(self):
        self.AUTH = ""

    def get(self, url: str, header: dict, params=None):
        tries = 0

        while tries < MAX_RETRIES:
            tries += 1
            with requests.get(url, headers=header, params=params) as response:
                match(response.status_code):
                    case 400:
                        print('Invalid parameter(s)')
                    case 401:
                        print('Invalid token')
                    case 403:
                        print('DoS detected')

                if tries < MAX_RETRIES:
                    continue

                if response.status_code == 200:
                    return response
                
        return HTTPError

requester = Requester()