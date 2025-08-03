from enum import IntEnum

MagneticStripeReaderPageId = 0x8E

class MagneticStripeReaderPage(IntEnum):
    Undefined                               = 0x00
    MSRDeviceReadOnly                       = 0x01
    __Reserved0_Begin                       = 0x02
    __Reserved0_End                         = 0x10
    Track1Length                            = 0x11
    Track2Length                            = 0x12
    Track3Length                            = 0x13
    TrackJISLength                          = 0x14
    __Reserved1_Begin                       = 0x15
    __Reserved1_End                         = 0x1F
    TrackData                               = 0x20
    Track1Data                              = 0x21
    Track2Data                              = 0x22
    Track3Data                              = 0x23
    TrackJISData                            = 0x24
    __Reserved2_Begin                       = 0x25
    __Reserved2_End                         = 0xFFFF

