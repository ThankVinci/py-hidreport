from enum import IntEnum


class CameraControlPage(IntEnum):
    Undefined                               = 0x00
    __Reserved0_Begin                       = 0x01
    __Reserved0_End                         = 0x1F
    CameraAutofocus                         = 0x20
    CameraShutter                           = 0x21
    __Reserved1_Begin                       = 0x22
    __Reserved1_End                         = 0xFFFF

