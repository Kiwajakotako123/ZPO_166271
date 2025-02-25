from collections import namedtuple
from dataclasses import dataclass, field
from itertools import product

from pydantic import BaseModel, Field

#1
class Employee:
    first_name: str
    last_name: str
    salary: float

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"My name is {self.first_name} {self.last_name}."


osoba1 = Employee(first_name="Radoslaw", last_name="Hubacz", salary=6000)
osoba2 = Employee(first_name="Kamil", last_name="Matusiak", salary=5000)

osoba1_info = osoba1.get_full_name()
print(osoba1_info)

osoba2_info = osoba2.get_full_name()
print(osoba2_info)

class Manager(Employee):
    departament: str

    def __init__(self, first_name: str, last_name: str, salary: float, departament: str) -> None:
        super().__init__(first_name, last_name, salary)
        self.departament = "defender"

    def get_department_info(self) -> str:
        return f"{self.first_name} {self.last_name} manages the department {self.departament}. He earns {self.salary}."

Manager =  Manager(first_name="Damian", last_name="Kowalski", salary="10000", departament="defender")
Manager_info= Manager.get_department_info()
print(Manager_info)

#2

Transaction = namedtuple("Transaction", ["tansaction_id", "amount", "currency"])

class BankAccount:
    balance: float

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def apply_transaction(self, transaction: Transaction) -> str:
        self.balance -= transaction.amount
        return f"{self.balance}"



cash = BankAccount(100000)

transaction = Transaction(1, 1000, BankAccount)

print(cash.apply_transaction(transaction))

#3
@dataclass()
class Book:
    title: str
    author: str
    year: float
    price: float

    def apply_discount(self, discount: float):
        discount = self.price * discount/100
        return self.price - discount


Book = Book("Lalka", "Bolesław Prus", 1850, 200)

discount = int(input("Jaki procent zniżki posiadasz: "))

print(Book.apply_discount(discount))

#4

@dataclass(frozen=True)
class Product:
    name: str
    price: float = Field(ge=0.01)
    category: str = field(default="General")


product = 



