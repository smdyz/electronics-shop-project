import csv
from pathlib import Path


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
    def instantiate_from_csv(cls, file):
        parents_path = Path(__file__).parent.parent
        file_path = Path(parents_path, file)
        try:
            with open(file_path) as f:
                reader = csv.DictReader(f)
                for i in reader:
                    it = Item(i['name'], float(i['price']), int(i['quantity']))
                    return it
        except (ValueError, KeyError):
            raise InstantiateCSVError(f"Файл {file} поврежден")
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {file}')

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

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл поврежден"

# Item.instantiate_from_csv("items2.csv")
