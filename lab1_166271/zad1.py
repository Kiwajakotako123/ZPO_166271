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

    def get_info(self) -> str:
        return f"Your product is {self.name} which cost {self.price}."

Product0 = Product(name="chipsy", price="100.0")

Product0_info = Product0.get_info()

print(Product0_info)

#zad5

class Car:
    brand: str
    model: str
    year: float

    def __init__(self, brand: str, model: str, year: float) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def is_classic(self) -> bool:
        if(self.year>25):
            return False
        else:
            return True

car1 = Car("BMW", "M4", 2)

print(car1.is_classic())




#Zad6

class ElectricVehicle:
    def fuel_type(self) -> str:
        return "electric"

class GasolineVehicle:
    def fuel_type(self) -> str:
        return "gasoline"

class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self) -> str:
        return "hybrid"

electric_car = ElectricVehicle()
gasoline_car = GasolineVehicle()
hybrid_car = HybridCar()

print(electric_car.fuel_type())
print(gasoline_car.fuel_type())
print(hybrid_car.fuel_type())



#Zad7

class Person:
    def introduce(self) -> str:
        return f"I am a person."

class Worker(Person):
    def introduce(self) -> str:
        return f"I am a worker."

class Student(Person):
    def introduce(self) -> str:
        return f"I am a student."

class WorkingStudent(Worker, Student):
    pass

person = Person()
worker = Worker()
student = Student()
working_student = WorkingStudent()

print(person.introduce())
print(worker.introduce())
print(student.introduce())
print(working_student.introduce())



#Zad8

class Animal:
    def make_sound(self) -> str:
        return "Some sound."

class Pet:
    def is_domestic(self) -> bool:
        return True


class Dog(Animal, Pet):
    def make_sound(self) -> str:
        return "Bark"


dog = Dog()
print(dog.make_sound())
print(dog.is_domestic())



#Zad9

class FlyingVehicle:
    def move(self) -> str:
        return "I fly."

class WaterVehicle:
    def move(self) -> str:
        return "I sail."

class AmphibiousVehicle(FlyingVehicle, WaterVehicle):
    def move(self, mode: str) -> str:
        if mode == "air":
            return FlyingVehicle.move(self)
        elif mode == "water":
            return WaterVehicle.move(self)
        else:
            return "Invalid mode"


amphibious = AmphibiousVehicle()
print(amphibious.move("air"))
print(amphibious.move("water"))
print(amphibious.move("land"))



#Zad10

class Robot:
    def operate(self) -> str:
        return "Performing task"

class AI:
    def think(self) -> str:
        return "Processing data"

class Android(Robot, AI):
    def self_learn(self) -> str:
        return "Learning new skills"


android = Android()
print(android.operate())
print(android.think())
print(android.self_learn())



#Zad11
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9

celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C to {fahrenheit_temp}°F")

fahrenheit_temp = 77
celsius_temp = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F to {celsius_temp}°C")





#Zad12

class IDGenerator:
    _id_counter = 0

    def __init__(self):
        self.id = IDGenerator.generate_id()

    @classmethod
    def generate_id(cls) -> int:
        cls._id_counter += 1
        return cls._id_counter


obj1 = IDGenerator()
print(f"ID pierwszego obiektu: {obj1.id}")

obj2 = IDGenerator()
print(f"ID drugiego obiektu: {obj2.id}")



#Zad13

class Store:
    total_customers = 0

    @classmethod
    def add_customer(cls):
        cls.total_customers += 1

    @classmethod
    def get_total_customers(cls) -> int:
        return cls.total_customers


Store.add_customer()
Store.add_customer()
print(f"Liczba klientów: {Store.get_total_customers()}")

#Zad14

class MathOperations:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @classmethod
    def identity_matrix(cls, size: int):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


print(f"Suma: {MathOperations.add(3, 4)}")
print(f"Iloczyn: {MathOperations.multiply(3, 4)}")
print("Macierz jednostkowa:")
for row in MathOperations.identity_matrix(3):
    print(row)

#Zad15

class GameCharacter:
    default_health = 100

    def __init__(self):
        self.health = GameCharacter.default_health

    def restore_health(self):
        self.health = GameCharacter.default_health

    @classmethod
    def set_default_health(cls, new_value: int):
        cls.default_health = new_value


character1 = GameCharacter()
character2 = GameCharacter()
print(f"Zdrowie postaci 1: {character1.health}")
GameCharacter.set_default_health(150)
character3 = GameCharacter()
print(f"Nowa domyślna wartość zdrowia: {character3.health}")



#Zad16

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Pole koła o promieniu 5: {circle.area():.2f}")
print(f"Pole prostokąta o wymiarach 4x6: {rectangle.area()}")

#Zad17

class PaymentProcessor(ABC):
    @abstractmethod
    def authorize_payment(self, amount: float) -> bool:
        pass

    @abstractmethod
    def capture_payment(self, amount: float) -> bool:
        pass


class CreditCardPayment(PaymentProcessor):
    def authorize_payment(self, amount: float) -> bool:
        print(f"Autoryzacja płatności kartą kredytową na kwotę {amount} zł")
        return True

    def capture_payment(self, amount: float) -> bool:
        print(f"Przetwarzanie płatności kartą kredytową na kwotę {amount} zł")
        return True


class PayPalPayment(PaymentProcessor):
    def authorize_payment(self, amount: float) -> bool:
        print(f"Autoryzacja płatności PayPal na kwotę {amount} zł")
        return True

    def capture_payment(self, amount: float) -> bool:
        print(f"Przetwarzanie płatności PayPal na kwotę {amount} zł")
        return True

credit_card = CreditCardPayment()
paypal = PayPalPayment()

credit_card.authorize_payment(100)
credit_card.capture_payment(100)

paypal.authorize_payment(200)
paypal.capture_payment(200)



#Zad18

class Vehicle(ABC):
    @abstractmethod
    def max_speed(self) -> float:
        pass


class Car(Vehicle):
    def __init__(self, speed: float):
        self.speed = speed

    def max_speed(self) -> float:
        return self.speed


class Bicycle(Vehicle):
    def __init__(self, speed: float):
        self.speed = speed

    def max_speed(self) -> float:
        return self.speed

car = Car(180)
bicycle = Bicycle(25)

print(f"Maksymalna prędkość samochodu: {car.max_speed()} km/h")
print(f"Maksymalna prędkość roweru: {bicycle.max_speed()} km/h")

#Zad19

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str) -> None:
        pass


class MySQLConnection(DatabaseConnection):
    def connect(self) -> None:
        print("Łączenie z bazą danych MySQL...")

    def execute_query(self, query: str) -> None:
        print(f"Wykonuję zapytanie w MySQL: {query}")


# Klasa PostgreSQLConnection implementująca DatabaseConnection
class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> None:
        print("Łączenie z bazą danych PostgreSQL...")

    def execute_query(self, query: str) -> None:
        print(f"Wykonuję zapytanie w PostgreSQL: {query}")

mysql = MySQLConnection()
postgres = PostgreSQLConnection()

mysql.connect()
mysql.execute_query("SELECT * FROM users")

postgres.connect()
postgres.execute_query("SELECT * FROM orders")

Utworzyć klasę abstrakcyjną Instrument z metodą play(), 
a następnie zaimplementować klasy Piano i Guitar, które będą miały różne wersje tej metody.

#Zad20

class Instrument(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

class Piano(Instrument):
    def play(self) -> None:
        print("Gram na pianinie")

class Guitar(Instrument):
    def play(self) -> None:
        print("Gram na gitarze")

piano = Piano()
guitar = Guitar()

piano.play()
guitar.play()

