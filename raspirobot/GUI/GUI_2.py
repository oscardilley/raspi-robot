# second attempt at a robot GUI, trying to get the camera preview to import

from guizero import App
from guizero import MenuBar
from time import sleep
from picamera import PiCamera

def gui_2():
  main_screen = App(title="Raspi-Robot")
  def function_1():
    main_screen.full_screen = True
    return
  def function_2():
    main_screen.full_screen = False
    return
  
  menu = MenuBar(main_screen,
                 toplevel=["File"],
                 options=[
                   [["Fullscreen", function_1], ["Exit Fullscreen", function_2]]
                 ])
  
  camera = PiCamera()
  camera.start_preview()
  sleep(5)
  camera.stop_preview()
  
  main_screen.display()
  return

gui_2()

