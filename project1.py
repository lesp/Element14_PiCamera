from time import sleep
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = 1920, 1080
    camera.saturation = 50
    camera.brightness = 50
    camera.start_preview()
    sleep(5)
    camera.capture("/home/pi/Desktop/image.jpg")
    camera.stop_preview()
    
