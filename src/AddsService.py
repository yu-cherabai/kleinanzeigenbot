import subprocess

from bs4 import BeautifulSoup

from AddsParser import AddsParser
from constants import USER_AGENT_HEADER


class AddsService:
    __parser = AddsParser()

    def __init__(self):
        pass

    def fetch_adds(self, url) -> list:
        try:
            curl_url = f"curl -XGET -H '{USER_AGENT_HEADER}' '{url}'"
            server_response = subprocess.check_output(curl_url, shell=True).decode()
            soup = BeautifulSoup(server_response, features='lxml')

            top_adds = soup.find_all('li', {'class': 'ad-listitem lazyload-item badge-topad is-topad'})
            simple_adds = soup.find_all('li', {'class': 'ad-listitem lazyload-item'})

            parsed_adds = self.__parser.parse_list(top_adds + simple_adds)
            parsed_adds.reverse()
            return parsed_adds
        except Exception as e:
            print(e)
            return []
