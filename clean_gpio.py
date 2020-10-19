import RPi.GPIO as GPIO

for pin in [2,3,4,17,27,22,10,9]:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
GPIO.cleanup()
