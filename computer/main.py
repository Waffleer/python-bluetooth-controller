import serial
from time import sleep
from inputs import get_gamepad
import math
import threading

#XboxController Class for getting xbox controller inputs, might work with other controllers as well, not sure
#change the .read() function if you want more or less inputs

#What serial port your using
port = 'COM5'
serialPort = serial.Serial(port=port, baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, stopbits=1)
size = 1024

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this method
        ly = self.LeftJoystickY
        ry = self.RightJoystickY
        a = self.A
        b = self.B # b=1, x=2
        rt = self.RightTrigger
        lt = self.LeftTrigger
        return [ly, ry, a, b, rt, lt]


    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state


joy = XboxController()

#Sends data while true, stop program to break loop
while True:
    #Gets inputs from controller
    data = joy.read()

    #Smooths inputs from 1.0 to -1.0 float to -100 to 100 integer
    data[0] = (int) (data[0] *100)
    data[1] = (int) (data[1] *100)

    #changing analog trigger 0.0 to 1.0 inputs to digital 0-1
    if data[4] > 0 : data[4] = 1 
    else: data[4] = 0

    if data[5] > 0 : data[5] = 1 
    else: data[5] = 0



    #Creates send data ly,ry,a,b,rt,lt
    #Converts list to string without []
    data = str(data).strip("[]")
    #encodes and with ASCII
    sendData = f"{data}".encode("ASCII")
    #Sends data
    data = serialPort.write(sendData)

    #Optional Data print
    if data:
        print(sendData)

    #delays system from sending packets too fast, faster then .05 gives me an error on the pico end, change at your own risk
    sleep(.05)












