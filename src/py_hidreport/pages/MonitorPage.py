from enum import IntEnum

MonitorPageId = 0x80

class MonitorPage(IntEnum):
    Undefined                               = 0x00
    MonitorControl                          = 0x01
    EDIDInformation                         = 0x02
    VDIFInformation                         = 0x03
    VESAVersion                             = 0x04
    __Reserved0_Begin                       = 0x05
    __Reserved0_End                         = 0xFFFF

    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

