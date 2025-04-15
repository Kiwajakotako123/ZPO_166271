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
        return "Zaatakował mnie agresywnie"

class DeffensiveAttack(AttackGame):
    def attack(self) -> str:
        return "Atakuje jak jakaś ciota"

class GoodOrBadAttack(AttackGame):
    def attack(self) -> str:
        return "Nie wiem wie co on odpierdala"

class Character:
    def __init__(self, power: float, height, strategy: AttackGame):
        self.power = power
        self.height = height
        self.strategy = strategy

    def StrategyAttack(self):
        print(f"My strategy is {self.strategy.attack()}")

heros = Character(10, 200, DeffensiveAttack())
print(heros.StrategyAttack())

class SortStrategy(ABC):
    def sort(self, data: list[int]) -> list[int]:
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Używam bubble sorta")
        arr = data.copy()
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class MergeSort(SortStrategy):
    def sort(self, data) -> list[int]:
        print("Używam merge sorta")
        return sorted(data)


class QuickSort(SortStrategy):
    def sort(self, data):
        print("Używam quick sorta")
        return sorted(data)

numbers = [1, 6, 3, 4, 5, 2, 7, 8, 9, 10]
bubble = MergeSort()
sorted_numbers = bubble.sort(numbers)
print(sorted_numbers)