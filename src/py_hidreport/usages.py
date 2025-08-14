from __future__ import annotations # 延迟类型解析, 使得包内一些__私有的类型也可以作为另一个类型的参数类型注解, 也可以避免循环引用的问题
from enum import IntEnum
from typing import Dict, Type

if __name__ == '__main__':
    # 进行内部调试时会找不到导入的模块，所以手动添加本程序根目录到sys.path中
    # 需要注意不同层级中root_path需要调用dirname的次数是不一样的
    import sys
    from os.path import dirname, abspath
    root_path = dirname(dirname(abspath(__file__)))
    print(root_path)
    sys.path.append(root_path)

__all__ = ['UsagePages', 'Page', 
           'Undefined', 'GenericDesktop', 'SimulationControls', 'VRControls', 
           'SportControls', 'GameControls', 'GenericDeviceControls', 'Keyboard', 'Keypad', 
           'LED', 'Button', 'Ordinal', 'TelephonyDevice', 'Consumer', 'Digitizers', 'Haptics', 
           'PhysicalInputDevice', 'Unicode', 'SoC', 'EyeandHeadTrackers', 'AuxiliaryDisplay',
           'Sensors', 'MedicalInstrument', 'BrailleDisplay', 'LightingAndIllumination',
           'Monitor', 'MonitorEnumerated', 'VESAVirtualControls', 'Power',
           'BatterySystem', 'BarcodeScanner', 'Scales', 'MagneticStripeReader', 'CameraControl', 
           'Arcade', 'GamingDevice', 'FIDOAlliance', 'VendordefinedFF00', 'VendordefinedFFFF', 'Vendordefined' ]

from py_hidreport.pages import *

class UsagePage(IntEnum):
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
    Unicode                     = UnicodePageId
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
    GamingDevice                = GamingDevicePageId
    __Reserved8_BEGIN           = 0x93 # 0x93~0xF1CF
    __Reserved8_END             = 0xF1CF
    FIDOAlliance                = FIDOAlliancePageId
    __Reserved9_BEGIN           = 0xF1D1 # 0xF1D0~0xFEFF
    __Reserved9_END             = 0xFEFF
    VendordefinedFF00           = VendordefinedFF00PageId
    VendordefinedFFFF           = VendordefinedFFFFPageId
    Vendordefined               = lambda value:UsagePage(value) # 0xFF01~0xFFFE
    
    @classmethod
    def _missing_(cls, value):
        if cls.VendordefinedFF00 <= value <= cls.VendordefinedFFFF:
            __pseudo_member = cls._value2member_map_.get(value)
            if __pseudo_member is None:
                # 构造一个临时的枚举对象
                __pseudo_member = int.__new__(cls, value)
                __pseudo_member._name_ = f"Vendordefined{value:04X}"
                __pseudo_member._value_ = value
                # 缓存以避免重复创建
                cls._value2member_map_[value] = __pseudo_member
                setattr(cls, __pseudo_member._name_, __pseudo_member)
            return __pseudo_member
        raise ValueError(f"{value} is not a valid UsagePages")
    
    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

UsagePages:Dict[UsagePage, Page] = {}

class Page():
    def __init__(self, page:UsagePage):
        self.__page = UsagePage(page)
        if(UsagePage.VendordefinedFF00 <= self.__page <= UsagePage.VendordefinedFFFF):
            ...
        else:
            UsagePages[page] = self
    
    def name(self)->str:
        return self.__page.name

    def usage(self, usage_v)->str:
        __page:Type = Pages[self.__page]
        __usage:IntEnum = __page(usage_v)
        return f'{__page.__name__}.{__usage.name}'
    
    def value(self)->int:
        return int(self.__page)

    def __call__(self):
        return self.__page.to_bytes()

Undefined = Page(UsagePage.Undefined)
GenericDesktop = Page(UsagePage.GenericDesktop)
SimulationControls = Page(UsagePage.SimulationControls)
VRControls = Page(UsagePage.VRControls)
SportControls = Page(UsagePage.SportControls)
GameControls = Page(UsagePage.GameControls)
GenericDeviceControls = Page(UsagePage.GenericDeviceControls)
Keyboard = Page(UsagePage.Keyboard)
Keypad = Page(UsagePage.Keypad)
LED = Page(UsagePage.LED)
Button = Page(UsagePage.Button)
Ordinal = Page(UsagePage.Ordinal)
TelephonyDevice = Page(UsagePage.TelephonyDevice)
Consumer = Page(UsagePage.Consumer)
Digitizers = Page(UsagePage.Digitizers)
Haptics = Page(UsagePage.Haptics)
PhysicalInputDevice = Page(UsagePage.PhysicalInputDevice)
Unicode = Page(UsagePage.Unicode)
SoC = Page(UsagePage.SoC)
EyeandHeadTrackers = Page(UsagePage.EyeandHeadTrackers)
AuxiliaryDisplay = Page(UsagePage.AuxiliaryDisplay)
Sensors = Page(UsagePage.Sensors)
MedicalInstrument = Page(UsagePage.MedicalInstrument)
BrailleDisplay = Page(UsagePage.BrailleDisplay)
LightingAndIllumination = Page(UsagePage.LightingAndIllumination)
Monitor = Page(UsagePage.Monitor)
MonitorEnumerated = Page(UsagePage.MonitorEnumerated)
VESAVirtualControls = Page(UsagePage.VESAVirtualControls)
Power = Page(UsagePage.Power)
BatterySystem = Page(UsagePage.BatterySystem)
BarcodeScanner = Page(UsagePage.BarcodeScanner)
Scales = Page(UsagePage.Scales)
MagneticStripeReader = Page(UsagePage.MagneticStripeReader)
CameraControl = Page(UsagePage.CameraControl)
Arcade = Page(UsagePage.Arcade)
GamingDevice = Page(UsagePage.GamingDevice)
FIDOAlliance = Page(UsagePage.FIDOAlliance)
VendordefinedFF00 = Page(UsagePage.VendordefinedFF00)
VendordefinedFFFF = Page(UsagePage.VendordefinedFFFF)
Vendordefined = lambda v:Page(UsagePage.Vendordefined(v))