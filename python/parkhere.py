from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import tkinter as tk
import time

A = 0
B = 1
DOT = 2
FULL = 3
PARKED = 0
FREE = 1
RESERVED = 2
NO = 0
YES = 1


devs = find_mcu_boards()

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

board = McuWithPeriBoard(devs[0])
print("*** Practicum board found")
print("*** Manufacturer: %s" % \
        board.handle.getString(board.device.iManufacturer, 256))
print("*** Product: %s" % \
        board.handle.getString(board.device.iProduct, 256))

def set_image(i):
    display_image = image_list[i]
    park_lot.configure(image = display_image)
    park_lot.image = display_image

def explore_park():
    count_space = 0
    for i in range (2):
        light_array[i] = board.getLight(pin_array[i])
        print('light from channel %d : %d'%(pin_array[i],light_array[i]))
        if light_array[i] > 400:
            if(park_status[i] < FREE):
                park_status[i] = FREE
            elif park_status[i] is FREE:
                count_space += 1
        else:
            park_status[i] = PARKED
        
    return count_space != 0

def determine_park():
    for i in range (2):
        if park_status[i] is FREE:
            print('choose %d' %(i))
            park_status[i] = RESERVED
            set_image(i)
            return


def board_logic(state):
    print(state)
    switch = board.getSwitch()
    time.sleep(0.1)
    isParkFree = explore_park()
    if isParkFree:
        if state is NO:
            if switch is True:
                state = YES
                print('switch state: ',state)
                if isParkFree:
                    determine_park()
            else:
                state = NO
                set_image(DOT)
                print('switch state: ',state)
        else:
            if switch is False:
                state = NO
    else:
        set_image(FULL)
    print('park-status: ' + (str)(park_status[0]) + '   ' + (str)(park_status[1]))
    root.after(100, lambda x = state : board_logic(x))

global state
state = NO
pin_array = [0,2]
light_array = [800, 800]
park_status = [FREE, FREE]
root = tk.Tk()
root.title("ParkHere")
root.geometry("530x530")
image_list =    [tk.PhotoImage(file= "./picture/a.png"),
                tk.PhotoImage(file= "./picture/b.png"),
                tk.PhotoImage(file= "./picture/dot.png"),
                tk.PhotoImage(file= "./picture/full.png")]
park_lot = tk.Label(image= image_list[DOT])
park_lot.pack()
set_image(2)
board_logic(state)
root.mainloop()


