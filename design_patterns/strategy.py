"""
Strategy is behavioral design pattern that allows selecting algorithm behavior at runtime.
"""


from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number

    def pay(self, amount):
        return f"{amount} paid using Credit Card by {self.name}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"{amount} paid using PayPal by {self.email}"


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"{amount} paid using Bitcoin with wallet {self.wallet_address}"


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Set a new strategy at runtime."""
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)


if __name__ == "__main__":
    # Initialize the processor with a payment strategy
    payment_processor = PaymentProcessor(CreditCardPayment("John Doe", "1234-5678-9876-5432"))

    # Process payment using Credit Card
    print(payment_processor.process_payment(100))  # Output: 100 paid using Credit Card by John Doe

    # Switch to PayPal payment strategy
    payment_processor.set_strategy(PayPalPayment("john.doe@example.com"))
    print(payment_processor.process_payment(150))  # Output: 150 paid using PayPal by john.doe@example.com

    # Switch to Bitcoin payment strategy
    payment_processor.set_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    print(payment_processor.process_payment(200))  # Output: 200 paid using Bitcoin with wallet 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
