# The file that holds the backend code for the coursework

""" 
    Beginning of the class library for the backend.
"""
class SmartHome(object):

    """
    A class that represents a smart home.
    """
    def __init__(self):
        self.devices = []

    def __str__(self):
        output = "Smart Home: \n"

        for index in range(len(self.devices)):
            output += f" {index + 1}. {self.devices[index]} \n"

        return output

    def addDevice(self, device):
        self.devices.append(device)

    def getDevices(self):
        return self.devices

    def getDeviceat(self, index):
        return self.devices[index]

    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()

    def turnoffAllDevices(self):
        for device in self.devices:

            if device.getSwitchState():
                device.toggleSwitch()

    def turnonAllDevices(self):
        for device in self.devices:

            if not device.getSwitchState():
                device.toggleSwitch()


class SmartPlug(object):
    """ 
    A class that represents a simple smart plug.
    """
    def __init__(self):
        self.switchedOn = False
        self.consumptionRate = 0

    def __str__(self):

        switchStatus = "On"
        if not self.switchedOn:
            switchStatus = "Off"

        output = f"Smart Plug: {switchStatus} | Consumption Rate: {self.consumptionRate}"
        return output

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchState(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, rate):

        if 0 <= rate <= 150:
            self.consumptionRate = rate

        else:
            print("Invalid consumption rate, must be between 0 and 150.")


class SmartWashingMachine(object):

    def __init__(self):

        self.switchedOn = False
        self.washModes = ["Daily wash", "Quick wash", "Eco"]
        self.washMode = self.washModes[0]

    def __str__(self):
        switchStatus = "On"

        if not self.switchedOn:
            switchStatus = "Off"

        output = f"Smart Washing Machine: {switchStatus} | Wash Mode: {self.washMode}"

        return output
    
    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def setWashMode(self, mode):
        if mode in self.washModes:
            self.washMode = mode
        else:
            print("Invalid wash mode.")

    def getSwitchState(self):
        return self.switchedOn
    
    def getWashMode(self):
        return self.washMode

    
"""
    Beginning of the function library for the backend.
"""
def testSmartPlug():

    plug = SmartPlug()
    plug.toggleSwitch()
    print(plug.getSwitchState())

    print(plug.getConsumptionRate())
    plug.setConsumptionRate(100)
    print(plug.getConsumptionRate())

    print(plug)

def testSmartWashingMachine():
    
        machine = SmartWashingMachine()
        machine.toggleSwitch()
        print(machine.getSwitchState())
    
        print(machine.getWashMode())
        machine.setWashMode("Eco")
        print(machine.getWashMode())
    
        print(machine)


def testSmartHome():

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

# testSmartHome()
