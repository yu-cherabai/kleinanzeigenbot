import requests

from constants import TRANSLATION_URL


class TranslationService:

    def __init__(self):
        pass

    def translate(self, source_text: str):
        try:
            response = requests.post(url=TRANSLATION_URL,
                                     data={
                                         'q': source_text,
                                         'source': "de",
                                         'target': "ru",
                                         'format': "html",
                                     })
            return response.json()['translatedText']
        except Exception:
            return None
