"""
Observer is behavioral design pattern that defines one-to-many relationship.
Typically used in subscriptions where observers are receiving updates without querying.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass


class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.price)

    def set_price(self, price):
        self.price = price
        self.notify_observers()


class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"Investor {self.name} has been notified about new price: {price}")


class Bank(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"Bank {self.name} has been notified about new stock price: {price}")


if __name__ == "__main__":
    google_stock = Stock("Google", 1200)

    investor_1 = Investor("John")
    investor_2 = Investor("Alice")
    bank = Bank("America")

    google_stock.add_observer(investor_1)
    google_stock.add_observer(investor_2)
    google_stock.add_observer(bank)

    google_stock.set_price(1250)

    google_stock.remove_observer(investor_1)

    google_stock.set_price(1300)
