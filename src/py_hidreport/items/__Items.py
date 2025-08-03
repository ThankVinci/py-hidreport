from enum import IntEnum
from typing import Union, Callable

class Mainitem(IntEnum):
    Input           = 0b10000000 # 最后两位按实际的来
    Output          = 0b10010000 # 最后两位按实际的来
    Featrue         = 0b10110000 # 最后两位按实际的来
    Collection      = 0b10100000 # 最后两位按实际的来
    EndCollection   = 0b11000000 # 最后两位按实际的来

    Reserved_Begin  = 0b11010000 # 最后两位按实际的来
    Reserved_End    = 0b11110000 # 最后两位按实际的来

class Globalitem(IntEnum):
    UsagePage       = 0b00000100 # 最后两位按实际的来
    LogicalMinimum  = 0b00010100 # 最后两位按实际的来
    LogicalMaximum  = 0b00100100 # 最后两位按实际的来
    PhysicalMinimum = 0b00110100 # 最后两位按实际的来
    PhysicalMaximum = 0b01000100 # 最后两位按实际的来
    UnitExponent    = 0b01010100 # 最后两位按实际的来
    Unit            = 0b01100100 # 最后两位按实际的来
    ReportSize      = 0b01110100 # 最后两位按实际的来
    ReportID        = 0b10000100 # 最后两位按实际的来
    ReportCount     = 0b10010100 # 最后两位按实际的来
    Push            = 0b10100100 # 最后两位按实际的来
    Pop             = 0b10110100 # 最后两位按实际的来

    Reserved_Begin  = 0b11000100 # 最后两位按实际的来
    Reserved_End    = 0b11110100 # 最后两位按实际的来

class Localitem(IntEnum):
    Usage               = 0b00001000 # 最后两位按实际的来
    UsageMinimum        = 0b00011000 # 最后两位按实际的来
    UsageMaximum        = 0b00101000 # 最后两位按实际的来
    DesignatorIndex     = 0b00111000 # 最后两位按实际的来
    DesignatorMinimum   = 0b01001000 # 最后两位按实际的来
    DesignatorMaximum   = 0b01011000 # 最后两位按实际的来
    StringIndex         = 0b01111000 # 最后两位按实际的来
    StringMinimum       = 0b10001000 # 最后两位按实际的来
    StringMaximum       = 0b10011000 # 最后两位按实际的来
    Delimiter           = 0b10101000 # 最后两位按实际的来
    
    Reserved_Begin      = 0b10101000 # 最后两位按实际的来
    Reserved_End        = 0b11111000 # 最后两位按实际的来

class CollectionitemType(IntEnum):
    Physical                = 0x00 # group of axes
    Application             = 0x01 # mouse keyboard
    Logical                 = 0x02 # interrelated data
    Report                  = 0x03
    NamedArray              = 0x04
    UsageSwitch             = 0x05
    UsageModifier           = 0x06

    Reserved_Begin          = 0x07
    Reserved_End            = 0x7F
    Vendor_defined_Begin    = 0x80
    Vendor_defined_End      = 0xFF

class HIDItemtype(IntEnum):
    MAINITEM    = 0b00000000
    GLOBALITEM  = 0b00000100
    LOCALITEM   = 0b00001000
    __RESERVED  = 0b00001100
    ITEMMASKS    = MAINITEM | GLOBALITEM | LOCALITEM

HIDItemsize = (0, 1, 2, 4)

class ShortItem():
    def __init__(self, item:Union[Mainitem, Globalitem, Localitem]):
        __type = HIDItemtype(item & HIDItemtype.ITEMMASKS)
        if(__type == HIDItemtype.MAINITEM):
            self.__item = Mainitem(item)
        elif(__type == HIDItemtype.GLOBALITEM):
            self.__item = Globalitem(item)
        elif(__type == HIDItemtype.LOCALITEM):
            self.__item = Localitem(item)
        else:
            raise ValueError()

    
    # 将int值限定到0、1、2、4字节范围中，取最小的
    def shortest_size(self, intvalue:int):
        assert(isinstance(intvalue, (int)))
        if(intvalue == 0):
            return 0
        elif(intvalue.bit_length() <= 8):
            return 1
        elif(intvalue.bit_length() <= 16):
            return 2
        elif(intvalue.bit_length() <= 32):
            return 4
        else:
            return 4
    
    def getname(self):
        return self.__item.name

    def __call__(self, arg:Union[int, bytes, Callable] = 0):
        if(callable(arg)):
            arg = arg()
        if(isinstance(arg, bytes)):
            __data = arg.rjust(4, b'\x00') if len(arg) == 3 else arg[:4] # 如果3字节就对齐到4字节, 其他情况下就[:4], 超过4字节会截断, 使得始终为1、2、4字节
            __size = len(__data)
        else:
            __size = self.shortest_size(arg)
            print(__size)
            __signed = False
            if(arg  < 0):
                __signed = True
            __data = arg.to_bytes(length=__size, byteorder='little', signed=__signed)
        __tag_v = self.__item | __size
        return __tag_v.to_bytes(length=1, byteorder='little') + __data

if __name__ == '__main__':
    Collection = ShortItem(Mainitem.Collection)
    EndCollection = ShortItem(Mainitem.EndCollection)
    print(Collection(0x0aff))
    print(Collection(Collection(Collection(0x121212))))
    print(EndCollection())