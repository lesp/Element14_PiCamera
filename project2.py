from time import sleep
import picamera
import RPi.GPIO as GPIO

button = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

while True:
    with picamera.PiCamera() as camera:
        camera.resolution = 1920, 1080
        camera.saturation = 50
        camera.brightness = 50
        GPIO.wait_for_edge(button,GPIO.FALLING)
        camera.start_preview()
        sleep(5)
        camera.capture("/home/pi/Desktop/image.jpg")
        camera.stop_preview()
