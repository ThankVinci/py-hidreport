from enum import IntEnum

MedicalInstrumentPageId = 0x40

class MedicalInstrumentPage(IntEnum):
    Undefined                               = 0x00
    MedicalUltrasound                       = 0x01
    __Reserved0_Begin                       = 0x02
    __Reserved0_End                         = 0x1F
    VCR_or_Acquisition                      = 0x20
    Freeze_or_Thaw                          = 0x21
    ClipStore                               = 0x22
    Update                                  = 0x23
    Next                                    = 0x24
    Save                                    = 0x25
    Print                                   = 0x26
    MicrophoneEnable                        = 0x27
    __Reserved1_Begin                       = 0x28
    __Reserved1_End                         = 0x3F
    Cine                                    = 0x40
    TransmitPower                           = 0x41
    Volume                                  = 0x42
    Focus                                   = 0x43
    Depth                                   = 0x44
    __Reserved2_Begin                       = 0x45
    __Reserved2_End                         = 0x5F
    SoftStepPrimary                         = 0x60
    SoftStepSecondary                       = 0x61
    __Reserved3_Begin                       = 0x62
    __Reserved3_End                         = 0x6F
    DepthGainCompensation                   = 0x70
    __Reserved4_Begin                       = 0x71
    __Reserved4_End                         = 0x7F
    ZoomSelect                              = 0x80
    ZoomAdjust                              = 0x81
    SpectralDopplerModeSelect               = 0x82
    SpectralDopplerAdjust                   = 0x83
    ColorDopplerModeSelect                  = 0x84
    ColorDopplerAdjust                      = 0x85
    MotionModeSelect                        = 0x86
    MotionModeAdjust                        = 0x87
    _2DModeSelect                           = 0x88
    _2DModeAdjust                           = 0x89
    __Reserved5_Begin                       = 0x8A
    __Reserved5_End                         = 0x9F
    SoftControlSelect                       = 0xA0
    SoftControlAdjust                       = 0xA1
    __Reserved6_Begin                       = 0xA2
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

