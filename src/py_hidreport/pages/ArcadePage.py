from enum import IntEnum

ArcadePageId = 0x91

class ArcadePage(IntEnum):
    Undefined                               = 0x00
    GeneralPurposeIOCard                    = 0x01
    CoinDoor                                = 0x02
    WatchdogTimer                           = 0x03
    __Reserved0_Begin                       = 0x04
    __Reserved0_End                         = 0x2F
    GeneralPurposeAnalogInputState          = 0x30
    GeneralPurposeDigitalInputState         = 0x31
    GeneralPurposeOpticalInputState         = 0x32
    GeneralPurposeDigitalOutputState        = 0x33
    NumberofCoinDoors                       = 0x34
    CoinDrawerDropCount                     = 0x35
    CoinDrawerStart                         = 0x36
    CoinDrawerService                       = 0x37
    CoinDrawerTilt                          = 0x38
    CoinDoorTest                            = 0x39
    __Reserved1_Begin                       = 0x3A
    __Reserved1_End                         = 0x3F
    CoinDoorLockout                         = 0x40
    WatchdogTimeout                         = 0x41
    WatchdogAction                          = 0x42
    WatchdogReboot                          = 0x43
    WatchdogRestart                         = 0x44
    AlarmInput                              = 0x45
    CoinDoorCounter                         = 0x46
    IODirectionMapping                      = 0x47
    SetIODirectionMapping                   = 0x48
    ExtendedOpticalInputState               = 0x49
    PinPadInputState                        = 0x4A
    PinPadStatus                            = 0x4B
    PinPadOutput                            = 0x4C
    PinPadCommand                           = 0x4D
    __Reserved2_Begin                       = 0x4E
    __Reserved2_End                         = 0xFFFF

    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)