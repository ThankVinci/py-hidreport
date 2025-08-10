from enum import IntEnum

MonitorEnumeratedPageId = 0x81

class MonitorEnumeratedPage(IntEnum):
    Reserved                                = 0x00
    Enum1                                   = 0x01
    Enum2                                   = 0x02
    Enum3                                   = 0x03
    Enum4                                   = 0x04
    __Defined_Begin                         = 0x05
    __Defined_End                           = 0xFFFF
    Enum                                    = lambda value:MonitorEnumeratedPage(value)

    @classmethod
    def _missing_(cls, value):
        if cls.__Defined_Begin <= value <= cls.__Defined_End:
            __pseudo_member = cls._value2member_map_.get(value)
            if __pseudo_member is None:
                # 构造一个临时的枚举对象
                __pseudo_member = int.__new__(cls, value)
                __pseudo_member._name_ = f"Enum{value}"
                __pseudo_member._value_ = value
                # 缓存以避免重复创建
                cls._value2member_map_[value] = __pseudo_member
            return __pseudo_member
        raise ValueError(f"{value} is not a valid MonitorEnumeratedPage")
    
    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)
