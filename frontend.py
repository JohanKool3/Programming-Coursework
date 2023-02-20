from backend import SmartHome, SmartPlug, SmartWashingMachine
from tkinter import *

"""
Global variables that include: backend manager, Tkinter window
"""
smartHome = SmartHome()
mainWin = Tk()

WINDOWDEFAULTS = [650, 400]


"""
Start of the function library for the frontend of the coursework 
"""
def setupHome():

    for i in range(2):
        smartHome.addDevice(SmartPlug())

    for i in range(3):
        smartHome.addDevice(SmartWashingMachine())


def dynamicUpdate():
    """
    This function is responsible for updating the GUI following a users actions
    """
    extraWidgets = 2
    mainWin.geometry(f"{WINDOWDEFAULTS[0]}x{(len(smartHome.devices)+ extraWidgets) * 50 }")
    # Creation of the device list
    for i in range(len(smartHome.devices)):

        device = smartHome.devices[i]
        deviceLabel = Label(mainWin, text=str(device))
        deviceLabel.grid(row=i + 2, column=0)

        # Anonymous function that is used to toggle the value of a given device as well as update the GUI 
        def toggleDevice(d=device):
            d.toggleSwitch()
            dynamicUpdate()


        def customWindow(d=device):
            """This is the cusomization window that is used to change the settings of a given device"""


            customWindow = Toplevel()

            customWindow.geometry(f"{WINDOWDEFAULTS[0]}x{WINDOWDEFAULTS[1]}")
            customWindow.title(f"Customise {type(d).__name__}")

            #Title label
            titleLabel = Label(customWindow, text=f"Customise {type(d).__name__}")
            titleLabel.config(font=("TkDefaultFont", 20, "bold"))
            titleLabel.grid(row=0, column=0)

            # Exit button
            exitButton = Button(customWindow, text="Exit", command=customWindow.destroy)
            exitButton.grid(row=0, column=1)

            # Consumption customisation
            consumptionLabel = Label(customWindow, text=f"Consumption")
            consumptionLabel.grid(row=1, column=0)

            consumptionEntry = Entry(customWindow)
            consumptionEntry.insert(0, d.getConsumptionRate())
            consumptionEntry.grid(row=1, column=1)

            consumptionConfirm = Button(customWindow, text="Confirm", command=lambda: d.setConsumptionRate(consumptionEntry.get()))
            consumptionConfirm.grid(row=1, column=2)

            # Change washing cycle if it is a washing machine
            if isinstance(d, SmartWashingMachine):

                cycleLabel = Label(customWindow, text="Washing Cycle")
                cycleLabel.grid(row=2, column=0)



                for index in range(len(d.getWashModes())):

                    def updateCycleLabel():
                        cycleLabel = Label(customWindow, text=f"{index + 1}: {d.getWashModes()[index]}")
                        cycleLabel.grid(row=index + 3, column=0)

                        cycleButton = Button(customWindow, text="Select", command=lambda: d.setWashMode(index))
                        cycleButton.grid(row=index + 3, column=1)
                    updateCycleLabel()

            # Update the GUI
            dynamicUpdate()

        # For each device add device toggle buttons as well as customise buttons
        deviceSwitch = Button(mainWin, text="Toggle Device", command=toggleDevice)
        deviceSwitch.grid(row=i + 2, column=1)

        deviceCustomise = Button(mainWin, text="Customise Device", command=customWindow)
        deviceCustomise.grid(row=i + 2, column=2)

    
    # Create a label that displays the number of devices that are on and off
    numOnLabel = Label(mainWin, text=f"Number of devices on: {smartHome.getNumOnDevices()}")
    numOnLabel.grid(row=len(smartHome.devices) + 2, column=0)

    mainWin.update()

"""
These functions are used to turn off and on all the devices in the smart home as well as update the GUI
"""
def turnoffAllDevices():
    smartHome.turnoffAllDevices()
    dynamicUpdate()

def turnonAllDevices():
    smartHome.turnonAllDevices()
    dynamicUpdate()

def setupGUI():
    """ The main setup function for the GUI """
    mainWin.title("Smart Home")
    mainWin.geometry(f"{WINDOWDEFAULTS[0]}x{WINDOWDEFAULTS[1]}")
    mainWin.resizable(False, False)

    # Create switch off and switch on all buttons
    switchOffAllButton = Button(mainWin, text="Switch Off All", command=turnoffAllDevices)
    switchOffAllButton.grid(row=0, column=0)

    switchOnAllButton = Button(mainWin, text="Switch On All", command=turnonAllDevices)
    switchOnAllButton.grid(row=1, column=0)

    # Create toggle switch for each device
    dynamicUpdate()

    mainWin.mainloop()


def main():
    """ Main function that is called to create both backend and frontend """
    setupHome()
    setupGUI()

main()