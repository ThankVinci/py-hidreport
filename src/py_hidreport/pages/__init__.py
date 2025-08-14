from .GenericDesktopPage import *
from .SimulationControlsPage import *
from .VRControlsPage import *
from .SportControlsPage import *
from .GameControlsPage import *
from .GenericDeviceControlsPage import *
from .KeyboardPage import *
from .LEDPage import *
from .ButtonPage import *
from .OrdinalPage import *
from .TelephonyDevicePage import *
from .ConsumerPage import *
from .DigitizersPage import *
from .HapticsPage import *
from .PhysicalInputDevicePage import *
from .UnicodePage import *
from .SoCPage import *
from .EyeandHeadTrackersPage import *
from .AuxiliaryDisplayPage import *
from .SensorsPage import *
from .MedicalInstrumentPage import *
from .BrailleDisplayPage import *
from .LightingAndIlluminationPage import *
from .MonitorPage import *
from .MonitorEnumeratedPage import *
from .VESAVirtualControlsPage import *
from .PowerPage import *
from .BatterySystemPage import *
from .BarcodeScannerPage import *
from .ScalesPage import *
from .MagneticStripeReaderPage import *
from .CameraControlPage import *
from .ArcadePage import *
from .GamingDevicePage import *
from .FIDOAlliancePage import *
from .VendordefinedPage import *

class PagesManager:
    _instance = None
    @classmethod
    def Get(cls):
        if(cls._instance is None):
            cls._instance = PagesManager()
        return cls._instance
    
    def __init__(self):
        self.__pages = {}

    def __setitem__(self, key, value):
        self.__pages[key] = value

    def __getitem__(self, key):
        if(key not in self.__pages.keys() and isinstance(key, int)):
            if(VendordefinedFF00PageId <= key <= VendordefinedFFFFPageId):
                self.__setitem__(key, VendordefinedPage)
        return self.__pages.get(key)

Pages = PagesManager.Get()

Pages[GenericDesktopPageId]             = GenericDesktopPage
Pages[SimulationControlsPageId]         = SimulationControlsPage
Pages[VRControlsPageId]                 = VRControlsPage
Pages[SportControlsPageId]              = SportControlsPage
Pages[GameControlsPageId]               = GameControlsPage
Pages[GenericDeviceControlsPageId]      = GenericDeviceControlsPage
Pages[KeyboardPageId]                   = KeyboardPage
Pages[KeypadPageId]                     = KeypadPage
Pages[LEDPageId]                        = LEDPage
Pages[ButtonPageId]                     = ButtonPage
Pages[OrdinalPageId]                    = OrdinalPage
Pages[TelephonyDevicePageId]            = TelephonyDevicePage
Pages[ConsumerPageId]                   = ConsumerPage
Pages[DigitizersPageId]                 = DigitizersPage
Pages[HapticsPageId]                    = HapticsPage
Pages[PhysicalInputDevicePageId]        = PhysicalInputDevicePage
Pages[UnicodePageId]                    = UnicodePage
Pages[SoCPageId]                        = SoCPage
Pages[EyeandHeadTrackersPageId]         = EyeandHeadTrackersPage
Pages[AuxiliaryDisplayPageId]           = AuxiliaryDisplayPage
Pages[SensorsPageId]                    = SensorsPage
Pages[MedicalInstrumentPageId]          = MedicalInstrumentPage
Pages[BrailleDisplayPageId]             = BrailleDisplayPage
Pages[LightingAndIlluminationPageId]    = LightingAndIlluminationPage
Pages[MonitorPageId]                    = MonitorPage
Pages[MonitorEnumeratedPageId]          = MonitorEnumeratedPage
Pages[VESAVirtualControlsPageId]        = VESAVirtualControlsPage
Pages[PowerPageId]                      = PowerPage
Pages[BatterySystemPageId]              = BatterySystemPage
Pages[BarcodeScannerPageId]             = BarcodeScannerPage
Pages[ScalesPageId]                     = ScalesPage
Pages[MagneticStripeReaderPageId]       = MagneticStripeReaderPage
Pages[CameraControlPageId]              = CameraControlPage
Pages[ArcadePageId]                     = ArcadePage
Pages[GamingDevicePageId]               = GamingDevicePage
Pages[FIDOAlliancePageId]               = FIDOAlliancePage