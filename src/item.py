import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return int(self.price * float(self.quantity))

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, rout) -> None:
        with open(rout) as file:
            heading = next(file)
            reader = csv.reader(file)
            for i in reader:
                Item(i[1], float(i[1]), int(i[2]))

    @staticmethod
    def string_to_number(num_string):
        return int(float(num_string))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        self.__name = name_str
        if len(self.__name) > 10:
            self.__name = self.__name[0:10]


# Item.instantiate_from_csv("items.csv")
# print(Item.all)
