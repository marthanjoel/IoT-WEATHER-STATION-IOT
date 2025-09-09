##**🌡️ IoT Weather Station**
An IoT Weather Station simulation built with Python (Tkinter GUI).
It reads temperature and humidity values (via a mocked Arduino dock helper), displays them on a desktop interface, and can be extended to integrate with real IoT hardware or cloud platforms.


##**⚙️ Setup Steps**
Clone the repository
git clone https://github.com/marthanjoel/IoT-WEATHER-STATION-IOT.git
cd IoT-WEATHER-STATION-IOT

Install Python 3 and Tkinter
sudo apt update
sudo apt install python3 python3-tk -y

Run the application
python3 gui.py
A GUI window will open showing live updates of temperature and humidity.


##**🚧 Challenges Faced**
1.Handling mocked sensor data when no physical hardware was available.

2.Getting Tkinter GUI to refresh smoothly in a background thread.

3.Managing git remotes and pushing to the correct repository.

4.Excluding unnecessary files (.pyc) that were automatically generated.


##**🔍 How the Simulation Works**
The arduinoDockHelper.py script simulates a connection to an Arduino device.

The helpers.py script fetches sensor data and allows sending commands.

The gui.py script creates a Tkinter-based dashboard that shows:

**🌡️ Temperature (°C)**

**💧 Humidity (%)**

The values update every 2 seconds in real-time.


##**🛠️ Sensors or Devices Emulated**
DHT11/DHT22-like Temperature & Humidity Sensor (simulated).

Arduino Dock (simulated with Python helper functions).

Future integration can be done with real Arduino + MQTT/IBM Watson IoT.

##**🚀 Ideas for Future Improvements**
Connect to a real Arduino board and read live sensor data.

Publish readings to an MQTT broker (e.g., Mosquitto, HiveMQ).

Integrate with cloud dashboards like IBM Watson IoT, ThingsBoard, or Node-RED.

Add more sensors:

🌬️ Wind speed,

🌞 Light intensity,

🌧️ Rain detector,

Save logs to a database or CSV for historical analysis.


<img width="756" height="531" alt="Screenshot from 2025-09-09 04-01-55" src="https://github.com/user-attachments/assets/9417bed7-6501-47c2-8ae8-82537988cec8" />


Add mobile/web dashboard alongside Tkinter GUI.
