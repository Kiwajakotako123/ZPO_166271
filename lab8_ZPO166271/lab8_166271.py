
Senzi aka młody siwunio🙈😎
Przemek Hubacz
from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, price: float) -> float:
        pass

class PolandTax(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.23

class GermanyTax(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.19

class USA_Tax(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.07

class TaxCalculator:
    def __init__(self, strategy: TaxStrategy):
        self.strategy = strategy

    def calculate(self, price: float) -> float:
        return self.strategy.calculate_tax(price)

product_price = 100
for strategy in [PolandTax(), GermanyTax(), USA_Tax()]:
    calculator = TaxCalculator(strategy)
    print(f"Podatek: {calculator.calculate(product_price):.2f}")

#b
class AttackGame(ABC):
    def attack(self) -> str:
        pass

class AgressiveAttack(AttackGame):
    def attack(self) -> str:
        return "Ten kutas zaatakował mnie agresywnie"

class DeffensiveAttack(AttackGame):
    def attack(self) -> str:
        return "Ten kutas atakuje jak jakaś ciota"

class GoodOrBadAttack(AttackGame):
    def attack(self) -> str:
        return "Chuj wie co on odpierdala"

class Character:
    def __init__(self, power: float, height, strategy: AttackGame):
        self.power = power
        self.height = height
        self.strategy = strategy

    def StrategyAttack(self):
        print(f"My strategy is {self.strategy.attack()}")

heros = Character(10, 200, DeffensiveAttack())
print(heros.StrategyAttack())