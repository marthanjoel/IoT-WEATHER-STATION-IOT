# -*- coding: utf-8 -*-
import warnings
from arduinoDockHelper import ArduinoDock

# Initialize ArduinoDock (mock mode will be used if no real hardware)
arduinoDock = ArduinoDock()

def get_sensor_data():
    """
    Reads a line from ArduinoDock and parses it into temperature & humidity.
    Returns a dictionary: {"temperature": float, "humidity": float}
    """
    try:
        line = arduinoDock.read_line()
        if line:
            # Example line: "TEMP:25.7,HUM:62.3"
            parts = line.split(",")
            temp = float(parts[0].split(":")[1])
            hum = float(parts[1].split(":")[1])
            return {"temperature": temp, "humidity": hum}
        else:
            warnings.warn("No data received from ArduinoDock.")
            return None
    except Exception as e:
        warnings.warn("Failed to parse sensor data: {}".format(e))
        return None

def send_command(cmd):
    """
    Send a command to ArduinoDock.
    (Mock mode just prints it to console)
    """
    try:
        arduinoDock.send(cmd)
    except Exception as e:
        warnings.warn("Failed to send command: {}".format(e))
