# -*- coding: utf-8 -*-
import warnings
import random
import time

class ArduinoDock(object):
    def __init__(self, uart=None, baudRate=9600):
        """
        Mock Arduino Dock - no real hardware required.
        Generates random temperature and humidity readings.
        """
        self.is_open = True
        warnings.warn("Running in MOCK mode - no Arduino connected.")

    def send(self, message):
        """Pretend to send a message to Arduino Dock"""
        print("[MOCK] Sent to Arduino:", message)

    def read_line(self):
        """Return fake sensor readings"""
        # Simulate a delay like a real serial read
        time.sleep(1)
        temp = round(random.uniform(20, 30), 1)  # C
        hum = round(random.uniform(40, 70), 1)   # %
        return "TEMP:{},HUM:{}".format(temp, hum)

    def close(self):
        """Close mock port"""
        self.is_open = False
        print("[MOCK] Serial port closed")
