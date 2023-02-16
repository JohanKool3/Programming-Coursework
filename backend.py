# The file that holds the backend code for the coursework

""" 
    Beginning of the class library for the backend.
"""
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


testSmartWashingMachine()
