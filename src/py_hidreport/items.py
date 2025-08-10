from __future__ import annotations # 延迟类型解析, 使得包内一些__私有的类型也可以作为另一个类型的参数类型注解, 也可以避免循环引用的问题
from enum import IntEnum
from typing import Union, Callable, Tuple

__all__ = ['HIDItemsize', 'ShortItems', 'MainitemCollectionPart', 'MainitemBitPart', 
           'Data', 'Constant', 'Array', 'Variable', 'Absolute', 'Relative', 
           'NoWrap', 'Wrap', 'Linear', 'Nonlinear', 'PreferredState', 'NoPreferred', 
           'NoNullPosition', 'NullState', 'Nonvolatile', 'Volatile', 'BitField', 'BufferedBytes',
           'Physical', 'Application', 'Logical', 'Report', 'NamedArray', 'UsageSwitch', 'UsageModifier',
           'Input', 'Output', 'Feature', 'Collection', 'EndCollection', 
           'UsagePage', 'LogicalMinimum', 'LogicalMaximum', 'PhysicalMinimum', 'PhysicalMaximum', 
           'UnitExponent', 'Unit', 'ReportSize', 'ReportID', 'ReportCount', 'Push', 'Pop', 
           'Usage', 'UsageMinimum', 'UsageMaximum', 'DesignatorIndex', 'DesignatorMinimum', 'DesignatorMaximum',
           'StringIndex', 'StringMinimum', 'StringMaximum', 'Delimiter' ]

class Mainitem(IntEnum):
    Input           = 0b10000000 # 最后两位按实际的来
    Output          = 0b10010000 # 最后两位按实际的来
    Feature         = 0b10110000 # 最后两位按实际的来
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

class HIDItemtype(IntEnum):
    MAINITEM    = 0b00000000
    GLOBALITEM  = 0b00000100
    LOCALITEM   = 0b00001000
    __RESERVED  = 0b00001100
    ITEMMASKS    = MAINITEM | GLOBALITEM | LOCALITEM

HIDItemsize = (0, 1, 2, 4) # bSize对应的ItemSize

ShortItems = {}

class ShortItem():
    def __init__(self, item:Union[Mainitem, Globalitem, Localitem]):
        self.bitvalues = 0
        self.bitcount = 0
        self.__mainitem = False
        self.__collection= False
        __type = HIDItemtype(item & HIDItemtype.ITEMMASKS)
        if(__type == HIDItemtype.MAINITEM):
            self.__item = Mainitem(item)
            self.__mainitem = True
            self.__collection = self.__item in (Mainitem.Collection, Mainitem.EndCollection)
        elif(__type == HIDItemtype.GLOBALITEM):
            self.__item = Globalitem(item)
        elif(__type == HIDItemtype.LOCALITEM):
            self.__item = Localitem(item)
        else:
            raise ValueError()
        ShortItems[self.__item] = self

    def name(self):
        return self.__item.name

    # 将int值限定到1、2、4字节范围中，取最小的
    def __shortest_size(self, intvalue:int):
        assert(isinstance(intvalue, (int)))
        if(intvalue.bit_length() <= 8):
            return 1
        elif(intvalue.bit_length() <= 16):
            return 2
        elif(intvalue.bit_length() <= 32):
            return 4
        else:
            return 4
    
    def __getbitsize(self):
        if(self.bitcount <= 8):
            __size = 1
        elif(self.bitcount <= 16):
            __size = 2
        elif(self.bitcount <= 32):
            __size = 4
        else:
            __size = 4
            print('DataInvaild!')
        return __size

    def __collectionitemcall(self, *arg):
        if(self.__item is Mainitem.Collection):
            return self.__otheritemcall(*arg)
        else:
            __size = 0
            __tag_v = self.__item | __size 
            return __tag_v.to_bytes(length=1)


    def __mainitemcall(self, *arg:Tuple[MainitemBitSetCallable]):
        if(self.__collection):
            return self.__collectionitemcall(*arg)
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
            __size = self.__shortest_size(arg)
            __signed = False
            if(arg  < 0):
                __signed = True
            __data = arg.to_bytes(length=__size, byteorder='little', signed=__signed)
        __tag_v = self.__item | __size
        return __tag_v.to_bytes(length=1, byteorder='little') + __data

    def __call__(self, *arg:tuple):
        if(not self.__mainitem or (len(arg) == 1 and not callable(arg[0]))):
            return self.__otheritemcall(*arg)
        else:
            return self.__mainitemcall(*arg)
            
    def __eq__(self, value):
        if(type(value).__name__ != type(self).__name__):
            return False
        return self.__item == value.__item

