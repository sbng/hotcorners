#!/usr/bin/env python3
from pynput import mouse
import os
import subprocess

cmd1 = '/home/sbng/.config/rofi/applets/applets/time.sh'
cmd2 = 'rofi -show window -window-format {w}{t} -theme /home/sbng/.config/rofi/launchers/misc/launchpad.rasi -pid /tmp/rofi.pid'

def on_move(x, y):
  if (x == 0) and (y == 0):
    p1 = subprocess.Popen(cmd1.split(), stderr=subprocess.DEVNULL)
    p2 = subprocess.Popen(cmd2.split(), stderr=subprocess.DEVNULL) 

with mouse.Listener( on_move=on_move) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was clicked'.format(e.args[0]))        
