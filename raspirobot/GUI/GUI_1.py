from guizero import App
from guizero import MenuBar
from time import sleep

def gui_1():
  main_screen = App(title"Welcome to my Robot")
  sleep(2)
  def function_1():
    main_screen.full_screen = True
    return
  def function_2():
    home_page.full_screen = False
    return
  
  menu = MenuBar(main_screen,
                 toplevel=["File"],
                 options=[
                   [["Fullscreen", function_1], ["Exit Fullscreen", function_2]]
                 ])
  return

gui_1()
