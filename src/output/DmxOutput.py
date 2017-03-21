"""DmxOutput handles the sending of a pattern's frame/state out through a DMX
connection. Wrapper around enttec_usb_dmx_pro.py

Functions:
    __init__: sets up module, opens resources
    close: closes all resources
    send: sends frame out through DMX

"""

from output.enttec_usb_dmx_pro import EnttecUsbDmxPro


class DmxOutput:
    def __init__(self, port):
        self._outputter = EnttecUsbDmxPro()
        self._port = port
        self._outputter.setPort(self._port)
        self._outputter.connect()

    def close(self, message):
        print('Closing DmxOutput {0}: {1}'.format(self._port, message))
        self._outputter.close()

    # Data is a list of length (9 boards) * (16 ch/board) = (144 ch)
    # where each element is the 8-bit value for that channel
    def send(self, data):
        self._outputter.sendDMX(data)
