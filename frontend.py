from backend import SmartHome, SmartPlug, SmartWashingMachine
from tkinter import *

"""
Global variables that include: backend manager, Tkinter window
"""
smartHome = SmartHome()
mainWin = Tk()
# This variables stores the labels for each device and the number of currently active devices (in index 0)
deviceLabels = []

WINDOWDEFAULTS = [650, 400]
"""
Start of the function library for the frontend of the coursework 
"""
def setupHome():

    for i in range(2):
        smartHome.addDevice(SmartPlug())

    for i in range(3):
        smartHome.addDevice(SmartWashingMachine())

""" These functions are used to turn off and on all the devices in the smart home """
def turnoffAllDevices():
    smartHome.turnoffAllDevices()
    updateGUI()

def turnonAllDevices():
    smartHome.turnonAllDevices()
    updateGUI()

""" These functions are used to create the GUI elements"""
def createTopLine():

    # Main title
    titleLabel = Label(mainWin, text="Smart Home", font=("TkDefaultFont", 20, "bold"))
    titleLabel.grid(row=0, column=1, columnspan=2)

    # Global buttons for all devices
    switchOffAllButton = Button(mainWin, text="Switch Off All", command=turnoffAllDevices)
    switchOffAllButton.grid(row=1, column=0)

    switchOnAllButton = Button(mainWin, text="Switch On All", command=turnonAllDevices)
    switchOnAllButton.grid(row=2, column=0)

def createDevices():
    """ This function creates both the labels and buttons for each device """
    height = (len(smartHome.getDevices()) * 30) + 150
    mainWin.geometry(f"{WINDOWDEFAULTS[0]}x{height}")

    for i in range(len(smartHome.getDevices())):

        # Anonymous function for toggling a given device
        def toggleDevice(index=i):
            device = smartHome.getDeviceat(index)
            device.toggleSwitch()

            updateGUI()

        def customiseDevice(index=i):
            """ This function is responsible for creating a new window that will allow the user to customise the device """
            device = smartHome.getDeviceat(index)

            customiseWin = Toplevel(mainWin)
            customiseWin.title("Customise Device")

            customiseTitle = Label(customiseWin, text="Customise Device",font=("TkDefaultFont", 20, "bold"))
            customiseTitle.grid(row=0, column=1, columnspan=2)

            # Handle customisation differently for each device type
            if type(device) == SmartPlug:
                
                consumptionLabel = Label(customiseWin, text="Consumption (W):")
                consumptionLabel.grid(row=1, column=0)

                consumptionEntry = Entry(customiseWin)
                consumptionEntry.insert(0, device.getConsumptionRate())
                consumptionEntry.grid(row=1, column=1)

                def confirmConsumption(d=device):
                    device.setConsumptionRate(consumptionEntry.get())
                    customiseWin.destroy()
                    updateGUI()

                confirmButton = Button(customiseWin, text="Confirm", command=confirmConsumption)
                confirmButton.grid(row=1, column=2)

            else:
                
                washModeTitleLabel = Label(customiseWin, text="Wash Mode:")
                washModeTitleLabel.grid(row=1, column=0)

                for index in range(len(device.getWashModes())):
                    
                    def confirmWashMode(washMode=index):
                        device.setWashModeAt(washMode)
                        updateGUI()
                    
                    washModeLabel = Label(customiseWin, text=device.getWashModeAt(index))
                    washModeLabel.grid(row=index + 2, column=1)

                    washModeConfirmButton = Button(customiseWin, text="Confirm", command=confirmWashMode)
                    washModeConfirmButton.grid(row=index + 2, column=2)
            updateGUI()
        

        device = smartHome.devices[i]

        deviceLabel = Label(mainWin, text=str(device))
        deviceButton = Button(mainWin, text="Toggle this", command=toggleDevice)
        customiseDeviceButton = Button(mainWin, text="Customise", command=customiseDevice)
        deviceLabels.append(deviceLabel)

        deviceLabel.grid(row=i + 3, column=0)
        deviceButton.grid(row=i + 3, column=1)
        customiseDeviceButton.grid(row=i + 3, column=2)

