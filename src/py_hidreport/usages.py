from enum import IntEnum

if __name__ == '__main__':
    # 进行内部调试时会找不到导入的模块，所以手动添加本程序根目录到sys.path中
    # 需要注意不同层级中root_path需要调用dirname的次数是不一样的
    import sys
    from os.path import dirname, abspath
    root_path = dirname(dirname(abspath(__file__)))
    print(root_path)
    sys.path.append(root_path)

from pages import *

class UsagePages(IntEnum):
    Undefined                   = 0x00
    GenericDesktop              = GenericDesktopPageId
    SimulationControls          = SimulationControlsPageId
    VRControls                  = VRControlsPageId
    SportControls               = SportControlsPageId
    GameControls                = GameControlsPageId
    GenericDeviceControls       = GenericDeviceControlsPageId
    Keyboard                    = KeyboardPageId
    Keypad                      = KeypadPageId
    LED                         = LEDPageId
    Button                      = ButtonPageId
    Ordinal                     = OrdinalPageId
    TelephonyDevice             = TelephonyDevicePageId
    Consumer                    = ConsumerPageId
    Digitizers                  = DigitizersPageId
    Haptics                     = HapticsPageId
    PhysicalInputDevice         = PhysicalInputDevicePageId
    Unicode                     = 0x10
    SoC                         = SoCPageId
    EyeandHeadTrackers          = EyeandHeadTrackersPageId
    __Reserved0                 = 0x13 # 0x13~0x13
    AuxiliaryDisplay            = AuxiliaryDisplayPageId
    __Reserved1_BEGIN           = 0x15 # 0x15~0x1F
    __Reserved1_END             = 0x1F
    Sensors                     = SensorsPageId
    __Reserved2_BEGIN           = 0x21 # 0x21~0x3F
    __Reserved2_END             = 0x3F
    MedicalInstrument           = MedicalInstrumentPageId
    BrailleDisplay              = BrailleDisplayPageId
    __Reserved3_BEGIN           = 0x42 # 0x42~0x58
    __Reserved3_END             = 0x58
    LightingAndIllumination     = LightingAndIlluminationPageId
    __Reserved4_BEGIN           = 0x5A # 0x5A~0x7F
    __Reserved4_END             = 0x7F
    Monitor                     = MonitorPageId
    MonitorEnumerated           = MonitorEnumeratedPageId
    VESAVirtualControls         = VESAVirtualControlsPageId
    __Reserved5                 = 0x83 # 0x83~0x83
    Power                       = PowerPageId
    BatterySystem               = BatterySystemPageId
    __Reserved6_BEGIN           = 0x86 # 0x86~0x8B
    __Reserved6_END             = 0x8B
    BarcodeScanner              = BarcodeScannerPageId
    Scales                      = ScalesPageId
    MagneticStripeReader        = MagneticStripeReaderPageId
    __Reserved7                 = 0x8F # 0x8F~0x8F
    CameraControl               = CameraControlPageId
    Arcade                      = ArcadePageId
    GamingDevice                = 0x92
    __Reserved8_BEGIN           = 0x93 # 0x93~0xF1CF
    __Reserved8_END             = 0xF1CF
    FIDOAlliance                = FIDOAlliancePageId
    __Reserved9_BEGIN           = 0xF1D1 # 0xF1D0~0xFEFF
    __Reserved9_END             = 0xFEFF
    Vendordefined_BEGIN         = 0xFF00
    Vendordefined_END           = 0xFFFF
    Vendordefined               = lambda value:UsagePages(value) # 0xFF00~0xFFFF
    
    @classmethod
    def _missing_(cls, value):
        if cls.Vendordefined_BEGIN <= value <= cls.Vendordefined_END:
            __pseudo_member = cls._value2member_map_.get(value)
            if __pseudo_member is None:
                # 构造一个临时的枚举对象
                __pseudo_member = int.__new__(cls, value)
                __pseudo_member._name_ = f"Vendordefined{value:04X}"
                __pseudo_member._value_ = value
                # 缓存以避免重复创建
                cls._value2member_map_[value] = __pseudo_member
            return __pseudo_member
        raise ValueError(f"{value} is not a valid UsagePages")

class Page():
    def __init__(self, page):
        self.__page = page
    
    def __call__(self):
        __page_v = self.__page
        return bytes(__page_v)

    def usage(self, usage_v):
        return Pages[self.__page](usage_v).name
        # return usage_v


Undefined = Page(UsagePages.Undefined)
GenericDesktop = Page(UsagePages.GenericDesktop)
SimulationControls = Page(UsagePages.SimulationControls)
VRControls = Page(UsagePages.VRControls)
SportControls = Page(UsagePages.SportControls)
GameControls = Page(UsagePages.GameControls)
GenericDeviceControls = Page(UsagePages.GenericDeviceControls)
Keyboard = Page(UsagePages.Keyboard)
Keypad = Page(UsagePages.Keypad)
LED = Page(UsagePages.LED)
Button = Page(UsagePages.Button)
Ordinal = Page(UsagePages.Ordinal)
TelephonyDevice = Page(UsagePages.TelephonyDevice)
Consumer = Page(UsagePages.Consumer)
Digitizers = Page(UsagePages.Digitizers)
Haptics = Page(UsagePages.Haptics)
PhysicalInputDevice = Page(UsagePages.PhysicalInputDevice)
Unicode = Page(UsagePages.Unicode)
SoC = Page(UsagePages.SoC)
EyeandHeadTrackers = Page(UsagePages.EyeandHeadTrackers)
AuxiliaryDisplay = Page(UsagePages.AuxiliaryDisplay)
Sensors = Page(UsagePages.Sensors)
MedicalInstrument = Page(UsagePages.MedicalInstrument)
BrailleDisplay = Page(UsagePages.BrailleDisplay)
LightingAndIllumination = Page(UsagePages.LightingAndIllumination)
Monitor = Page(UsagePages.Monitor)
MonitorEnumerated = Page(UsagePages.MonitorEnumerated)
VESAVirtualControls = Page(UsagePages.VESAVirtualControls)
Power = Page(UsagePages.Power)
BatterySystem = Page(UsagePages.BatterySystem)
BarcodeScanner = Page(UsagePages.BarcodeScanner)
Scales = Page(UsagePages.Scales)
MagneticStripeReader = Page(UsagePages.MagneticStripeReader)
CameraControl = Page(UsagePages.CameraControl)
Arcade = Page(UsagePages.Arcade)
GamingDevice = Page(UsagePages.GamingDevice)
FIDOAlliance = Page(UsagePages.FIDOAlliance)
VendordefinedFF01 = Page(UsagePages.Vendordefined(0xFF01))