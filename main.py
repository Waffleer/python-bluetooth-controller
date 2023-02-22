import bluetooth  # install pybluez before importing
import struct
import binascii



class GLMxxC(object):
    device_name = ''
    socket = None
    port = 0x0005  # depends on model type
    bluetooth_address = None
    connected = False
    cmds = {
            'measure':          b'\xC0\x40\x00\xEE',
            'laser_on':         b'\xC0\x41\x00\x96',
            'laser_off':        b'\xC0\x42\x00\x1E',
            'backlight_on':     b'\xC0\x47\x00\x20',
            'backlight_off':    b'\xC0\x48\x00\x62'
        }

    status = {
            0:  'ok',
            1:  'communication timeout',
            3:  'checksum error',
            4:  'unknown command',
            5:  'invalid access level',
            8:  'hardware error',
            10: 'device not ready',
        }

    #Initializing or Constructor
    def __init__(self, bluetooth_address=None):
        if bluetooth_address is None:
            self.find_GLMxxC()
        else:
            self.bluetooth_address = bluetooth_address
        self.connect()
    #Finding the available bluetooth devices
    def find_GLMxxC(self):
        print('Searching for BOSCH GLMxxC ...')

        nearby_devices = bluetooth.discover_devices(
            duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
            
        for index, val in enumerate(nearby_devices):
                addr, name = val
                if 'BOSCH GLM' in name.upper():
                    self.bluetooth_address = addr
                    print('Found ', name.upper(), ' @', self.bluetooth_address)
                    self.device_name = name.upper()
                    if 'GLM50' in self.device_name:
                        self.port = 5
                    return

    def connect(self):
        try:
            self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.socket.connect((self.bluetooth_address, self.port))
            self.connected = True
        except:
            self.socket.close()
            self.conencted = False












