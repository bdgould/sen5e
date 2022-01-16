#!/usr/bin/env python3


# import Adafruit_DHT


class Reading:

    def __init__(self, sensor_name, humidity, temperature):
        self.sensor_name = sensor_name
        self.humidity = humidity
        self.celsius = temperature
        self.fahrenheit = (temperature * 1.8) + 32


class Sensor22:

    def __init__(self, pin, name):
        self.pin = pin
        self.name = name

    def sense(self):
        # humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin)
        humidity, temperature = 0, 0
        if humidity is not None and temperature is not None:
            return Reading(self.name, humidity, temperature)
        else:
            raise IOError from None
