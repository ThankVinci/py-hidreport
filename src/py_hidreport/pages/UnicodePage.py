from enum import IntEnum

UnicodePageId = 0x10

# 此处不做严格的限制，只定义Unicode用途页的范围为0x0000~0xFFFF
class UnicodePage(IntEnum):
    U0000   = 0x0000,
    UFFFF   = 0xFFFF

    @classmethod
    def _missing_(cls, value):
        if cls.U0000 <= value <= cls.UFFFF:
            __pseudo_member = cls._value2member_map_.get(value)
            if __pseudo_member is None:
                # 构造一个临时的枚举对象
                __pseudo_member = int.__new__(cls, value)
                __pseudo_member._name_ = f"U{value:04X}"
                __pseudo_member._value_ = value
                # 缓存以避免重复创建
                cls._value2member_map_[value] = __pseudo_member
                setattr(cls, __pseudo_member._name_, __pseudo_member)
            return __pseudo_member
        raise ValueError(f"{value} is not a valid UnicodePage")
    
    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)