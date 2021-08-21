import pyautogui as pg
from time import sleep

sleep(4)

toopen = input("Enter the name of the file : ")
speed = float(input("enter the speed of writing :"))
f = open(toopen)
txt = f.read()

sleep(3)
pg.typewrite(txt,speed)