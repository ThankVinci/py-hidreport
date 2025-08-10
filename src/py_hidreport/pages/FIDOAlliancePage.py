from enum import IntEnum

FIDOAlliancePageId = 0xF1D0

# Fast IDentify Online Alliance page
class FIDOAlliancePage(IntEnum):
    Undefined                               = 0x00
    U2FAuthenticatorDevice                  = 0x01
    __Reserved0_Begin                       = 0x02
    __Reserved0_End                         = 0x1F
    InputReportData                         = 0x20
    OutputReportData                        = 0x21
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

