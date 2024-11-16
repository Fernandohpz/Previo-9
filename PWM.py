import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

diodo = GPIO.PWM (12, 50)
duty = 0
diodo.start (duty)

try:
    while True:
        duty+= 5
        if duty > 100;
                duty = 0
        diodo.ChangeDutyCycle(duty)
        time.sleep(0.05)
        
except keyboardInterrupt:
    print("Fin")
diodo.stop()
GPIO.Cleanup()