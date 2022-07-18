from telegraph import Telegraph

from constants import TELEGRAPH_TOKEN
from Model import Model
from TranslationService import TranslationService


class TelegraphService:
    __telegraph = Telegraph(TELEGRAPH_TOKEN)
    __translation_service: TranslationService = TranslationService()

    def __init__(self):
        pass

    def create_add_page(self, add: Model):
        body_html_list = []
        body_html_list.append('<h4>Характеристики:</h4>')
        body_html_list.append('<ul>')
        for attr_k, attr_v in add.attrs.items():
            body_html_list.append(f'<li>{attr_k}: {attr_v}</li>')
        body_html_list.append('</ul>')
        if add.configs:
            body_html_list.append('<h4>Комплектация:</h4>')
            body_html_list.append('<ul>')
            for conf in add.configs:
                body_html_list.append(f'<li>{conf}</li>')
            body_html_list.append('</ul>')
        body_html_list.append('<h4>Продавец:</h4>')
        body_html_list.append(f'<p>{add.seller_name}</p>')
        body_html_list.append('<h4>Описание:</h4>')
        desc = self.__translation_service.translate(add.full_description)
        body_html_list.append(f'<p>{desc if desc else add.full_description}</p>')
        body_html_list.append(f'<a href="{add.url}">Перейти к обьявлению</a>')
        for img in add.images:
            body_html_list.append(f'<img src="{img}">\n')
        body_html_list.append(f'<a href="{add.url}">Перейти к обьявлению</a>')

        body = "".join(body_html_list)
        return self.__telegraph.create_page(title=add.title, html_content=body)['url']
