from enum import IntEnum

EyeandHeadTrackersPageId = 0x12

class EyeandHeadTrackersPage(IntEnum):
    Undefined                               = 0x00
    EyeTracker                              = 0x01
    HeadTracker                             = 0x02
    __Reserved0_Begin                       = 0x03
    __Reserved0_End                         = 0x0F
    TrackingData                            = 0x10
    Capabilities                            = 0x11
    Configuration                           = 0x12
    Status                                  = 0x13
    Control                                 = 0x14
    __Reserved1_Begin                       = 0x15
    __Reserved1_End                         = 0x1F
    SensorTimestamp                         = 0x20
    PositionX                               = 0x21
    PositionY                               = 0x22
    PositionZ                               = 0x23
    GazePoint                               = 0x24
    LeftEyePosition                         = 0x25
    RightEyePosition                        = 0x26
    HeadPosition                            = 0x27
    HeadDirectionPoint                      = 0x28
    RotationaboutXaxis                      = 0x29
    RotationaboutYaxis                      = 0x2A
    RotationaboutZaxis                      = 0x2B
    __Reserved2_Begin                       = 0x2C
    __Reserved2_End                         = 0xFF
    TrackerQuality                          = 0x100
    MinimumTrackingDistance                 = 0x101
    OptimumTrackingDistance                 = 0x102
    MaximumTrackingDistance                 = 0x103
    MaximumScreenPlaneWidth                 = 0x104
    MaximumScreenPlaneHeight                = 0x105
    __Reserved3_Begin                       = 0x106
    __Reserved3_End                         = 0x1FF
    DisplayManufacturerID                   = 0x200
    DisplayProductID                        = 0x201
    DisplaySerialNumber                     = 0x202
    DisplayManufacturerDate                 = 0x203
    CalibratedScreenWidth                   = 0x204
    CalibratedScreenHeight                  = 0x205
    __Reserved4_Begin                       = 0x206
    __Reserved4_End                         = 0x2FF
    SamplingFrequency                       = 0x300
    ConfigurationStatus                     = 0x301
    __Reserved5_Begin                       = 0x302
    __Reserved5_End                         = 0x3FF
    DeviceModeRequest                       = 0x400
    __Reserved6_Begin                       = 0x401
    __Reserved6_End                         = 0xFFFF

    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

