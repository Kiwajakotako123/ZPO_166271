from copy import deepcopy
from typing import Any

#a

class CharacterPrototype:
    def __init__(self) -> None:
        self.objects = dict()

    def add_prototype(self, id_: int, obj: Any) -> None:
        self.objects[id_] = obj

    def del_prototype(self, id_: int) -> None:
        del self.objects[id_]

    def clone(self, id_: int, **kwargs: dict) -> Any:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")


class Mage:
    def __init__(
        self,
        hp: int,
        mana: int,
        inteligent: int,
        type: str,
        lvl: int,
        nick: str,
        id: int,
        **kwargs: dict,
        ) -> None:
        self.hp = hp
        self.mana = mana
        self.inteligent = inteligent
        self.type = type
        self.lvl = lvl
        self.nick = nick
        self.id = id

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

class Warrior:
    def __init__(
        self,
        hp: int,
        strong: int,
        speed: int,
        stamina: int,
        type: str,
        lvl: int,
        **kwargs: dict,
        ) -> None:
        self.hp = hp
        self.strong = strong
        self.speed = speed
        self.stamina = stamina
        self.type = type
        self.lvl = lvl

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)


magik = Mage(100, 800, 25, "fire", 23, "napalonymatus09", 12)
print(magik)

prototypes = CharacterPrototype()
prototypes.add_prototype("1", magik)
another_mag = prototypes.clone("1", nick="poteznyradek05", id=13)
print(another_mag)

#b

class Prototype:
    def __init__(self) -> None:
        self.objects = dict()

    def add_prototype(self, id_: int, obj: Any) -> None:
        self.objects[id_] = obj

    def del_prototype(self, id_: int) -> None:
        del self.objects[id_]

    def clone(self, id_: int, **kwargs: dict) -> Any:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")


class Car:
    def __init__(
            self,
            brand: str,
            model: str,
            engine: str,
            gearbox: str,
            body_type: str,
            licence_plate: str,
            owner: str,
            **kwargs: dict,
    ) -> None:
        self.brand = brand
        self.model = model
        self.engine = engine
        self.gearbox = gearbox
        self.body_type = body_type
        self.licence_plate = licence_plate
        self.owner = owner

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

ford_focus = Car("Ford", "Focus mk2", "1.6D", "manual", "hatchback", "XX YYYYY", "Wujek Janusz", color="silver", doors=5)
print(ford_focus)

prototypes = Prototype()
prototypes.add_prototype("1", ford_focus)
another_car = prototypes.clone("1", license_plate="AA BBBBB", owner="other")
another_car2 = prototypes.clone("1")
print(another_car)
print(another_car2)

#c

class Configuration:
    def __init__(
            self,
            sound: str,
            theme: str,
            nick: str,
            **kwargs: dict,
    ) -> None:
        self.sound = sound
        self.theme = theme
        self.nick = nick

    for key in kwargs:
        setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

Flachscore = Configuration("40%", "light", "Kiwajakotako")
print(Flachscore)

