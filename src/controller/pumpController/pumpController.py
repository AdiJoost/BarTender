import RPi.GPIO as GPIO
import time

class PumpController():

    def __init__(self, PIN: int) -> None:
        self.PIN = PIN
        self.setupBoard()

    def setupBoard(self) -> None:
        GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
        GPIO.setup(self.PIN, GPIO.OUT)  # Set pin as output

    def run(self) -> None:
        try:
            print("Turning on the pin...")
            GPIO.output(self.PIN, GPIO.HIGH)  # Turn the pin ON
            time.sleep(10)  # Keep it ON for 10 seconds
            print("Turning off the pin...")
            GPIO.output(self.PIN, GPIO.LOW)
        except:
            print("running failed")

    def cleanUp(self) -> None:
        GPIO.cleanup()
        print("cleanUp")