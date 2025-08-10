from enum import IntEnum

GameControlsPageId = 0x05

class GameControlsPage(IntEnum):
    Undefined                               = 0x00
    _3DGameController                       = 0x01
    PinballDevice                           = 0x02
    GunDevice                               = 0x03
    __Reserved0_Begin                       = 0x04
    __Reserved0_End                         = 0x1F
    PointofView                             = 0x20
    Turn_Right_or_Left                      = 0x21
    Pitch_Forward_or_Backward               = 0x22
    Roll_Right_or_Left                      = 0x23
    Move_Right_or_Left                      = 0x24
    Move_Forward_or_Backward                = 0x25
    Move_Up_or_Down                         = 0x26
    Lean_Right_or_Left                      = 0x27
    Lean_Forward_or_Backward                = 0x28
    HeightofPOV                             = 0x29
    Flipper                                 = 0x2A
    SecondaryFlipper                        = 0x2B
    Bump                                    = 0x2C
    NewGame                                 = 0x2D
    ShootBall                               = 0x2E
    Player                                  = 0x2F
    GunBolt                                 = 0x30
    GunClip                                 = 0x31
    GunSelector                             = 0x32
    GunSingleShot                           = 0x33
    GunBurst                                = 0x34
    GunAutomatic                            = 0x35
    GunSafety                               = 0x36
    Gamepad_Fire_or_Jump                    = 0x37
    __Reserved1                             = 0x38
    GamepadTrigger                          = 0x39
    FormfittingGamepad                      = 0x3A
    __Reserved2_Begin                       = 0x3B
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

