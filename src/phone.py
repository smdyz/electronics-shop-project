from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value < 1 or isinstance(value, float):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.__number_of_sim = value

# phone = Phone("iph 14", 120_000, 3, 2)
# print(repr(phone))
