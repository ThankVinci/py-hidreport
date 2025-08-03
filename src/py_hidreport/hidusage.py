from enum import IntEnum

if __name__ == '__main__':
    # 进行内部调试时会找不到导入的模块，所以手动添加本程序根目录到sys.path中
    # 需要注意不同层级中root_path需要调用dirname的次数是不一样的
    import sys
    from os.path import dirname, abspath
    root_path = dirname(dirname(abspath(__file__)))
    print(root_path)
    sys.path.append(root_path)

'''
Items
'''
from py_hidreport.items import ShortItem
from py_hidreport.items import Mainitem, Globalitem, Localitem, CollectionitemType
from py_hidreport.items.Main import Input
from py_hidreport.items.Main import Data, Variable, Absolute

# MainItem
Output = ShortItem(Mainitem.Output)
Feature = ShortItem(Mainitem.Output)
Collection = ShortItem(Mainitem.Collection)
EndCollection = ShortItem(Mainitem.EndCollection)

# GlobalItem
UsagePage = ShortItem(Globalitem.UsagePage)
LogicalMinimum = ShortItem(Globalitem.LogicalMinimum)
LogicalMaximum = ShortItem(Globalitem.LogicalMaximum)
PhysicalMinimum = ShortItem(Globalitem.PhysicalMinimum)
PhysicalMaximum = ShortItem(Globalitem.PhysicalMaximum)
UnitExponent = ShortItem(Globalitem.UnitExponent)
Unit = ShortItem(Globalitem.Unit)
ReportSize = ShortItem(Globalitem.ReportSize)
ReportID = ShortItem(Globalitem.ReportID)
ReportCount = ShortItem(Globalitem.ReportCount)
Push = ShortItem(Globalitem.Push)
Pop = ShortItem(Globalitem.Pop)

# LocalItem
Usage = ShortItem(Localitem.Usage)
UsageMinimum = ShortItem(Localitem.UsageMinimum)
UsageMaximum = ShortItem(Localitem.UsageMaximum)
DesignatorIndex = ShortItem(Localitem.DesignatorIndex)
DesignatorMinimum = ShortItem(Localitem.DesignatorMinimum)
DesignatorMaximum = ShortItem(Localitem.DesignatorMaximum)
StringIndex = ShortItem(Localitem.StringIndex)
StringMinimum = ShortItem(Localitem.StringMinimum)
StringMaximum = ShortItem(Localitem.StringMaximum)
Delimiter = ShortItem(Localitem.Delimiter)

'''
Pages
'''

class UsagePages(IntEnum):
    Undefined                   = 0x00
    GenericDesktopPage          = 0x01
    SimulationControlsPage      = 0x02
    VRControlsPage              = 0x03
    SportControlsPage           = 0x04
    GameControlsPage            = 0x05
    GenericDeviceControlsPage   = 0x06
    KeyboardPage                = 0x07
    KeypadPage                  = 0x07
    LEDPage                     = 0x08
    ButtonPage                  = 0x09
    OrdinalPage                 = 0x0a
    TelephonyDevicePage         = 0x0b
    ConsumerPage                = 0x0c
    DigitizersPage              = 0x0d
    HapticsPage                 = 0x0e
    PhysicalInputDevicePage     = 0x0f
    UnicodePage                 = 0x10
    SoCPage                     = 0x11
    EyeandHeadTrackersPage      = 0x12
    __Reserved0                 = 0x13 # 0x13~0x13
    AuxiliaryDisplayPage        = 0x14
    __Reserved1_BEGIN           = 0x15 # 0x15~0x1F
    __Reserved1_END             = 0x1F
    SensorsPage                 = 0x20
    __Reserved2_BEGIN           = 0x21 # 0x21~0x3F
    __Reserved2_END             = 0x3F
    MedicalInstrumentPage       = 0x40
    BrailleDisplayPage          = 0x41
    __Reserved3_BEGIN           = 0x42 # 0x42~0x58
    __Reserved3_END             = 0x58
    LightingAndIlluminationPage = 0x59
    __Reserved4_BEGIN           = 0x5A # 0x5A~0x7F
    __Reserved4_END             = 0x7F
    MonitorPage                 = 0x80
    MonitorEnumeratedPage       = 0x81
    VESAVirtualControlsPage     = 0x82
    __Reserved5                 = 0x83 # 0x83~0x83
    PowerPage                   = 0x84
    BatterySystemPage           = 0x85
    __Reserved6_BEGIN           = 0x86 # 0x86~0x8B
    __Reserved6_END             = 0x8B
    BarcodeScannerPage          = 0x8C
    ScalesPage                  = 0x8D
    MagneticStripeReaderPage    = 0x8E
    __Reserved7                 = 0x8F # 0x8F~0x8F
    CameraControlPage           = 0x90
    ArcadePage                  = 0x91
    GamingDevicePage            = 0x92
    __Reserved8_BEGIN           = 0x93 # 0x93~0xF1CF
    __Reserved8_END             = 0xF1CF
    FIDOAlliancePage            = 0xF1D0
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

