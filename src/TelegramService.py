import re

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from Model import Model
from constants import TG_TOKEN, TG_USER_IDS, DEFAULT_IMG
from TelegraphService import TelegraphService


class TelegramService:
    __bot = telebot.TeleBot(TG_TOKEN, parse_mode='markdown')
    __telegraph_svc = TelegraphService()

    def __init__(self):
        pass

    def send_add_msg(self, add: Model):
        for user_id in TG_USER_IDS:
            try:
                page_url = self.__create_page(add)
                photo = add.img_url if add.img_url else DEFAULT_IMG
                if page_url:
                    markup = InlineKeyboardMarkup()
                    markup.add(InlineKeyboardButton('Подробнее', url=page_url),
                               InlineKeyboardButton('Обьявление', url=add.url))
                    self.__bot.send_photo(chat_id=user_id, photo=photo, caption=self.__generate_msg_txt(add),
                                          reply_markup=markup)
                else:
                    msg_txt = f'{self.__generate_msg_txt(add)}\n[Перейти к обьявлению 🚀]({add.url})'
                    self.__bot.send_photo(chat_id=user_id, photo=photo, caption=msg_txt)
            except Exception as ex:
                print(ex)

    def __generate_msg_txt(self, add: Model) -> str:
        msg_body_list = []
        msg_body_list.append(f'Цена:      *{add.price}*\n')
        msg_body_list.append(f'Год:         {add.year}\n')
        msg_body_list.append(f'Пробег:  {add.mileage}\n')
        if add.attrs.get('Мощность'):
            msg_body_list.append(f'Силы:      {add.attrs.get("Мощность")}\n')
        if  add.attrs.get('Топливо'):
            msg_body_list.append(f'Топливо: {add.attrs.get("Топливо")}\n')
        msg_body_list.append(f'Город:      `{self.__normalize_location(add.location)}`\n')

        msg_body = ''.join(msg_body_list)

        return f'*{self.__normalize_title(add.title)}*\n\n' \
               f'{msg_body}'

    def __create_page(self, add):
        try:
            return self.__telegraph_svc.create_add_page(add)
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def __normalize_title(title: str) -> str:
        return title.replace('*', '*\\**')

    @staticmethod
    def __normalize_location(location) -> str:
        return re.sub('\((.*?)\)', "", re.sub('\d+', "", location))[1:]

