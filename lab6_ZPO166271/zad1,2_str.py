from abc import ABC, abstractmethod
from typing import Any


#a
class OldSystem:
    def print_old(self):
        print("Drukowanie w starym systemie")

class Adapter:
    def __init__(self, old_system: OldSystem):
        self.old_system = old_system

    def print_new(self):
        self.old_system.print_old()

old_system = OldSystem()

adapter = Adapter(old_system)

adapter.print_new()

#b

#b)
class FahrenheitSensor:
    def get_temperature_fahrenheit(self) -> float:
        return 98.6

class FahrenheitAdapter:
    def __init__(self, fahrenheit_sensor: FahrenheitSensor):
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature_float(self) -> float:
        fahrenheit = self.fahrenheit_sensor.get_temperature_fahrenheit()
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        return celsius

fahrenheit_sensor = FahrenheitSensor()

adapter = FahrenheitAdapter(fahrenheit_sensor)

temperature_celsius = adapter.get_temperature_float()

print(f"Temperatura w stopniach Celsjusza: {temperature_celsius:.2f}°C")

#c)

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

class PayPal:
    def make_payment(self, amount: float) -> str:
        return f"Płatność {amount} PLN została przetworzona przez PayPal"

class Stripe:
    def charge_payment(self, amount: float) -> str:
        return f"Płatność {amount} PLN została przetworzona przez Stripe"

class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal: PayPal):
        self.paypal = paypal

    def process_payment(self, amount: float) -> str:
        return self.paypal.make_payment(amount)

class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe: Stripe):
        self.stripe = stripe

    def process_payment(self, amount: float) -> str:
        return self.stripe.charge_payment(amount)

paypal = PayPal()
stripe = Stripe()

paypal_adapter = PayPalAdapter(paypal)
stripe_adapter = StripeAdapter(stripe)

print(paypal_adapter.process_payment(200.00))
print(stripe_adapter.process_payment(400.00))

#2

#a


class User(ABC):
    @abstractmethod
    def get_permissions(self):
        pass

class BasicUser(User):
    def get_permissions(self):
        return "Podstawowe uprawnienia"

class UserDecorator(User):
    def __init__(self, user: User):
        self._user = user

    @abstractmethod
    def get_permissions(self):
        return self._user.get_permissions()

class AdminDecorator(UserDecorator):
    def get_permissions(self):
        return f"{self._user.get_permissions()}, Uprawnienia Admina"

class ModeratorDecorator(UserDecorator):
    def get_permissions(self):
        return f"{self._user.get_permissions()}, Uprawnienia Moderatora"

class GuestDecorator(UserDecorator):
    def get_permissions(self):
        return f"{self._user.get_permissions()}, Uprawnienia Gościa"

user = BasicUser()
print(user.get_permissions())

admin_user = AdminDecorator(user)
print(admin_user.get_permissions())

moderator_user = ModeratorDecorator(admin_user)
print(moderator_user.get_permissions())


#b

class MainClass(ABC):
    @abstractmethod
    def important_method(self) -> str:
        pass

class MyClass(MainClass):
    def important_method(self) -> str:
        return "Important value!"


class Decorator(ABC):
    def __init__(self, obj: Any) -> None:
        self.object = obj

    @abstractmethod
    def important_method(self) -> str:
        pass


class ClassDecorator(Decorator):
    def important_method(self) -> str:
        parent_value = self.object.important_method()

        return f"decorated | {parent_value} | decorated!"
    #def true_method(*args:list) -> float:
    #    form_data =kwargs
    #    password = form_data


#c


#3

#a

class Pliki:
    def save(self) -> Any:
        print(f"save a file")

    def read(self) -> Any:
        print(f"read a file")
    def delete(self) -> Any:
        print(f"delete a file")

#b 

