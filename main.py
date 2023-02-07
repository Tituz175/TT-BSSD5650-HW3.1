from Observer import Subject, IListener
from WeatherData import *


class WeatherTower(Subject):
    def getUserAction(self):
        prompt = "Enter Pressure, Temperature, and Wind Direction separated by a comma."
        self.data = input(prompt)
        return self.data



if __name__ == "__main__":
    # make a subject object to spy on
    subject = WeatherTower()

    listenerT = TemperatureListener("Temp", subject)

    listenerP = PressureListener("Press", subject)

    listenerW = WindListener("Wind", subject)


    action = subject.getUserAction()
    subject.notify_listeners(action)

    action = subject.getUserAction()
    subject.notify_listeners(action)

    action = subject.getUserAction()
    subject.notify_listeners(action)

