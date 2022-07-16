from AddsService import AddsService
from TelegramService import TelegramService
from constants import PROCESSING_URLS


class ProcessingService:
    __adds_service: AddsService = AddsService()
    __tg_svc: TelegramService = TelegramService()
    url_state_map: dict = {}

    def __init__(self):
        for url in PROCESSING_URLS:
            adds = self.__adds_service.fetch_adds(url)
            self.url_state_map.setdefault(url, adds)

    def process(self):
        for url in self.url_state_map.keys():
            current_adds = self.url_state_map[url]
            updated_adds = self.__adds_service.fetch_adds(url)
            new_add_ids = set(set(map(lambda m: m.add_id, updated_adds)) - set(map(lambda m: m.add_id, current_adds)))
            new_adds = list(filter(lambda m: m.add_id in new_add_ids, updated_adds))
            for new_add in new_adds:
                self.__tg_svc.send_add_msg(self.__adds_service.fill_add(new_add))
            self.url_state_map[url] = updated_adds
