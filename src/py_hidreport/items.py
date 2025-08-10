from __future__ import annotations # 延迟类型解析, 使得包内一些__私有的类型也可以作为另一个类型的参数类型注解, 也可以避免循环引用的问题
from enum import IntEnum
from typing import Union, Callable, Tuple

__all__ = ['HIDItem_size2bSize', 'HIDItem_bSize2Size', 'ItemValue', 'ArgValue', 
           'ShortItems', 'MainitemCollectionPart', 'MainitemBitPart', 
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

HIDItem_size2bSize = {0:0b00, 1:0b01, 2:0b10, 4:0b11}
HIDItem_bSize2Size = {0b00:0, 0b01:1, 0b10:2, 0b11:4}

class ValueType(int):
    def __new__(cls, *args:Union[tuple, int]):
        __value = 0
        if(isinstance(args, tuple)):
            # item 与 bSize 分开设置的情况
            if(len(args) > 0):
                __item:Union[Mainitem, Globalitem, Localitem] = args[0]
                __value = __item
            if(len(args) > 1):
                __size:int = args[1]
                __value = __value | HIDItem_size2bSize[__size]
        elif(isinstance(args, int)):
            # item整体或者arg值的情况
            __value = args
        return super().__new__(cls, __value)
    
    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        signed = False
        if(self < 0):
            signed = True
        return super().to_bytes(length=length, byteorder='little', signed=signed)

ArgValue = ValueType

ShortItems = {}

class ItemValue(ValueType):
    def bSize(self)->int:
        return self & 0b11
    
    def Item(self)->ShortItem:
        __item = self & 0b11111100
        return ShortItems[__item]

    def Size(self)->int:
        return HIDItem_bSize2Size[self.bSize()]

class ShortItem:
    def __init__(self, item:Union[Mainitem, Globalitem, Localitem]):
        self.__bitvalues = 0
        self.__bitcount = 0
        self.__mainitem = False
        self.__collection= False
        __type = HIDItemtype(item & HIDItemtype.ITEMMASKS)
        if(__type is HIDItemtype.MAINITEM):
            self.__item = Mainitem(item)
            self.__mainitem = True
            self.__collection = self.__item in (Mainitem.Collection, Mainitem.EndCollection)
        elif(__type is HIDItemtype.GLOBALITEM):
            self.__item = Globalitem(item)
        elif(__type is HIDItemtype.LOCALITEM):
            self.__item = Localitem(item)
        else:
            raise ValueError()
        ShortItems[self.__item] = self

    def name(self)->str:
        return self.__item.name
    
    def setbitvalue(self, bit:int, pos:int):
        if(bit == 1):
            self.__bitvalues =  self.__bitvalues | (1 << pos)
        elif(bit == 0):
            self.__bitvalues =  self.__bitvalues & ~(1 << pos)

    def __collectionitemcall(self, *arg):
        if(self.__item is Mainitem.EndCollection):
            __size = 0
            __item = ValueType(self.__item, __size)
            return __item.to_bytes()
        return self.__otheritemcall(*arg)

    def __mainitemcall(self, *arg:Tuple[MainitemBitSetCallable]):
        if(self.__collection):
            return self.__collectionitemcall(*arg)
        self.__bitvalues = 0
        if(isinstance(arg, tuple)):
            for i in range(len(arg)):
                caller = arg[i]
                caller(self)
        __data = ValueType(self.__bitvalues).to_bytes()
        __size = len(__data)
        __item = ItemValue(self.__item, __size).to_bytes()
        return __item + __data

    def __otheritemcall(self, arg:Union[int, bytes, Callable] = 0):
        if(callable(arg)):
            arg = arg()
        if(isinstance(arg, bytes)):
            __data = arg.rjust(4, b'\x00') if len(arg) == 3 else arg[:4] # 如果3字节就对齐到4字节, 其他情况下就[:4], 超过4字节会截断, 使得始终为1、2、4字节
        else:
            __data = ArgValue(arg).to_bytes()
        __size = len(__data)
        __item = ItemValue(self.__item, __size).to_bytes()
        return __item + __data

    def __call__(self, *arg:tuple):
        if(not self.__mainitem or (len(arg) == 1 and not callable(arg[0]))):
            return self.__otheritemcall(*arg)
        else:
            return self.__mainitemcall(*arg)

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
        for i in range(len(MainitemBits)):
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
    
    def __call__(self, item:ShortItem):
        item.setbitvalue(self.__bit, self.__pos)

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

    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

class MainitemCollectionCallable:
    def __init__(self, part:MainitemCollectionPart):
        self.__part = MainitemCollectionPart(part)
    
    def __call__(self):
        return self.__part.to_bytes()

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