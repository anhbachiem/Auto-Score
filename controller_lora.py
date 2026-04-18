import serial
import time

class LoraHandler:
    def __init__(self, port='/dev/ttyAMA0', baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        time.sleep(2)  # Allow time for the serial connection to initialize

    def send_command(self, command):
        if self.ser.isOpen():
            self.ser.write(f'{command}\n'.encode())
            print(f'Sent: {command}')
        else:
            print('Serial port is not open.')

    def receive_coordinates(self):
        coordinates = None
        if self.ser.isOpen():
            if self.ser.in_waiting > 0:
                coordinates = self.ser.readline().decode().strip()
                print(f'Received: {coordinates}')
        else:
            print('Serial port is not open.')
        return coordinates

    def close(self):
        if self.ser.isOpen():
            self.ser.close()
            print('Closed serial connection.')
