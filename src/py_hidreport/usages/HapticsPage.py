from enum import IntEnum


class HapticsPage(IntEnum):
    Undefined                               = 0x00
    SimpleHapticController                  = 0x01
    __Reserved0_Begin                       = 0x02
    __Reserved0_End                         = 0x0F
    WaveformList                            = 0x10
    DurationList                            = 0x11
    __Reserved1_Begin                       = 0x12
    __Reserved1_End                         = 0x1F
    AutoTrigger                             = 0x20
    ManualTrigger                           = 0x21
    AutoTriggerAssociatedControl            = 0x22
    Intensity                               = 0x23
    RepeatCount                             = 0x24
    RetriggerPeriod                         = 0x25
    WaveformVendorPage                      = 0x26
    WaveformVendorID                        = 0x27
    WaveformCutoffTime                      = 0x28
    __Reserved2_Begin                       = 0x29
    __Reserved2_End                         = 0x1000
    WaveformNone                            = 0x1001
    WaveformStop                            = 0x1002
    WaveformClick                           = 0x1003
    WaveformBuzzContinuous                  = 0x1004
    WaveformRumbleContinuous                = 0x1005
    WaveformPress                           = 0x1006
    WaveformRelease                         = 0x1007
    WaveformHover                           = 0x1008
    WaveformSuccess                         = 0x1009
    WaveformError                           = 0x100A
    WaveformInkContinuous                   = 0x100B
    WaveformPencilContinuous                = 0x100C
    WaveformMarkerContinuous                = 0x100D
    WaveformChiselMarkerContinuous          = 0x100E
    WaveformBrushContinuous                 = 0x100F
    WaveformEraserContinuous                = 0x1010
    WaveformSparkleContinuous               = 0x1011
    __Reserved3_Begin                       = 0x1012
    __Reserved3_End                         = 0x2000
    ReservedforVendorWaveforms_Begin        = 0x2001
    ReservedforVendorWaveforms_End          = 0x2FFF
    __Reserved4_End                         = 0x3000
    __Reserved4_End                         = 0xFFFF

