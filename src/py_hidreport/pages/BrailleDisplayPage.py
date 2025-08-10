from enum import IntEnum

BrailleDisplayPageId = 0x41

class BrailleDisplayPage(IntEnum):
    Undefined                               = 0x00
    BrailleDisplay                          = 0x01
    BrailleRow                              = 0x02
    _8DotBrailleCell                        = 0x03
    _6DotBrailleCell                        = 0x04
    NumberofBrailleCells                    = 0x05
    ScreenReaderControl                     = 0x06
    ScreenReaderIdentifier                  = 0x07
    __Reserved0_Begin                       = 0x08
    __Reserved0_End                         = 0xF9
    RouterSet1                              = 0xFA
    RouterSet2                              = 0xFB
    RouterSet3                              = 0xFC
    __Reserved1_Begin                       = 0xFD
    __Reserved1_End                         = 0xFF
    RouterKey                               = 0x100
    RowRouterKey                            = 0x101
    __Reserved2_Begin                       = 0x102
    __Reserved2_End                         = 0x1FF
    BrailleButtons                          = 0x200
    BrailleKeyboardDot1                     = 0x201
    BrailleKeyboardDot2                     = 0x202
    BrailleKeyboardDot3                     = 0x203
    BrailleKeyboardDot4                     = 0x204
    BrailleKeyboardDot5                     = 0x205
    BrailleKeyboardDot6                     = 0x206
    BrailleKeyboardDot7                     = 0x207
    BrailleKeyboardDot8                     = 0x208
    BrailleKeyboardSpace                    = 0x209
    BrailleKeyboardLeftSpace                = 0x20A
    BrailleKeyboardRightSpace               = 0x20B
    BrailleFaceControls                     = 0x20C
    BrailleLeftControls                     = 0x20D
    BrailleRightControls                    = 0x20E
    BrailleTopControls                      = 0x20F
    BrailleJoystickCenter                   = 0x210
    BrailleJoystickUp                       = 0x211
    BrailleJoystickDown                     = 0x212
    BrailleJoystickLeft                     = 0x213
    BrailleJoystickRight                    = 0x214
    BrailleDPadCenter                       = 0x215
    BrailleDPadUp                           = 0x216
    BrailleDPadDown                         = 0x217
    BrailleDPadLeft                         = 0x218
    BrailleDPadRight                        = 0x219
    BraillePanLeft                          = 0x21A
    BraillePanRight                         = 0x21B
    BrailleRockerUp                         = 0x21C
    BrailleRockerDown                       = 0x21D
    BrailleRockerPress                      = 0x21E
    __Reserved3_Begin                       = 0x21F
    __Reserved3_End                         = 0xFFFF

    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

