from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Any


from typing import List


class Pizza:
    def __init__(self):
        self.ingredients: List[str] = []

    def add_ingredient(self, ingredient: str):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f"Pizza with: {', '.join(self.ingredients)}"



class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def add_base_ingredients(self):
        pass

    def add_cheese(self):
        self.pizza.add_ingredient("Cheese")
        return self

    def add_salami(self):
        self.pizza.add_ingredient("Salami")
        return self

    def add_salami(self):
        self.pizza.add_ingredient("Chicken")
        return self

    def add_mushrooms(self):
        self.pizza.add_ingredient("Mushrooms")
        return self

    def add_onion(self):
        self.pizza.add_ingredient("Onion")
        return self

    def build(self):
        return self.pizza


class PizzaVegeBuilder(PizzaBuilder):
    def add_base_ingredients(self):
        self.pizza.add_ingredient("Cheese")
        self.pizza.add_ingredient("Mushrooms")
        self.pizza.add_ingredient("Onion")
        return self

class PizzaMealBuilder(PizzaBuilder):
    def add_base_ingredients(self):
        self.pizza.add_ingredient("Cheese")
        self.pizza.add_ingredient("Chicken")
        self.pizza.add_ingredient("Salami")
        return self

class PizzaCheeseBuilder(PizzaBuilder):
    def add_base_ingredients(self):
        self.pizza.add_ingredient("Cheese")
        return self


class Computer:
    def __init__(self, Procesor, GraphicCard, Windows, RAM):
        self.procesor = Procesor
        self.graphicCard = GraphicCard
        self.windows = Windows
        self.ram = RAM

    def __str__(self):
        return f"Computer: {self.procesor} and {self.graphicCard} and {self.windows} and {self.ram}"


vege_pizza = PizzaVegeBuilder().add_base_ingredients().build()
builder = PizzaBuilder()
pizza = builder.add_cheese().add_salami().add_mushrooms().build()
computer1 = Computer("Intel I7", "NVIDIA RTX 3070", "Windows 11", 32)
print(pizza)
print(vege_pizza)
print(computer1)

#Zad2

#a
class Document(ABC):
    @abstractmethod
    def create_document(self) -> str:
        pass

class WordDocument(Document):
    def create_document(self) -> str:
        return "Tworzymy dokument WordDocument"

class PDFDocument(Document):
    def create_document(self) -> str:
        return "Tworzymy dokument PDFDocument"

class DocumentFactory:
    @staticmethod
    def create_document(document_type: str) -> Document:
        if document_type == "docx":
            return WordDocument()
        elif document_type == "pdf":
            return PDFDocument()
        else:
            raise ValueError("Unknown type!")

doc1 = DocumentFactory.create_document("pdf")
print(doc1.create_document())

#b

class Animal(ABC):
    @abstractmethod
    def create_animal(self) -> str:
        pass

class Cat(Animal):
    def create_animal(self) -> str:
        return "Stworzono kota"

class Dog(Animal):
    def create_animal(self) -> str:
        return "Stworzono doga"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type!")

dog = AnimalFactory.create_animal("dog")
print(dog.create_animal())

from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self) -> str:
        pass

class WordDocument(Document):
    def open(self) -> str:
        return "Opening a Word document (.docx)"

class PDFDocument(Document):
    def open(self) -> str:
        return "Opening a PDF document (.pdf)"

class DocumentFactory:
    _registry = {}

    @classmethod
    def register_document(cls, file_extension: str, document_class):
        cls._registry[file_extension.lower()] = document_class

    @classmethod
    def create_document(cls, file_extension: str) -> Document:
        if file_extension.lower() in cls._registry:
            return cls._registry[file_extension.lower()]()
        else:
            raise ValueError(f"Unsupported document type: {file_extension}")

DocumentFactory.register_document("docx", WordDocument)
DocumentFactory.register_document("pdf", PDFDocument)

doc1 = DocumentFactory.create_document("docx")
print(doc1.open())

doc2 = DocumentFactory.create_document("pdf")
print(doc2.open())


class ExcelDocument(Document):
    def open(self) -> str:
        return "Opening an Excel document (.xlsx)"

DocumentFactory.register_document("xlsx", ExcelDocument)

