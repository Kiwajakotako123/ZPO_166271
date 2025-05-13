from abc import ABC, abstractmethod

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class Heater:
    def on(self):
        print("Heater is ON")

    def off(self):
        print("Heater is OFF")


class Command(ABC):
    @abstractmethod
    def execute(self): pass

class LightOn(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOff(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

class HeaterOn(Command):
    def __init__(self, heater: Heater):
        self.heater = heater

    def execute(self):
        self.heater.on()

class HeaterOff(Command):
    def __init__(self, heater: Heater):
        self.heater = heater

    def execute(self):
        self.heater.off()


class SmartHome:
    def __init__(self):
        self.history = []

    def run(self, command: Command):
        self.history.append(command)
        command.execute()


light = Light()
heater = Heater()
home = SmartHome()

home.run(LightOn(light))
home.run(HeaterOn(heater))
home.run(LightOff(light))
home.run(HeaterOff(heater))


from abc import ABC, abstractmethod

class App:
    def open_file(self): print("Opening file...")
    def write_text(self): print("Typing text...")
    def save_file(self): print("Saving file...")

class Command(ABC):
    @abstractmethod
    def execute(self): pass

class OpenCommand(Command):
    def __init__(self, app): self.app = app
    def execute(self): self.app.open_file()

class WriteCommand(Command):
    def __init__(self, app): self.app = app
    def execute(self): self.app.write_text()

class SaveCommand(Command):
    def __init__(self, app): self.app = app
    def execute(self): self.app.save_file()

class MacroRecorder:
    def __init__(self): self.commands = []

    def record(self, cmd: Command):
        self.commands.append(cmd)

    def playback(self):
        print("== Playback Macro ==")
        for cmd in self.commands:
            cmd.execute()


app = App()
macro = MacroRecorder()
macro.record(OpenCommand(app))
macro.record(WriteCommand(app))
macro.record(SaveCommand(app))
macro.playback()


from abc import ABC, abstractmethod
from collections import deque


class Command(ABC):
    @abstractmethod
    def execute(self): pass
    @abstractmethod
    def undo(self): pass


class GenerateReport(Command):
    def __init__(self): self.executed = False

    def execute(self):
        print("Generating report...")
        self.executed = True

    def undo(self):
        if self.executed:
            print("Undo report generation")
            self.executed = False

class SendEmail(Command):
    def __init__(self): self.executed = False

    def execute(self):
        print("Sending email...")
        self.executed = True

    def undo(self):
        if self.executed:
            print("Undo sending email")
            self.executed = False

class TaskQueue:
    def __init__(self): self.queue = deque()

    def add(self, cmd: Command):
        self.queue.append(cmd)

    def run_all(self):
        for cmd in self.queue:
            cmd.execute()

    def undo_last(self):
        if self.queue:
            last = self.queue.pop()
            last.undo()


queue = TaskQueue()
queue.add(GenerateReport())
queue.add(SendEmail())
queue.run_all()
queue.undo_last()
