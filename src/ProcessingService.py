from AddsService import AddsService
from TelegramService import TelegramService
from constants import PROCESSING_URLS


class ProcessingService:
    __adds_service: AddsService = AddsService()
    __tg_svc: TelegramService = TelegramService()
    __processed_adds_ids: list = []

    def __init__(self):
        for url in PROCESSING_URLS:
            adds = self.__adds_service.fetch_adds(url)
            for add in adds:
                self.__processed_adds_ids.append(add.add_id)

    def process(self):
        for url in PROCESSING_URLS:
            adds = self.__adds_service.fetch_adds(url)
            for add in adds:
                if add.add_id not in self.__processed_adds_ids:
                    self.__tg_svc.send_add_msg(self.__adds_service.fill_add(add))
                    self.__processed_adds_ids.append(add.add_id)
