from enum import IntEnum

SoCPageId = 0x11

class SoCPage(IntEnum):
    Undefined                               = 0x00
    SocControl                              = 0x01
    FirmwareTransfer                        = 0x02
    FirmwareFileId                          = 0x03
    FileOffsetInBytes                       = 0x04
    FileTransferSizeMaxInBytes              = 0x05
    FilePayload                             = 0x06
    FilePayloadSizeInBytes                  = 0x07
    FilePayloadContainsLastBytes            = 0x08
    FileTransferStop                        = 0x09
    FileTransferTillEnd                     = 0x0A
    __Reserved0_Begin                       = 0x0B
    __Reserved0_End                         = 0xFFFF

