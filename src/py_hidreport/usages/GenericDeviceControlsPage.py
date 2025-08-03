from enum import IntEnum


class GenericDeviceControlsPage(IntEnum):
    Undefined                               = 0x00
    Background_NonuserControls              = 0x01
    __Reserved0_Begin                       = 0x02
    __Reserved0_End                         = 0x1F
    BatteryStrength                         = 0x20
    WirelessChannel                         = 0x21
    WirelessID                              = 0x22
    DiscoverWirelessControl                 = 0x23
    SecurityCodeCharacterEntered            = 0x24
    SecurityCodeCharacterErased             = 0x25
    SecurityCodeCleared                     = 0x26
    SequenceID                              = 0x27
    SequenceIDReset                         = 0x28
    RFSignalStrength                        = 0x29
    SoftwareVersion                         = 0x2A
    ProtocolVersion                         = 0x2B
    HardwareVersion                         = 0x2C
    Major                                   = 0x2D
    Minor                                   = 0x2E
    Revision                                = 0x2F
    Handedness                              = 0x30
    EitherHand                              = 0x31
    LeftHand                                = 0x32
    RightHand                               = 0x33
    BothHands                               = 0x34
    __Reserved1_Begin                       = 0x35
    __Reserved1_End                         = 0x3F
    GripPoseOffset                          = 0x40
    PointerPoseOffset                       = 0x41
    __Reserved2_Begin                       = 0x42
    __Reserved2_End                         = 0xFFFF