doc3 = DocumentFactory.create_document("xlsx")
print(doc3.open())
try:
    doc4 = DocumentFactory.create_document("txt")
    print(doc4.open())
except ValueError as e:
    print(e)


#Zad3

class Car(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass
class HatchBackCar(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass

class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Car:
        pass

    @abstractmethod
    def create_suv(self) -> Car:
        pass

class TeslaSedan(Car):
    def specifications(self) -> str:
        return "Tesla Model S - Elektryczny Sedan"

class TeslaSUV(Car):
    def specifications(self) -> str:
        return "Tesla Model X - Elektryczny SUV"

class BMWSedan(Car):
    def specifications(self) -> str:
        return "BMW Seria 5 - Benzynowy/Dieslowy Sedan"

class BMWSUV(Car):
    def specifications(self) -> str:
        return "BMW X5 - Benzynowy/Dieslowy SUV"

class TeslaFactory(CarFactory):
    def create_sedan(self) -> Car:
        return TeslaSedan()

    def create_suv(self) -> Car:
        return TeslaSUV()

class BMWFactory(CarFactory):
    def create_sedan(self) -> Car:
        return BMWSedan()

    def create_suv(self) -> Car:
        return BMWSUV()

tesla_factory = TeslaFactory()
bmw_factory = BMWFactory()

tesla_sedan = tesla_factory.create_sedan()
tesla_suv = tesla_factory.create_suv()

bmw_sedan = bmw_factory.create_sedan()
bmw_suv = bmw_factory.create_suv()

print(tesla_sedan.specifications())
print(tesla_suv.specifications())
print(bmw_sedan.specifications())
print(bmw_suv.specifications())




@dataclass
class Wheel:
    diameter: int
    material: str = field(default="aluminium")

@dataclass
class Body:
    color: str
    thickness: float = field(default=0.6)

@dataclass
class Door:
    interior_material: str
    control: str = field(default="manual")

@dataclass
class Seat:
    material: str
    control: str = field(default="manual")


@dataclass
class Car:
    wheels: tuple
    body: Body
    doors: tuple
    seats: tuple

@dataclass
class Sedan(Car):
    pass

@dataclass
class SUV(Car):
    pass

@dataclass
class Hatchback(Car):
    pass


class CarFactory(ABC):
    @abstractmethod
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        pass

    @abstractmethod
    def produce_body(self, color: str) -> Body:
        pass

    @abstractmethod
    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        pass

    @abstractmethod
    def produce_seats(self, material: str, amount: int) -> tuple:
        pass


class TeslaFactory(CarFactory):
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        return tuple([Wheel(diameter=diameter, material="carbon") for _ in range(amount)])

    def produce_body(self, color: str) -> Body:
        return Body(color=color, thickness=0.8)

    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        return tuple([Door(interior_material=interior_material, control="electric") for _ in range(amount)])

    def produce_seats(self, material: str, amount: int) -> tuple:
        return tuple([Seat(material=material, control="electric") for _ in range(amount)])


class BMWFactory(CarFactory):
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        return tuple([Wheel(diameter=diameter, material="steel") for _ in range(amount)])

    def produce_body(self, color: str) -> Body:
        return Body(color=color, thickness=1.0)

    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        return tuple([Door(interior_material=interior_material, control="manual") for _ in range(amount)])

    def produce_seats(self, material: str, amount: int) -> tuple:
        return tuple([Seat(material=material, control="manual") for _ in range(amount)])


class AbstractCarFactory:
    _factories = {}

    @staticmethod
    def register_factory(brand: str, factory_class):
        AbstractCarFactory._factories[brand] = factory_class

    @staticmethod
    def get_factory(brand: str):
        factory = AbstractCarFactory._factories.get(brand)
        if not factory:
            raise ValueError(f"Unknown car brand: {brand}")
        return factory()


AbstractCarFactory.register_factory("Tesla", TeslaFactory)
AbstractCarFactory.register_factory("BMW", BMWFactory)


class CarManufacturer:
    client_options: dict

    def __init__(self, client_options: dict) -> None:
        self.client_options = client_options

    def produce_car(self) -> Car:
        factory = AbstractCarFactory.get_factory(self.client_options["brand"])
        wheels, body, doors, seats = self._request_parts(factory)

        if self.client_options["type"] == "Sedan":
            return Sedan(wheels=wheels, body=body, doors=doors, seats=seats)
        elif self.client_options["type"] == "SUV":
            return SUV(wheels=wheels, body=body, doors=doors, seats=seats)
        elif self.client_options["type"] == "Hatchback":
            return Hatchback(wheels=wheels, body=body, doors=doors, seats=seats)
        else:
            raise ValueError("Unknown car type")

    def _request_parts(self, factory) -> tuple:
        wheels = factory.produce_wheels(self.client_options["diameter"], 4)
        body = factory.produce_body(self.client_options["color"])
        doors = factory.produce_doors(self.client_options["doors"], 5)
        seats = factory.produce_seats(self.client_options["seats"], 5)

        return wheels, body, doors, seats


if __name__ == "__main__":
    hatchback_specification = {
        "brand": "Tesla",
        "type": "Hatchback",
        "diameter": 17,
        "color": "blue",
        "doors": "plastic",
        "seats": "leather"
    }

    manufacturer = CarManufacturer(hatchback_specification)
    tesla_hatchback = manufacturer.produce_car()

    print(tesla_hatchback)

    suv_specification = {
        "brand": "BMW",
        "type": "SUV",
        "diameter": 20,
        "color": "black",
        "doors": "leather",
        "seats": "fabric"
    }

    manufacturer = CarManufacturer(suv_specification)
    bmw_suv = manufacturer.produce_car()

    print(bmw_suv)

from typing import List


@dataclass
class Smartphone:
    brand: str
    model: str
    year: int
    specs: List[str]

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Specs: {', '.join(self.specs)}"

# 📌 Interfejs fabryki smartfonów
class SmartphoneFactory(ABC):
    @abstractmethod
    def create_smartphone(self, year: int) -> Smartphone:
        pass

# 📌 Fabryka Apfel (Apple)
class ApfelFactory(SmartphoneFactory):
    def create_smartphone(self, year: int) -> Smartphone:
        models = {
            2023: "Apfel X",
            2022: "Apfel Y",
            2021: "Apfel Z"
        }
        specs = ["OLED Display", "Face ID", "iOS"]
        return Smartphone(brand="Apfel", model=models.get(year, "Unknown"), year=year, specs=specs)

# 📌 Fabryka Szajsung (Samsung)
class SzajsungFactory(SmartphoneFactory):
    def create_smartphone(self, year: int) -> Smartphone:
        models = {
            2023: "Szajsung Ultra",
            2022: "Szajsung Pro",
            2021: "Szajsung Lite"
        }
        specs = ["AMOLED Display", "Fingerprint Sensor", "Android"]
        return Smartphone(brand="Szajsung", model=models.get(year, "Unknown"), year=year, specs=specs)

# 📌 Fabryka MajFon (Nowa Marka)
class MajFonFactory(SmartphoneFactory):
    def create_smartphone(self, year: int) -> Smartphone:
        models = {
            2023: "MajFon Mega",
            2022: "MajFon Turbo",
            2021: "MajFon Basic"
        }
        specs = ["LCD Display", "Dual SIM", "Custom OS"]
        return Smartphone(brand="MajFon", model=models.get(year, "Unknown"), year=year, specs=specs)

class AbstractSmartphoneFactory:
    _factories = {}

    @staticmethod
    def register_factory(brand: str, factory_class):
        AbstractSmartphoneFactory._factories[brand] = factory_class

    @staticmethod
    def get_factory(brand: str) -> SmartphoneFactory:
        factory = AbstractSmartphoneFactory._factories.get(brand)
        if not factory:
            raise ValueError(f"Unknown smartphone brand: {brand}")
        return factory()

AbstractSmartphoneFactory.register_factory("Apfel", ApfelFactory)
AbstractSmartphoneFactory.register_factory("Szajsung", SzajsungFactory)
AbstractSmartphoneFactory.register_factory("MajFon", MajFonFactory)

if __name__ == "__main__":
    # Zamówienia na smartfony różnych marek z różnych lat
    brands = ["Apfel", "Szajsung", "MajFon"]
    years = [2023, 2022, 2021]

    for brand in brands:
        factory = AbstractSmartphoneFactory.get_factory(brand)
        for year in years:
            smartphone = factory.create_smartphone(year)
            print(smartphone)
