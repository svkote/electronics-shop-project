import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # Уровень цен с учетом скидки
    all = []  # Список для хранения всех созданных экземпляров класса

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Геттер для атрибута name.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Сеттер для атрибута name. Обрезает значение, если оно превышает 10 символов.
        """
        if len(value) > 10:
            value = value[:10]
        self._name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        cls.all.clear()  # Очищаем список перед созданием новых объектов
        with open(file_path, 'r', encoding='cp1251') as file:  # Задаем кодировку cp1251
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                cls(
                    name=row['name'],
                    price=float(row['price']),
                    quantity=int(row['quantity'])
                )

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Статический метод, возвращающий число из строки.

        :param value: Строка, содержащая число.
        :return: Целое число.
        """
        return int(float(value))
