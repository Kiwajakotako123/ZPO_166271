from typing import Self

class Iterator:
    n: int
    add: int
    limit: int
    k: int

    def __init__(self, limit: int) -> None:
        self.n = 0
        self.limit = limit
        self.add = 1

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.n < self.limit:
            self.n += self.add
            self.add += 2
            return self.n

        raise StopIteration
iterator = Iterator(20)
while 1:
    print(next(iterator))
#b

from typing import List, Iterator

class Order:
    def __init__(self, id: int, status: str):
        self.id = id
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, status={self.status})"

class OrderIterator(Iterator):
    def __init__(self, orders: List[Order], status: str):
        self.orders = orders
        self.status = status
        self.index = 0
        self.filtered_orders = [order for order in self.orders if order.status == self.status]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.filtered_orders):
            order = self.filtered_orders[self.index]
            self.index += 1
            return order
        else:
            raise StopIteration

orders = [
    Order(1, "nowe"),
    Order(2, "w realizacji"),
    Order(3, "zrealizowane"),
    Order(4, "nowe"),
    Order(5, "w realizacji"),
]

iterator = OrderIterator(orders, "nowe")

for order in iterator:
    print(order)

print("Sena magłiszana i jesty bambo bambo")
#c
from typing import Generator


def prime_generator(limit: float) -> Generator:
    n = 1
    gen_sum = 0.0
    while gen_sum <= limit:
        gen_sum += 1/n
        yield gen_sum
        n += 1

gen = prime_generator(5.0)
for i in gen:
    print(i)

#3a

from abc import abstractmethod

class Document(ABC):
    name: str
    content: str

    def __init__(self, name: str, content: str) -> None:
        self.name = name
        self.content = content

    @abstractmethod
    def save(self) -> str:
        pass

    @abstractmethod
    def show_content(self) -> str:
        pass

    def show_extension(self) -> str:
        pass

    def show_file(self) -> None:
        self.save()
        self.show_content()
        self.show_extension()

class PDF(Document):
    def save(self) -> str:
        print("PDF file saved.")

    def show_content(self) -> str:
        print(self.content)

    def show_extension(self) -> str:
        print("PDF File")

class DOCX(Document):
    def save(self) -> str:
        print("DOCX file saved.")

    def show_content(self) -> str:
        print(self.content)

    def show_extension(self) -> str:
        print("DOCX File")

class TXT(Document):
    def save(self) -> str:
        print("TXT file saved.")

    def show_content(self) -> str:
        print(self.content)

    def show_extension(self) -> str:
        print("TXT File")

pdf_file = PDF("PlikPDF", "To jest zawartosc pliku PDF")
docx_file = DOCX("PlikDOCX", "To jest zawartosc pliku DOCX")
txt_file = TXT("PlikTXT", "To jest zawartosc pliku TXT")

print("====")
pdf_file.show_file()
print("====")
docx_file.show_file()
print("====")
txt_file.show_file()
print("====")


#b
from abc import ABC, abstractmethod


class OrderProcessor(ABC):

    def process_order(self):
        self.receive_order()
        self.prepare_order()
        self.ship_order()
        self.send_confirmation()

    @abstractmethod
    def receive_order(self):
        pass

    @abstractmethod
    def prepare_order(self):
        pass

    @abstractmethod
    def ship_order(self):
        pass

    def send_confirmation(self):
        print("Order has been processed and confirmation sent.")


class StandardDeliveryOrder(OrderProcessor):


    def receive_order(self):
        print("Receiving the order through standard process.")

    def prepare_order(self):
        print("Preparing the order for standard delivery.")

    def ship_order(self):
        print("Shipping the order via standard delivery method.")


class ExpressDeliveryOrder(OrderProcessor):
    """
    Realizacja zamówienia z dostawą ekspresową.
    """

    def receive_order(self):
        print("Receiving the order through expedited process.")

    def prepare_order(self):
        print("Preparing the order for express delivery.")

    def ship_order(self):
        print("Shipping the order via express delivery method.")


class InPersonPickupOrder(OrderProcessor):
    """
    Realizacja zamówienia z odbiorem osobistym.
    """

    def receive_order(self):
        print("Receiving the order for in-person pickup.")

    def prepare_order(self):
        print("Preparing the order for in-person pickup.")

    def ship_order(self):
        print("Order is ready for pickup at the designated location.")


order_standard = StandardDeliveryOrder()
order_standard.process_order()

order_express = ExpressDeliveryOrder()
order_express.process_order()

order_pickup = InPersonPickupOrder()
order_pickup.process_order()

#c


class FileExporter(ABC):
    def export(self, data):
        self.open_file()
        self.write_data(data)
        self.close_file()

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def close_file(self):
        pass


class CSVExporter(FileExporter):
    def open_file(self):
        print("Opening CSV file for writing.")

    def write_data(self, data):
        print(f"Writing data to CSV: {data}")

    def close_file(self):
        print("Closing CSV file.")


class JSONExporter(FileExporter):
    def open_file(self):
        print("Opening JSON file for writing.")

    def write_data(self, data):
        print(f"Writing data to JSON: {data}")

    def close_file(self):
        print("Closing JSON file.")


class XMLExporter(FileExporter):
    def open_file(self):
        print("Opening XML file for writing.")

    def write_data(self, data):
        print(f"Writing data to XML: {data}")

    def close_file(self):
        print("Closing XML file.")


data = "Sample data"

csv_exporter = CSVExporter()
csv_exporter.export(data)

json_exporter = JSONExporter()
json_exporter.export(data)

xml_exporter = XMLExporter()
xml_exporter.export(data)