# Mainitem的Input/Output/Feature使用的位类型的参数定义
class MainitemBitPart:
    class __Bit0(IntEnum):
        Data            = 0
        Constant        = 1
    class __Bit1(IntEnum):
        Array           = 0
        Variable        = 1
    class __Bit2(IntEnum):
        Absolute        = 0
        Relative        = 1
    class __Bit3(IntEnum):
        NoWrap          = 0
        Wrap            = 1
    class __Bit4(IntEnum):
        Linear          = 0
        Nonlinear       = 1
    class __Bit5(IntEnum):
        PreferredState  = 0
        NoPreferred     = 1
    class __Bit6(IntEnum):
        NoNullPosition  = 0
        NullState       = 1
    class __Bit7(IntEnum):
        Nonvolatile     = 0 # Input时表示Reserved
        Volatile        = 1
    class __Bit8(IntEnum):
        BitField        = 0
        BufferedBytes   = 1
    
    MainitemBits = {}
    MainitemBits[0] = __Bit0
    MainitemBits[1] = __Bit1
    MainitemBits[2] = __Bit2
    MainitemBits[3] = __Bit3
    MainitemBits[4] = __Bit4
    MainitemBits[5] = __Bit5
    MainitemBits[6] = __Bit6
    MainitemBits[7] = __Bit7
    MainitemBits[8] = __Bit8

    @classmethod
    def parse(cls, value:int):
        value = value & 0x1ff
        __args = ''
        __cnt = 0
        for i in range(9):
            __value = (value >> i) & 1
            if(__value == 1):
                if(__cnt == 0):
                    __args += f'{MainitemBits[i](__value).name}'
                    __cnt += 1
                else:
                    __args += f',{MainitemBits[i](__value).name}'
        return __args

MainitemBits = MainitemBitPart.MainitemBits

class MainitemBitSetCallable:
    def __init__(self, bitvalue:int, bitpos:int):
        self.__bit = bitvalue
        self.__pos = bitpos
    
    def __call__(self, obj:ShortItem):
        if(self.__pos + 1 > obj.bitcount):
            obj.bitcount = self.__pos + 1
        if(self.__bit == 1):
            obj.bitvalues = obj.bitvalues | (1 << self.__pos)
        elif(self.__bit == 0):
            obj.bitvalues = obj.bitvalues & ~(1 << self.__pos)

Data = MainitemBitSetCallable(MainitemBits[0].Data, 0)
Constant = MainitemBitSetCallable(MainitemBits[0].Constant, 0)

Array = MainitemBitSetCallable(MainitemBits[1].Array, 1)
Variable = MainitemBitSetCallable(MainitemBits[1].Variable, 1)

Absolute = MainitemBitSetCallable(MainitemBits[2].Absolute, 2)
Relative = MainitemBitSetCallable(MainitemBits[2].Relative, 2)

NoWrap = MainitemBitSetCallable(MainitemBits[3].NoWrap, 3)
Wrap = MainitemBitSetCallable(MainitemBits[3].Wrap, 3)

Linear = MainitemBitSetCallable(MainitemBits[4].Linear, 4)
Nonlinear = MainitemBitSetCallable(MainitemBits[4].Nonlinear, 4)

PreferredState = MainitemBitSetCallable(MainitemBits[5].PreferredState, 5)
NoPreferred = MainitemBitSetCallable(MainitemBits[5].NoPreferred, 5)

NoNullPosition = MainitemBitSetCallable(MainitemBits[6].NoNullPosition, 6)
NullState = MainitemBitSetCallable(MainitemBits[6].NullState, 6)

Reserved = MainitemBitSetCallable(MainitemBits[7].Nonvolatile, 7)
Nonvolatile = MainitemBitSetCallable(MainitemBits[7].Nonvolatile, 7)
Volatile = MainitemBitSetCallable(MainitemBits[7].Volatile, 7)

BitField = MainitemBitSetCallable(MainitemBits[8].BitField, 8)
BufferedBytes = MainitemBitSetCallable(MainitemBits[8].BufferedBytes, 8)

# Mainitem的Collection使用的参数定义
class MainitemCollectionPart(IntEnum):
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

class MainitemCollectionCallable:
    def __init__(self, part:MainitemCollectionPart):
        self.__part = MainitemCollectionPart(part)
    
    def __call__(self):
        return self.__part

Physical = MainitemCollectionCallable(MainitemCollectionPart.Physical)
Application = MainitemCollectionCallable(MainitemCollectionPart.Application)
Logical = MainitemCollectionCallable(MainitemCollectionPart.Logical)
Report = MainitemCollectionCallable(MainitemCollectionPart.Report)
NamedArray = MainitemCollectionCallable(MainitemCollectionPart.NamedArray)
UsageSwitch = MainitemCollectionCallable(MainitemCollectionPart.UsageSwitch)
UsageModifier = MainitemCollectionCallable(MainitemCollectionPart.UsageModifier)

'''
ShortItems
'''

# MainItem
Input = ShortItem(Mainitem.Input)
Output = ShortItem(Mainitem.Output)
Feature = ShortItem(Mainitem.Feature)
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
    print(Collection(0x0aff))
    print(EndCollection())
    Input = ShortItem(Mainitem.Input)
    print(Input(Data, Variable, Absolute))