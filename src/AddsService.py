import subprocess

from bs4 import BeautifulSoup

from AddsParser import AddsParser
from constants import USER_AGENT_HEADER
from Model import Model
import add_attributes
import add_configurations


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
            simple_adds = soup.find_all('li', {'class': 'ad-listitem lazyload-item'})[:5]

            parsed_adds = self.__parser.parse_list(top_adds + simple_adds)
            parsed_adds.reverse()
            return parsed_adds
        except Exception as ex:
            print(ex)
            return []

    def fill_add(self, add: Model):
        try:
            curl_url = f"curl -XGET -H '{USER_AGENT_HEADER}' '{add.url}'"
            server_response = subprocess.check_output(curl_url, shell=True).decode()
            soup = BeautifulSoup(server_response, features='lxml')

            attrs = self.__parser.parse_attrs(soup)
            for attr_k in list(attrs):
                translated_k = add_attributes.attrs_ru.get(attr_k)
                if translated_k:
                    attrs.setdefault(translated_k, attrs.pop(attr_k))

            add.attrs = attrs

            add.configs = list(map(lambda c: c.replace(c, add_configurations.configurations_ru.get(c)),
                                   self.__parser.parse_configurations(soup)))

            add.full_description = soup.find('p', {'class': 'text-force-linebreak'}).prettify()

            add.seller_name = self.__parser.parse_seller_name(soup)

            add.images = self.__parser.parse_images(soup)
            if add.images:
                add.img_url = add.images[0]

            return add
        except Exception as ex:
            print(ex)
            return add
