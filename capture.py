from gpiozero import Button
from picamera import PiCamera
import datetime
import storeFileFB

button = Button(22)
camera = PiCamera

camera.start_preview()
frame = 1
while True:
  button.wait_for_press()
  fileLoc = f'/home/pi/images/frame{frame}.jpg'
  currentTime = datetime.datetime.now()strftime("%d/%m/%Y %H:%M:%S")
  
  camera.capture(fileLoc)
  print(f'frame {frame} taken at {currentTime}')
  storeFileFB.store_file(fileLoc)
  storeFileFB.push_db(fileLoc, currentTime)
  print('Image stored')
  frame += 1
  camera.close()
