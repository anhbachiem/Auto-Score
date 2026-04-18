import RPi.GPIO as GPIO
from config import CONTROLLER_GPIO_PINS

class GPIOHandler:
    def __init__(self, callback=None):
        self.callback = callback
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for button_name, pin in CONTROLLER_GPIO_PINS.items():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(pin, GPIO.RISING, callback=self._on_button_press, bouncetime=200)

    def _on_button_press(self, channel):
        if self.callback:
            button_name = self._get_button_name(channel)
            self.callback(button_name, channel)

    def _get_button_name(self, pin):
        for button_name, button_pin in CONTROLLER_GPIO_PINS.items():
            if button_pin == pin:
                return button_name
        return None

    def cleanup(self):
        GPIO.cleanup()