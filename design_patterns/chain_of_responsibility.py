"""
Chain of Responsibility is behavioral design pattern
that allows passing request along chain of handlers.
"""

from abc import ABC, abstractmethod


class PurchaseRequest:
    def __init__(self, amount, purpose):
        self.amount = amount
        self.purpose = purpose


class Approver(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request: PurchaseRequest):
        pass


class Manager(Approver):
    def handle_request(self, request: PurchaseRequest):
        if request.amount < 1000:
            print(f"Manager approved the request for {request.amount} USD: {request.purpose}")
        elif self.successor:
            print(f"Manager passed the request for {request.amount} USD to the next level.")
            self.successor.handle_request(request)


class Director(Approver):
    def handle_request(self, request: PurchaseRequest):
        if request.amount < 5000:
            print(f"Director approved the request for {request.amount} USD: {request.purpose}")
        elif self.successor:
            print(f"Director passed the request for {request.amount} USD to the next level.")
            self.successor.handle_request(request)


class VicePresident(Approver):
    def handle_request(self, request: PurchaseRequest):
        if request.amount < 10000:
            print(f"Vice President approved the request for {request.amount} USD: {request.purpose}")
        elif self.successor:
            print(f"Vice President passed the request for {request.amount} USD to the next level.")
            self.successor.handle_request(request)


class CEO(Approver):
    def handle_request(self, request: PurchaseRequest):
        print(f"CEO approved the request for {request.amount} USD: {request.purpose}")


# Client code
if __name__ == "__main__":
    # Step 4: Create the chain of responsibility
    ceo = CEO()
    vice_president = VicePresident(successor=ceo)
    director = Director(successor=vice_president)
    manager = Manager(successor=director)

    # Step 5: Create and process some requests
    requests = [
        PurchaseRequest(500, "Office supplies"),
        PurchaseRequest(2000, "New laptops"),
        PurchaseRequest(7000, "Office renovation"),
        PurchaseRequest(15000, "New company car")
    ]

    for req in requests:
        print(f"\nProcessing request for {req.amount} USD: {req.purpose}")
        manager.handle_request(req)
