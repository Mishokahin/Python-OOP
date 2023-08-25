from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    DEFAULT_PROTECTION = 120
    DEFAULT_PRICE = 15.0
    PRICE_INCREMENT = 0.2

    def __init__(self):
        super().__init__(protection=self.DEFAULT_PROTECTION, price=self.DEFAULT_PRICE)

    def increase_price(self):
        self.price *= (1.0 + self.PRICE_INCREMENT)

