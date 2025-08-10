from enum import IntEnum

CameraControlPageId = 0x90

class CameraControlPage(IntEnum):
    Undefined                               = 0x00
    __Reserved0_Begin                       = 0x01
    __Reserved0_End                         = 0x1F
    CameraAutofocus                         = 0x20
    CameraShutter                           = 0x21
    __Reserved1_Begin                       = 0x22
    __Reserved1_End                         = 0xFFFF

    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

