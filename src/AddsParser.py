from Model import Model
from constants import KLEINANZEIGEN_HOST


class AddsParser:

    def parse_list(self, list_to_parse):
        parsed_list = []
        for item in list_to_parse:
            parsed_list.append(self.parse(item))
        return parsed_list

    def parse(self, item):
        try:
            model: Model = Model()
            article = item.find('article')
            model.add_id = article.get('data-adid').strip()
            model.url = f"{KLEINANZEIGEN_HOST}{article.get('data-href').strip()}"
            model.img_url = self.__get_img_url(article)

            ad_main = article.find('div', {'class': 'aditem-main'})
            ad_main_top = ad_main.find('div', {'class': 'aditem-main--top'})
            model.location = " ".join(
                ad_main_top.find('div', {'class': 'aditem-main--top--left'}).find('i').next.strip().split())
            model.created_at = self.__get_created_at(ad_main_top)

            ad_main_middle = ad_main.find('div', {'class': 'aditem-main--middle'})
            model.title = ad_main_middle.find('h2').find('a').text.strip()
            model.description = ad_main_middle.find('p', {'class': 'aditem-main--middle--description'}).text.strip()
            model.price = ad_main_middle.find('p', {'class': 'aditem-main--middle--price'}).text.strip()

            ad_main_bottom = ad_main.find('div', {'class': 'aditem-main--bottom'})
            model.mileage = ad_main_bottom.find('p').find_all('span')[0].text.strip()
            model.year = ad_main_bottom.find('p').find_all('span')[1].text.strip()
            return model
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def parse_attrs(soup) -> dict:
        attrs_res: dict = {}
        try:
            attrs = soup.find_all('li', {'class': 'addetailslist--detail'})
            for attr in attrs:
                attrs_res.setdefault(attr.next.strip(), attr.find('span').text.strip())
            return attrs_res
        except Exception as ex:
            print(ex)
            return attrs_res

    @staticmethod
    def parse_configurations(soup) -> list:
        parsed_config = []
        try:
            configs = soup.find_all('li', {'class': 'checktag'})
            for config in configs:
                parsed_config.append(config.text.strip())
            return parsed_config
        except Exception as ex:
            print(ex)
            return parsed_config

    def parse_images(self, soup):
        images = []
        try:
            img_divs = soup.find_all('div', {'class': 'galleryimage-element'})
            for div in img_divs:
                img_url = self.__parse_image(div)
                if img_url:
                    images.append(img_url)
            return images
        except Exception as ex:
            print(ex)
            return images

    @staticmethod
    def __parse_image(img_div):
        try:
            return img_div.find('img').get('src').strip()
        except Exception:
            return None

    @staticmethod
    def parse_seller_name(soup):
        try:
            return soup.find_all('span', {'class': 'text-body-regular-strong text-force-linebreak'})[0].text.strip()
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def __get_img_url(article):
        try:
            return article.find('div', {'class': 'aditem-image'}).find('a').find('div').get('data-imgsrc').strip()
        except Exception:
            return None

    @staticmethod
    def __get_created_at(ad_main_top):
        try:
            return ad_main_top.find('div', {'class': 'aditem-main--top--right'}).find('i', {'class': 'icon icon-small icon-calendar-open'}).next.strip()
        except Exception:
            return 'TOP'

