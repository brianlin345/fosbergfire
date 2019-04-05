import math

class Region(object):
    def __init__(self, temperature, humidity, wind):
        self.temperature = temperature
        self.humidity = humidity
        self.wind = wind
        self.final = 0


    def castVariables(self):
        self.temperature = int(self.temperature)
        self.humidity = int(self.humidity)
        self.wind = int(self.wind)

    def calcEquilMoisture(self):
        if(int(self.humidity) <= 10):
            self.eqm = 0.03229 + (0.281073 * self.humidity) - (0.000578 * self.humidity * self.temperature)
        elif(int(self.humidity) <= 50):
            self.eqm = 2.22749 + (0.160107 * self.humidity) - (0.01478 * self.temperature)
        else:
            self.eqm = 21.0606 + (0.005565 * pow(self.humidity, 2)) - (0.00035 * self.humidity * self.temperature) - (0.483199 * self.humidity)

    def calcMoistureDampening(self):
        self.mdc = 1 - (2 * (self.eqm / 30)) + (1.5 * pow(self.eqm / 30, 2)) - (0.05 * pow(self.eqm / 30, 3))

    def calcFinal(self):
        self.final = (self.mdc * math.sqrt(1 + math.pow(self.wind, 2))) / 0.3002
        return self.final