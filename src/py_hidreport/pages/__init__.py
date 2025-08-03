Pages = {}

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
# from .UnicodePage import *
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
# from .GamingDevicePage import *
from .FIDOAlliancePage import *

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
# Pages[UnicodePageId]                    = UnicodePage
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
# Pages[GamingDevicePageId]               = GamingDevicePage
Pages[FIDOAlliancePageId]               = FIDOAlliancePage