def createBottomLine():
    """ This function creates the functionality for adding devices and removing devices from the smart home as well as displaying the number of active devices """
    
    activeDevicesCount = Label(mainWin, text=f"Active Devices: {smartHome.getNumOnDevices()}")
    activeDevicesCount.grid(row=len(smartHome.getDevices()) + 3, column=0)
    deviceLabels.append(activeDevicesCount)

    addDeviceButton = Button(mainWin, text="Add Device", command=addDeviceWindow)
    addDeviceButton.grid(row=len(smartHome.getDevices()) + 4, column=0)

    removeDeviceButton = Button(mainWin, text="Remove Device", command=removeDeviceWindow)
    removeDeviceButton.grid(row=len(smartHome.getDevices()) + 4, column=1)

# The windows that are needed for the challenge feature (7.5)
def addDeviceWindow():

    def addSmartPlug():
        smartHome.addDevice(SmartPlug())
        deleteGUI()
        setupGUI()
        updateGUI()

    def addSmartWasher():
        smartHome.addDevice(SmartWashingMachine())
        deleteGUI()
        setupGUI()
        updateGUI()

    addWin = Toplevel(mainWin)
    addWin.title("Add Device")
    addWin.resizable(False, False)

    addLabel = Label(addWin, text="Add Device", font=("TkDefaultFont", 20, "bold"))
    addLabel.grid(row=0, column=0, columnspan=2)

    # Add Smart Plug Functionality
    smartPlugLabel = Label(addWin, text="Smart Plug")
    smartPlugLabel.grid(row=1, column=0)
    smartPlugAddButton = Button(addWin, text="Add", command=addSmartPlug)
    smartPlugAddButton.grid(row=1, column=1)

    # Add Smart Washer Functionality
    smartWasherLabel = Label(addWin, text="Smart Washing Machine")
    smartWasherLabel.grid(row=2, column=0)
    smartWasherAddButton = Button(addWin, text="Add", command=addSmartWasher)
    smartWasherAddButton.grid(row=2, column=1)

def removeDeviceWindow():
    removeWin = Toplevel(mainWin)
    removeWin.title("Remove Device")
    removeWin.resizable(False, False)

    removeLabel = Label(removeWin, text="Remove Device", font=("TkDefaultFont", 20, "bold"))
    removeLabel.grid(row=0, column=0, columnspan=2)

    for index in range(len(smartHome.getDevices())):

        def removeDevice(index=index):
            smartHome.removeDeviceAt(index)
            deviceLabels.remove(deviceLabels[index])
            deleteGUI()
            setupGUI()
            updateGUI()

        device = smartHome.getDeviceat(index)

        deviceLabel = Label(removeWin, text=str(device))
        deviceLabel.grid(row=index + 1, column=0)

        removeButton = Button(removeWin, text="Remove", command=removeDevice)
        removeButton.grid(row=index + 1, column=1)

""" These function are used to manage the GUI and make sure it is up to date"""
def updateGUI():
    """ This function updates each label by configuring the text to be the string function of each device """
    for index in range(len(smartHome.getDevices())):

        device = smartHome.getDeviceat(index)
        deviceLabel = deviceLabels[index]
        deviceLabel.config(text=str(device))

    deviceLabels[-1].config(text=f"Active Devices: {smartHome.getNumOnDevices()}")

""" Main functions that are outlined in the coursework specification """
def setupGUI():
    """ The main setup function for the GUI """
    mainWin.title("Smart Home")
    mainWin.geometry(f"{WINDOWDEFAULTS[0]}x{WINDOWDEFAULTS[1]}")
    mainWin.resizable(False, False)

    createTopLine()
    createDevices()
    createBottomLine()

    mainWin.mainloop()

def deleteGUI():

    global deviceLabels
    deviceLabels = []
    for widget in mainWin.winfo_children():
        widget.destroy()

def main():
    """ Main function that is called to create both backend and frontend """
    setupHome()
    setupGUI()

main()