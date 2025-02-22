import csv

class Item:
    pay_rate = 1.0
    all = []


    def __init__(self,name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price},{self.quantity})"

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
        if len(self.__name) > 10:
            raise ValueError('Не больше 10 символов')
        return self.__name

    @classmethod
    def instantiate_from_csv(cls) -> None:
        cls.all = []
        with open('../src/items.csv', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            if file is None:
                raise FileNotFoundError('Отсутствует файл item.csv')
            else:
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    else:
                        cls.all.append(row)
        return cls.all.pop(1)



    @staticmethod
    def string_to_number(number) -> int:
        return int(number.split('.')[0])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity*self.price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    def __add__(self, other):
        if isinstance(other,Item):
            return self.quantity + other.quantity
        else:
            raise TypeError('Складывать можно только объекты Item и дочерние от них.')

