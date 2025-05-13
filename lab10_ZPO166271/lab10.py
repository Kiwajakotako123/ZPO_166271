# Zadanie 4.

class Memento:
    _states: list
    _i: int

    def __init__(self) -> None:
        self._states = []
        self._i = -1

    def save_state(self, state: str) -> None:
        if self._i != len(self._states) - 1:
            self._states = self._states[:self._i + 1]

        self._states.append(state)
        self._i += 1

    def undo(self) -> None:
        if self._i > 0:
            self._i -= 1

    def redo(self) -> None:
        if self._i < len(self._states) - 1:
            self._i += 1

    def read_state(self) -> str:
        return self._states[self._i]


class Settings:
    def __init__(self) -> None:
        self.settings = []
        self.memento = Memento()

    def add_setting(self, setting: str) -> None:
        self.settings.append(setting)
        self.memento.save_state(self.settings)

    def show_settings(self, show_deleted: bool = True) -> None:
        for i, setting in enumerate(self.settings):
            if not show_deleted and setting.startswith("!"):
                continue
            print(i + 1, setting)

    def delete_setting(self, num: int) -> None:
        self.settings[num - 1] = "!" + self.settings[num - 1]
        self.memento.save_state(self.settings)

    def undo(self) -> None:
        self.memento.undo()
        self.settings = self.memento.read_state()

    def redo(self) -> None:
        self.memento.redo()
        self.settings = self.memento.read_state()


player_settings = Settings()
player_settings.add_setting("Audio 50")
player_settings.show_settings()
player_settings.add_setting("Video Quality Medium")
player_settings.add_setting("WASD movement")
player_settings.show_settings()
player_settings.delete_setting(1)
player_settings.show_settings()
player_settings.show_settings(show_deleted=False)
player_settings.undo()
player_settings.show_settings()


#Zadanie 5

from abc import ABC, abstractmethod

class Request:
    def __init__(self, amount: float) -> None:
        self.amount = amount


class Approver(ABC):
    successor = None

    def set_successor(self, successor) -> None:
        self.successor = successor

    @abstractmethod
    def handle(self, request: Request) -> None:
        pass


class Manager(Approver):
    def handle(self, request: Request) -> None:
        if request.amount <= 1000:
            print("Manager approved request")
        elif self.successor:
            self.successor.handle(request)


class COO(Approver):
    def handle(self, request: Request) -> None:
        if request.amount <= 5000:
            print("COO approved request")
        elif self.successor:
            self.successor.handle(request)


class CTO(Approver):
    def handle(self, request: Request) -> None:
        if request.amount <= 20000:
            print("CTO approved request")
        elif self.successor:
            self.successor.handle(request)


class CEO(Approver):
    def handle(self, request: Request) -> None:
        if request.amount > 20000:
            print("CEO approved request")


# utworzenie łańcucha

m = Manager()
coo = COO()
cto = CTO()
ceo = CEO()

m.set_successor(coo)
coo.set_successor(cto)
cto.set_successor(ceo)

# test

r1 = Request(500)
r2 = Request(4000)
r3 = Request(15000)
r4 = Request(100000)

m.handle(r1)
m.handle(r2)
m.handle(r3)
m.handle(r4)


from abc import ABC, abstractmethod

class Email:
    def __init__(self, subject: str, body: str) -> None:
        self.subject = subject
        self.body = body


class EmailFilter(ABC):
    successor = None

    def set_successor(self, successor):
        self.successor = successor

    @abstractmethod
    def check(self, email: Email):
        pass


class HeaderFilter(EmailFilter):
    def check(self, email: Email):
        if "X-Phish" in email.subject:
            print("Blocked due to suspicious header")
        elif self.successor:
            self.successor.check(email)


class SpamFilter(EmailFilter):
    def check(self, email: Email):
        if "Buy now" in email.body or "promo" in email.body:
            print("Blocked as spam")
        elif self.successor:
            self.successor.check(email)


class VirusFilter(EmailFilter):
    def check(self, email: Email):
        if "<script>" in email.body:
            print("Blocked: contains virus")
        elif self.successor:
            self.successor.check(email)


class DefaultFilter(EmailFilter):
    def check(self, email: Email):
        print("Email delivered")


# łańcuch filtrów

hf = HeaderFilter()
sf = SpamFilter()
vf = VirusFilter()
df = DefaultFilter()

hf.set_successor(sf)
sf.set_successor(vf)
vf.set_successor(df)

# testy

e1 = Email("Hello", "This is normal message")
e2 = Email("URGENT X-Phish", "urgent update")
e3 = Email("Promo inside", "Buy now! 2 for 1")
e4 = Email("Security", "Hi! <script>alert('danger')</script>")

hf.check(e1)
hf.check(e2)
hf.check(e3)
hf.check(e4)


from abc import ABC, abstractmethod

class Ticket:
    def __init__(self, category: str, message: str) -> None:
        self.category = category
        self.message = message


class SupportHandler(ABC):
    successor = None

    def set_next(self, successor):
        self.successor = successor

    @abstractmethod
    def handle(self, ticket: Ticket):
        pass


class HardwareSupport(SupportHandler):
    def handle(self, ticket: Ticket):
        if ticket.category == "hardware":
            print(f"Hardware team: {ticket.message}")
        elif self.successor:
            self.successor.handle(ticket)


class SoftwareSupport(SupportHandler):
    def handle(self, ticket: Ticket):
        if ticket.category == "software":
            print(f"Software team: {ticket.message}")
        elif self.successor:
            self.successor.handle(ticket)


class NetworkSupport(SupportHandler):
    def handle(self, ticket: Ticket):
        if ticket.category == "network":
            print(f"Network team: {ticket.message}")
        elif self.successor:
            self.successor.handle(ticket)


class UnknownSupport(SupportHandler):
    def handle(self, ticket: Ticket):
        print(f"Unknown category. No handler found: {ticket.message}")


# łańcuch

hw = HardwareSupport()
sw = SoftwareSupport()
net = NetworkSupport()
unk = UnknownSupport()

hw.set_next(sw)
sw.set_next(net)
net.set_next(unk)

# testy

t1 = Ticket("hardware", "Mouse not working")
t2 = Ticket("software", "App crash on launch")
t3 = Ticket("network", "WiFi not connecting")
t4 = Ticket("printer", "No toner!")

hw.handle(t1)
hw.handle(t2)
hw.handle(t3)
hw.handle(t4)
