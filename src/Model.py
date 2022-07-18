from constants import KLEINANZEIGEN_HOST


class Model:
    def __init__(self, add_id=None, url=None, img_url=None, location=None, created_at=None, title=None,
                 description=None, price=None,
                 mileage=None, year=None, attrs=None, configs=None, seller_name=None, full_description=None,
                 images=None):
        self.add_id = add_id
        self.url = f"{KLEINANZEIGEN_HOST}{url}"
        self.img_url = img_url
        self.location = location
        self.created_at = created_at
        self.title = title
        self.description = description
        self.price = price
        self.mileage = mileage
        self.year = year
        self.attrs = attrs
        self.configs = configs
        self.seller_name = seller_name
        self.full_description = full_description
        self.images = images
