import serial
import time
import json

class LoRaUARTHandler:
    def __init__(self, port='/dev/serial0', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        self.commands = {}  # Store commands

    def listen(self):
        while True:
            if self.ser.in_waiting > 0:
                command = self.ser.readline().decode('utf-8').strip()
                self.handle_command(command)

    def handle_command(self, command):
        if command in self.commands:
            response = self.commands[command]()
            self.send_response(response)
        else:
            self.send_response('Unknown command')

    def send_response(self, response):
        self.ser.write((response + '\n').encode('utf-8'))

    def add_command(self, command_name, command_handler):
        self.commands[command_name] = command_handler

    def example_handler(self):
        # Implement the logic to determine impact coordinates
        impact_coordinates = {'x': 10, 'y': 20}
        return json.dumps(impact_coordinates)

if __name__ == '__main__':
    lora_handler = LoRaUARTHandler()
    lora_handler.add_command('get_coordinates', lora_handler.example_handler)
    try:
        lora_handler.listen()
    except KeyboardInterrupt:
        print('Exiting...')
        lora_handler.ser.close()