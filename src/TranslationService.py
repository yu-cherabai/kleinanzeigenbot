import requests

from constants import TRANSLATION_URL


class TranslationService:

    def __init__(self):
        pass

    def translate(self, source_text: str):
        try:
            if len(source_text) < 3000:
                response = requests.post(url=TRANSLATION_URL,
                                         data={
                                             'q': source_text,
                                             'source': "de",
                                             'target': "ru",
                                             'format': "html",
                                         })
                return response.json()['translatedText']
            else:
                split_str = [source_text[0:len(source_text)//2], source_text[len(source_text)//2:]]
                translated_split_str = []
                for s in split_str:
                    response = requests.post(url=TRANSLATION_URL,
                                             data={
                                                 'q': s,
                                                 'source': "de",
                                                 'target': "ru",
                                                 'format': "html",
                                             })
                    translated_split_str.append(response.json()['translatedText'])
                    return translated_split_str[0][:-4] + translated_split_str[1] + "</p>"
        except Exception:
            return None
