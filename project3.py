from time import sleep
import picamera
from mcpi import minecraft

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    if pos.x == -7.0:
        mc.postToChat("SMILE :)")
        with picamera.PiCamera() as camera:
            camera.resolution = 1920, 1080
            camera.saturation = 50
            camera.brightness = 50
            camera.start_preview()
            sleep(5)
            camera.capture("/home/pi/Desktop/image.jpg")
            camera.stop_preview()
            sleep(5)
    