GenericDesktop = Page(UsagePages.GenericDesktopPage)
SimulationControls = Page(UsagePages.SimulationControlsPage)
VRControls = Page(UsagePages.VRControlsPage)
SportControls = Page(UsagePages.SportControlsPage)
GameControls = Page(UsagePages.GameControlsPage)
GenericDeviceControls = Page(UsagePages.GenericDeviceControlsPage)
Keyboard = Page(UsagePages.KeyboardPage)
Keypad = Page(UsagePages.KeypadPage)
LED = Page(UsagePages.LEDPage)
Button = Page(UsagePages.ButtonPage)
Ordinal = Page(UsagePages.OrdinalPage)
TelephonyDevice = Page(UsagePages.TelephonyDevicePage)
Consumer = Page(UsagePages.ConsumerPage)
Digitizers = Page(UsagePages.DigitizersPage)
Haptics = Page(UsagePages.HapticsPage)
PhysicalInputDevice = Page(UsagePages.PhysicalInputDevicePage)
Unicode = Page(UsagePages.UnicodePage)
SoC = Page(UsagePages.SoCPage)
EyeandHeadTrackers = Page(UsagePages.EyeandHeadTrackersPage)
AuxiliaryDisplay = Page(UsagePages.AuxiliaryDisplayPage)
Sensors = Page(UsagePages.SensorsPage)
MedicalInstrument = Page(UsagePages.MedicalInstrumentPage)
BrailleDisplay = Page(UsagePages.BrailleDisplayPage)
LightingAndIllumination = Page(UsagePages.LightingAndIlluminationPage)
Monitor = Page(UsagePages.MonitorPage)
MonitorEnumerated = Page(UsagePages.MonitorEnumeratedPage)
VESAVirtualControls = Page(UsagePages.VESAVirtualControlsPage)
Power = Page(UsagePages.PowerPage)
BatterySystem = Page(UsagePages.BatterySystemPage)
BarcodeScanner = Page(UsagePages.BarcodeScannerPage)
Scales = Page(UsagePages.ScalesPage)
MagneticStripeReader = Page(UsagePages.MagneticStripeReaderPage)
CameraControl = Page(UsagePages.CameraControlPage)
Arcade = Page(UsagePages.ArcadePage)
GamingDevice = Page(UsagePages.GamingDevicePage)
FIDOAlliance = Page(UsagePages.FIDOAlliancePage)
VendordefinedFF01 = Page(UsagePages.Vendordefined(0xFF01))

from usages import *
from items import *
# 状态机

def main():
    print(UsagePages.Vendordefined(0xFF01).name)
    print(ButtonPage.Button(5).name)
    print(OrdinalPage.Instance(4).name)
    print(type(UsagePages(UsagePages.Vendordefined(0xFF01))) == UsagePages)
    print(type(Mainitem(0b10000000)) == Mainitem)
    print(UsagePage(GenericDesktop))
    print(Usage(GenericDesktopPage.Mouse))
    print(Collection(CollectionitemType.Application))

    UsagePage(GenericDesktop)
    Usage(GenericDesktopPage.Mouse)
    Collection(CollectionitemType.Application)
    Usage(GenericDesktopPage.Pointer)
    Collection(CollectionitemType.Physical)
    UsageMinimum(1)
    UsageMaximum(3)
    LogicalMinimum(0)
    LogicalMaximum(1)
    ReportCount(3)
    ReportSize(1)
    Input(Data, Variable, Absolute)
    ReportCount(1)
    ReportSize(5)
    # Input(Constant)
    UsagePage(GenericDesktop)
    Usage(GenericDesktopPage.X)
    Usage(GenericDesktopPage.Y)
    print(LogicalMinimum(-127))
    print(LogicalMaximum(127))
    ReportSize(8)
    ReportCount(2)
    # Input(Data, Variable, Relative)
    EndCollection()
    EndCollection()

if __name__ == '__main__':
    # main()
    ...