from constants import KLEINANZEIGEN_HOST


class Model:
    def __init__(self, add_id=None, url=None, img_url=None, location=None, created_at=None, title=None, description=None, price=None,
                 mileage=None, year=None):
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
