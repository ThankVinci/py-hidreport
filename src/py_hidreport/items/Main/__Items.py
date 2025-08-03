from __future__ import annotations # 延迟类型解析, 使得包内一些__私有的类型也可以作为另一个类型的参数类型注解, 也可以避免循环引用的问题
from enum import IntEnum
from typing import Tuple

if __name__ == '__main__':
    # 进行内部调试时会找不到导入的模块，所以手动添加本程序根目录到sys.path中
    # 需要注意不同层级中root_path需要调用dirname的次数是不一样的
    import sys
    from os.path import dirname, abspath
    root_path = dirname(dirname(dirname(dirname(dirname(dirname(abspath(__file__)))))))
    print(root_path)
    sys.path.append(root_path)

from  py_hidreport.items import ShortItem, Mainitem

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

NonDataMainItem = ShortItem

class DataMainItem(ShortItem):
    def __init__(self, tag):
        ShortItem.__init__(self, tag)
        self.bitvalues = 0
        self.bitcount = 0 # 比特数量
    
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

    def __call__(self, *arg:Tuple[__BitSetCallable]):
        # 初始化
        self.bitvalues = 0
        self.bitcount = 0
        if(isinstance(arg, tuple)):
            for i in range(len(arg)):
                caller = arg[i]
                caller(self)
        __size = self.__getbitsize()
        __arg = self.bitvalues
        __data = __arg.to_bytes(length=__size, byteorder='little')
        __tag_v = self.tag | __size
        return __tag_v.to_bytes(length=1) + __data

class __BitSetCallable:
    def __init__(self, bitvalue:__BitPart, bitpos:int):
        self.__bit = bitvalue
        self.__pos = bitpos
    
    def __call__(self, obj:DataMainItem):
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

if __name__ == '__main__':
    Input = DataMainItem(Mainitem.Input)
    print(Input(Data, Variable, Absolute))