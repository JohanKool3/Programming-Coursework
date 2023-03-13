from backend import SmartHome, SmartPlug, SmartWashingMachine
from tkinter import *

""" Global variables that include: backend manager, Tkinter window """
smartHome = SmartHome()
mainWin = Tk()
# This variables stores the labels for each device and the number of currently active devices (in index 0)
deviceLabels = []

# Constants
WINDOWDEFAULTS = [650, 400]

""" Start of the function library for the frontend of the coursework """
def setupHome():
    """ This function is responsible for setting up the smart home with the default devices outined in task 4 """

    for i in range(2):
        smartHome.addDevice(SmartPlug())

    for i in range(3):
        smartHome.addDevice(SmartWashingMachine())

def turnoffAllDevices():
    """ Turns off all the devices in the 'smartHome' object """
    smartHome.turnoffAllDevices()
    updateGUI()

def turnonAllDevices():
    """ Turns on all the devices in the 'smartHome' object """
    smartHome.turnonAllDevices()
    updateGUI()


""" These functions are used to create the GUI elements"""
def createTopLine():
    """ Creates the header information for the GUI"""

    # Main title
    titleLabel = Label(mainWin, text="Smart Home", font=("TkDefaultFont", 20, "bold"))
    titleLabel.grid(row=0, column=0, columnspan=2)

    # Exit button
    exitButton = Button(mainWin, text="Exit", command=quit)
    exitButton.grid(row=0, column=1)

    # Global buttons for all devices
    switchOffAllButton = Button(mainWin, text="Switch Off All", command=turnoffAllDevices)
    switchOffAllButton.grid(row=1, column=0)

    switchOnAllButton = Button(mainWin, text="Switch On All", command=turnonAllDevices)
    switchOnAllButton.grid(row=2, column=0)

def createDevices():
    """ This function creates both the labels and buttons for each device in the 'smartHome' object """

    height = (len(smartHome.getDevices()) * 30) + 150
    mainWin.geometry(f"{WINDOWDEFAULTS[0]}x{height}")

    for i in range(len(smartHome.getDevices())):

        # Anonymous function for toggling a given device
        def toggleDevice(index=i):
            device = smartHome.getDeviceat(index)
            device.toggleSwitch()
            updateGUI()

        def customiseDevice(index=i):
            customiseWindow(index)

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

# The windows here are responsible for the challenge features
def addDeviceWindow():
    """ This function is responsible for creating a window that allows the user to add a new device """

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
    """ This function is responsible for creating a window that allows the user to remove a device """

    removeWin = Toplevel(mainWin)
    removeWin.title("Remove Device")
    removeWin.resizable(False, False)

    removeLabel = Label(removeWin, text="Remove Device", font=("TkDefaultFont", 20, "bold"))
    removeLabel.grid(row=0, column=0, columnspan=2)

    for index in range(len(smartHome.getDevices())):

        def removeDevice(index=index):
            removeWin.destroy()
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

def customiseWindow(index):
    """ This function is responsible for creating a new window that will allow the user to customise the device """

    # Device that is being customised
    device = smartHome.getDeviceat(index)

    # GUI setup and generation
    customiseWin = Toplevel(mainWin)
    customiseWin.title("Customise Device")
    customiseWin.resizable(False, False)

    customiseTitle = Label(customiseWin, text="Customise Device",font=("TkDefaultFont", 20, "bold"))
    customiseTitle.grid(row=0, column=0, columnspan=2)

    # Handle customisation differently for each device type

        
    consumptionLabel = Label(customiseWin, text="Consumption (W):")
    consumptionLabel.grid(row=1, column=0)

    consumptionEntry = Entry(customiseWin)
    consumptionEntry.insert(0, device.getConsumptionRate())
    consumptionEntry.grid(row=1, column=1)

    def confirmConsumption(d=device):
        """ This anonymous function is responsible for confirming the new consumption rate for the device """

        # Error handling for invalid data types
        try:
            newConsumptionRate = int(consumptionEntry.get())

            # Error catching for out of bounds values
            if  not (0 <= newConsumptionRate <=150):
                errorLabel.config(text=f"Value {newConsumptionRate} is out of bounds, please enter a number between 0 and 150")
            else:
                device.setConsumptionRate(consumptionEntry.get())
                customiseWin.destroy()
                updateGUI()

        except:
            newConsumptionRate = consumptionEntry.get()
            errorLabel.config(text=f"Value {newConsumptionRate} is not Valid, please enter a number between 0 and 150")
            

    confirmButton = Button(customiseWin, text="Confirm", command=confirmConsumption)
    confirmButton.grid(row=1, column=2)

    if type(device) == SmartWashingMachine:
        
        washModeTitleLabel = Label(customiseWin, text="Wash Mode:")
        washModeTitleLabel.grid(row=2, column=0)

        for index in range(len(device.getWashModes())):
            
            def confirmWashMode(washMode=index):
                """ This anonymous function is responsible for confirming the new wash mode for the device """
                device.setWashModeAt(washMode)
                customiseWin.destroy()
                updateGUI()
            
            washModeLabel = Label(customiseWin, text=device.getWashModeAt(index))
            washModeLabel.grid(row=index + 2, column=1)

            washModeConfirmButton = Button(customiseWin, text="Confirm", command=confirmWashMode)
            washModeConfirmButton.grid(row=index + 2, column=2)

    errorLabel = Label(customiseWin, text="")
    errorLabel.grid(row=100, column=0, columnspan=3)
    updateGUI()


""" These function are used to manage the GUI and make sure it is up to date"""
def updateGUI():
    """ This function updates each label by configuring the text to be the string function of each device """

    # Check in place as to allow the GUI to be closed without an error occurring
    if len(deviceLabels) > 0:

        for index in range(len(smartHome.getDevices())):

            device = smartHome.getDeviceat(index)
            deviceLabel = deviceLabels[index]
            deviceLabel.config(text=str(device))

        deviceLabels[-1].config(text=f"Active Devices: {smartHome.getNumOnDevices()}")

def quit():
    """ This function is used for the quit button at the top of the GUI """
    deleteGUI()
    mainWin.destroy()


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
    """ This function removes all widgets from the GUI and resets the deviceLabels list """

    global deviceLabels
    deviceLabels = []
    for widget in mainWin.winfo_children():
        widget.destroy()

def main():
    """ Main function that is called to create both backend and frontend """

    setupHome()
    setupGUI()

main()