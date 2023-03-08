# The file that holds the backend code for the coursework

""" 
    Beginning of the class library for the backend.
"""
class SmartHome(object):

    """ A class that represents a smart home. This is a manager class that holds a list of devices. """
    def __init__(self):
        """ Initialises the smart home with an empty list of devices """
        self.devices = []

    def __str__(self):
        """ This method returns a string representation of the smart home """
        output = "Smart Home: \n"

        for index in range(len(self.devices)):
            output += f" {index + 1}. {self.devices[index]} \n"

        return output

    def addDevice(self, device):
        """ Adds a device to the self.devices attribute """
        self.devices.append(device)

    def removeDeviceAt(self, index):
        """ Removes a device from the self.devices attribute with the parameter index """
        try:
            self.devices.pop(index)

        except ValueError:
            print("Invalid index.")

    def getDevices(self):
        """ Returns the list of devices in the smart home  """
        return self.devices

    def getNumOnDevices(self):
        """ Returns the number of devices that are on """
        numOn = 0

        for device in self.devices:
            if device.getSwitchState():
                numOn += 1

        return numOn

    def getNumOffDevices(self):
        """ This method returns the number of devices that are off """
        numOff = 0

        for device in self.devices:
            if not device.getSwitchState():
                numOff += 1

        return numOff

    def getDeviceat(self, index):
        """ Returns the device at a given index """
        return self.devices[index]

    def toggleSwitch(self, index):
        """ Toggles the switch of a device at a given index     """
        self.devices[index].toggleSwitch()

    def turnoffAllDevices(self):
        """ Turns off all devices in the smart home """
        for device in self.devices:

            if device.getSwitchState():
                device.toggleSwitch()

    def turnonAllDevices(self):
        """ Turns on all devices in the smart home"""
        for device in self.devices:

            if not device.getSwitchState():
                device.toggleSwitch()


class SmartPlug(object):
    
    """ A class that represents a simple smart plug. """
    def __init__(self):
        """ Initialises the smart plug with the attributes switchedOn set to False and consumptionRate to 0 """
        self.switchedOn = False
        self.consumptionRate = 0

    def __str__(self):
        """ Returns a string representation of the smart plug """
        switchStatus = "On"
        if not self.switchedOn:
            switchStatus = "Off"

        output = f"Smart Plug: {switchStatus} | Consumption Rate: {self.consumptionRate}"
        return output

    def toggleSwitch(self):
        """ Toggles the switchedOn attribute of the smart plug """
        self.switchedOn = not self.switchedOn

    def getSwitchState(self):
        """ Returns the switchedOn attribute of the smart plug """
        return self.switchedOn

    def getConsumptionRate(self):
        """ Returns the consumption rate of the smart plug """
        return self.consumptionRate

    def setConsumptionRate(self, rate):
        """ Sets the consumption rate of the smart plug, has validation to ensure the rate is between 0 and 150 """
        try:
            rate = int(rate)
            if 0 <= rate <= 150:
                self.consumptionRate = rate

            else:
                print("Invalid consumption rate, must be between 0 and 150.")

        except ValueError:
            print("Invalid consumption rate, must be an integer.")


class SmartWashingMachine(SmartPlug):

    """ A class that represents a smart washing machine. It inherits functionality from the SmartPlug class. """
    def __init__(self):
        """ Initialises the smart washing machine 
            1. Wash modes are stored in a list.
            2. The current wash mode is stored in the attribute washMode and is set to the first index by default.
            3. washModes contain all the wash modes that the washing machine can do. """
            
        super().__init__()
        self.washModes = ["Daily wash", "Quick wash", "Eco"]
        self.washMode = self.washModes[0]

    def __str__(self):
        """ Returns a string representation of the smart washing machine """
        switchStatus = "On"

        if not self.switchedOn:
            switchStatus = "Off"

        output = f"Smart Washing Machine: {switchStatus} | Wash Mode: {self.washMode}"

        return output

    def setWashMode(self, mode):
        """ Sets the washing mode if a valid mode is given """
        if mode in self.washModes:
            self.washMode = mode
        else:
            print("Invalid wash mode.")

    def setWashModeAt(self, index):
        """ Sets a washing mode at a given index if a valid index is given """
        try:
            if 0 <= index < len(self.washModes):
                self.washMode = self.washModes[index]
            else:
                print("Invalid wash mode.")

        except ValueError:
            print("Invalid index, must be an integer")
    
    def getWashMode(self):
        """ Returns the current wash mode """
        return self.washMode

    def getWashModeAt(self, index):
        """ Returns a wash mode at a given index if a valid index is given """
        try:
            if 0 <= index < len(self.washModes):
                return self.washModes[index]
            else:
                print("Invalid wash mode.")

        except ValueError:
            print("Invalid index, must be an integer")

    def getWashModes(self):
        """ Returns all wash modes """
        return self.washModes


""" Beginning of the function library for the backend. """
def testSmartPlug():
    """ A test function as outlined in task 1"""

    plug = SmartPlug()
    plug.toggleSwitch()
    print(plug.getSwitchState())

    print(plug.getConsumptionRate())
    plug.setConsumptionRate(100)
    print(plug.getConsumptionRate())

    print(plug)

def testDevice():
    """ A test function as outlined in task 2"""

    machine = SmartWashingMachine()
    machine.toggleSwitch()
    print(machine.getSwitchState())

    print(machine.getWashMode())
    machine.setWashMode("Eco")
    print(machine.getWashMode())

    print(machine)


def testSmartHome():
    """ A test function as outlined in task 3 """

    home = SmartHome()
    plug1 = SmartPlug()
    plug2 = SmartPlug()
    smWshMch = SmartWashingMachine()

    home.addDevice(plug1)
    home.addDevice(plug2)
    home.addDevice(smWshMch)

    plug2.toggleSwitch()
    plug2.setConsumptionRate(45)
    smWshMch.setWashMode("Quick wash")
    print(home)
    home.turnonAllDevices()
    print(home)


""" Below are the tests for the backend objects """
#1.
# testSmartPlug()

#2.
#testDevice()

#3.
#testSmartHome()
