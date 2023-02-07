from Observer import IListener


class PressureListener(IListener):
    prev_val = ""

    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        val = event.split(",")[0]
        if self.prev_val != val:
            self.prev_val = val
            print(f"Current Barometric Pressure is {val} atms.")


class TemperatureListener(IListener):
    prev_val = ""

    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        val = event.split(",")[1]
        if self.prev_val != val:
            self.prev_val = val
            print(f"Current Temperature is {val} degrees.")


class WindListener(IListener):
    prev_val = ""

    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        val = event.split(",")[2]
        if self.prev_val != val:
            self.prev_val = val
            print(f"Current Wind Direction is from the {val.capitalize()}.")
