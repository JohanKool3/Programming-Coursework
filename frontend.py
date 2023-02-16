from backend import SmartHome, SmartPlug, SmartWashingMachine
from tkinter import *

SMARTHOME = SmartHome()
mainWin = Tk()

def setupHome():

    for i in range(2):
        SMARTHOME.addDevice(SmartPlug())

    for i in range(3):
        SMARTHOME.addDevice(SmartWashingMachine())

def setupGUI():
    
    mainWin.title("Smart Home")
    mainWin.geometry("800x600")

    # Create switch off and switch on all buttons
    switchOffAllButton = Button(mainWin, text="Switch Off All", command=SMARTHOME.turnoffAllDevices)
    switchOffAllButton.grid(row=0, column=0)

    switchOnAllButton = Button(mainWin, text="Switch On All", command=SMARTHOME.turnonAllDevices)
    switchOnAllButton.grid(row=1, column=0)

    # Create toggle switch for each device
    for i in range(len(SMARTHOME.devices)):

        device = SMARTHOME.devices[i]
        deviceLabel = Label(mainWin, text=str(device))
        deviceLabel.grid(row=i + 2, column=0)

        deviceSwitch = Button(mainWin, text="Toggle Device", command=device.toggleSwitch)
        deviceSwitch.grid(row=i + 2, column=1)

    mainWin.mainloop()
def main():
    setupHome()
    setupGUI()

main()