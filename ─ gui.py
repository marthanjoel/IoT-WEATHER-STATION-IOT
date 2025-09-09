# -*- coding: utf-8 -*-
import tkinter as tk
import time
import threading
from helpers import get_sensor_data, send_command

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌡️ IoT Weather Station")
        self.root.geometry("300x150")

        # Labels
        self.temp_label = tk.Label(root, text="Temperature: -- °C", font=("Arial", 14))
        self.temp_label.pack(pady=10)

        self.hum_label = tk.Label(root, text="Humidity: -- %", font=("Arial", 14))
        self.hum_label.pack(pady=10)

        # Start background thread
        self.running = True
        threading.Thread(target=self.update_data, daemon=True).start()

    def update_data(self):
        while self.running:
            data = get_sensor_data()
            if data:
                self.temp_label.config(text=f"Temperature: {data['temperature']} °C")
                self.hum_label.config(text=f"Humidity: {data['humidity']} %")
                send_command("PING")
            time.sleep(2)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        app.stop()
