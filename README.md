# Hot corner implementation on linux without gnome
Hot corners are define as x-axis = 0 or y-axis - 0 base on the mouse pointer cordinates. Upon registering the requirement coordinate of 0 (x-axis or y-axis), a shell script will executed. 

## Requirments 
- python3
- pynput module (for mouse evens)

## Installation
- specify the cmd1 (x-axis = 0) and cmd2 (y-axis = 0) in mouse.py
- make install will install the script mouse.py into .local/bin/mouse.py
- make install will copy systemd start file to the user systemd directory
