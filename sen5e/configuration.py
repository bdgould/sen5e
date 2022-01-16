#!/usr/bin/env python3

import json
import os.path


class Sensor:

    def __init__(self, payload):
        self.pin = int(payload['pin'])
        self.name = payload['name']


class InfluxConfig:

    def __init__(self, payload):
        self.url = payload['url']
        self.org = payload['org']
        self.bucket = payload['bucket']
        self.token = payload['token']


class Config:

    def __init__(self, location):
        assert os.path.isfile(location)
        self.sensors = []
        with open(location, 'r') as stream:
            self.config = json.load(stream)
        self.loopDelay = float(self.config['delay'])
        for sensor in self.config['sensors']:
            self.sensors.append(Sensor(sensor))
        self.influx = InfluxConfig(self.config['influxdb'])
