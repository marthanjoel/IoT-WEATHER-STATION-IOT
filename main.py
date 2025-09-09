from helpers import get_sensor_data, send_command
import time

def main():
    print("IoT Weather Station (Mock Mode)")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            data = get_sensor_data()
            if data:
                print("Temperature: {} C | Humidity: {} %".format(
                    data["temperature"], data["humidity"]
                ))
            # Example: send a command every loop (optional)
            send_command("PING")
            time.sleep(2)  # wait 2 seconds between reads
    except KeyboardInterrupt:
        print("\nStopping Weather Station...")

if __name__ == "__main__":
    main()

