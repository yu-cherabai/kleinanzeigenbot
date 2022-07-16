import re

import telebot

from Model import Model
from constants import TG_TOKEN, TG_USER_IDS, DEFAULT_IMG


class TelegramService:
    __bot = telebot.TeleBot(TG_TOKEN, parse_mode='markdown')

    def __init__(self):
        pass

    def send_add_msg(self, add: Model):
        for user_id in TG_USER_IDS:
            try:
                photo = add.img_url if add.img_url else DEFAULT_IMG
                self.__bot.send_photo(chat_id=user_id, photo=photo, caption=self.__generate_msg_txt(add))
            except Exception as ex:
                print(ex)

    def __generate_msg_txt(self, add: Model) -> str:
        return f'*{self.__normalize_title(add.title)}*\n\n' \
               f'Цена:     {add.price}\n' \
               f'Год:        {add.year}\n' \
               f'Пробег: {add.mileage}\n' \
               f'Город:    `{self.__normalize_location(add.location)}`\n\n' \
               f'[Перейти к обьявлению 🚀]({add.url})'

    @staticmethod
    def __normalize_title(title: str) -> str:
        return title.replace('*', '*\\**')

    @staticmethod
    def __normalize_location(location) -> str:
        return re.sub('\((.*?)\)', "", re.sub('\d+', "", location))[1:]

