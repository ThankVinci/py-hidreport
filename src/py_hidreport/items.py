from __future__ import annotations # 延迟类型解析, 使得包内一些__私有的类型也可以作为另一个类型的参数类型注解, 也可以避免循环引用的问题
from enum import IntEnum
from typing import Union, Callable, Tuple

__all__ = ['Mainitem', 'Globalitem', 'Localitem', 'CollectionitemType', 'HIDItemsize', 'ShortItem', 
           'Data', 'Array', 'Variable', 'Absolute', 'Relative', 'NoWrap', 'Wrap', 'Linear', 'Nonlinear',
           'PreferredState', 'NoPreferred', 'NoNullPosition', 'NullState', 'Nonvolatile', 'Volatile',
           'BitField', 'BufferedBytes',
           'Input', 'Output', 'Feature', 'Collection', 'EndCollection', 
           'UsagePage', 'LogicalMinimum', 'LogicalMaximum', 'PhysicalMinimum', 'PhysicalMaximum', 
           'UnitExponent', 'Unit', 'ReportSize', 'ReportID', 'ReportCount', 'Push', 'Pop', 
           'Usage', 'UsageMinimum', 'UsageMaximum', 'DesignatorIndex', 'DesignatorMinimum', 'DesignatorMaximum',
           'StringIndex', 'StringMinimum', 'StringMaximum', 'Delimiter' ]

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

HIDItemsize = (0, 1, 2, 4) # bSize对应的ItemSize

class ShortItem():
    def __init__(self, item:Union[Mainitem, Globalitem, Localitem], datamainitem = False):
        self.bitvalues = 0
        self.bitcount = 0
        self.__datamainitem = False
        __type = HIDItemtype(item & HIDItemtype.ITEMMASKS)
        if(__type == HIDItemtype.MAINITEM):
            self.__item = Mainitem(item)
            self.__datamainitem = self.__item < Mainitem.Collection
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
    
    def __getbitsize(self):
        if(self.bitcount == 0):
            __size = 0
        elif(self.bitcount <= 8):
            __size = 1
        elif(self.bitcount <= 16):
            __size = 2
        elif(self.bitcount <= 32):
            __size = 4
        else:
            __size = 4
            print('DataInvaild!')
        return __size

    def __datamainitemcall(self, *arg:Tuple[__BitSetCallable]):
        self.bitvalues = 0
        self.bitcount = 0
        if(isinstance(arg, tuple)):
            for i in range(len(arg)):
                caller = arg[i]
                caller(self)
        __size = self.__getbitsize()
        __arg = self.bitvalues
        __data = __arg.to_bytes(length=__size, byteorder='little')
        __tag_v = self.__item | __size
        return __tag_v.to_bytes(length=1) + __data

    def __otheritemcall(self, arg:Union[int, bytes, Callable] = 0):
        if(callable(arg)):
            arg = arg()
        if(isinstance(arg, bytes)):
            __data = arg.rjust(4, b'\x00') if len(arg) == 3 else arg[:4] # 如果3字节就对齐到4字节, 其他情况下就[:4], 超过4字节会截断, 使得始终为1、2、4字节
            __size = len(__data)
        else:
            __size = self.shortest_size(arg)
            __signed = False
            if(arg  < 0):
                __signed = True
            __data = arg.to_bytes(length=__size, byteorder='little', signed=__signed)
        __tag_v = self.__item | __size
        return __tag_v.to_bytes(length=1, byteorder='little') + __data

    def __call__(self, *arg:tuple):
        if(not self.__datamainitem or (len(arg) == 1 and not callable(arg[0]))):
            return self.__otheritemcall(*arg)
        else:
            return self.__datamainitemcall(*arg)
            
    
    def __eq__(self, value):
        if(type(value).__name__ != type(self).__name__):
            return False
        return self.__item == value.__item

# Mainitem的Input/Output/Feature使用的位类型的参数定义
class __BitPart(IntEnum):
    # Bit0
    Data            = 0
    Constant        = 1
    # Bit1
    Array           = 0
    Variable        = 1
    # Bit2
    Absolute        = 0
    Relative        = 1
    # Bit3
    NoWrap          = 0
    Wrap            = 1
    # Bit4
    Linear          = 0
    Nonlinear       = 1
    # Bit5
    PreferredState  = 0
    NoPreferred     = 1
    # Bit6
    NoNullPosition  = 0
    NullState       = 1
    # Bit7
    Reserved        = 0 # Input Item
    Nonvolatile     = 0 # Feature or Output
    Volatile        = 1
    # Bit8
    BitField        = 0
    BufferedBytes   = 1

class __BitSetCallable:
    def __init__(self, bitvalue:__BitPart, bitpos:int):
        self.__bit = bitvalue
        self.__pos = bitpos
    
    def __call__(self, obj:ShortItem):
        if(self.__pos + 1 > obj.bitcount):
            obj.bitcount = self.__pos + 1
        if(self.__bit == 1):
            obj.bitvalues = obj.bitvalues | (1 << self.__pos)
        elif(self.__bit == 0):
            obj.bitvalues = obj.bitvalues & ~(1 << self.__pos)

Data = __BitSetCallable(__BitPart.Data, 0)
Constant = __BitSetCallable(__BitPart.Constant, 0)

Array = __BitSetCallable(__BitPart.Array, 1)
Variable = __BitSetCallable(__BitPart.Variable, 1)

Absolute = __BitSetCallable(__BitPart.Absolute, 2)
Relative = __BitSetCallable(__BitPart.Relative, 2)

NoWrap = __BitSetCallable(__BitPart.NoWrap, 3)
Wrap = __BitSetCallable(__BitPart.Wrap, 3)

Linear = __BitSetCallable(__BitPart.Linear, 4)
Nonlinear = __BitSetCallable(__BitPart.Nonlinear, 4)

PreferredState = __BitSetCallable(__BitPart.PreferredState, 5)
NoPreferred = __BitSetCallable(__BitPart.NoPreferred, 5)

NoNullPosition = __BitSetCallable(__BitPart.NoNullPosition, 6)
NullState = __BitSetCallable(__BitPart.NullState, 6)

Reserved = __BitSetCallable(__BitPart.Reserved, 7)
Nonvolatile = __BitSetCallable(__BitPart.Nonvolatile, 7)
Volatile = __BitSetCallable(__BitPart.Volatile, 7)

BitField = __BitSetCallable(__BitPart.BitField, 8)
BufferedBytes = __BitSetCallable(__BitPart.BufferedBytes, 8)

# MainItem
Input = ShortItem(Mainitem.Input)
Output = ShortItem(Mainitem.Output)
Feature = ShortItem(Mainitem.Featrue)
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

if __name__ == '__main__':
    Collection = ShortItem(Mainitem.Collection)
    EndCollection = ShortItem(Mainitem.EndCollection)
    print(Collection(0x0aff))
    print(EndCollection())
    Input = ShortItem(Mainitem.Input)
    print(Input(Data, Variable, Absolute))