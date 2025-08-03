from enum import IntEnum


class VRControlsPage(IntEnum):
    Undefined                               = 0x00
    Belt                                    = 0x01
    BodySuit                                = 0x02
    Flexor                                  = 0x03
    Glove                                   = 0x04
    HeadTracker                             = 0x05
    HeadMountedDisplay                      = 0x06
    HandTracker                             = 0x07
    Oculometer                              = 0x08
    Vest                                    = 0x09
    AnimatronicDevice                       = 0x0A
    __Reserved0_Begin                       = 0x0B
    __Reserved0_End                         = 0x1F
    StereoEnable                            = 0x20
    DisplayEnable                           = 0x21
    __Reserved1_Begin                       = 0x22
    __Reserved1_End                         = 0xFFFF

