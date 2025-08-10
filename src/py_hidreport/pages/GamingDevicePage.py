from enum import IntEnum

GamingDevicePageId = 0x92

# 由于GamingDevice相关文档获取方式对于我来说不太方便，所以不支持GamingDevice用途页的详细解码，最多让它能够解析出当前用途页下对应的用途值

class GamingDevicePage(IntEnum):
    Undefined_BEGIN                         = 0x00
    Undefined_END                           = 0xFFFF
    
    @classmethod
    def _missing_(cls, value):
        if cls.Undefined_BEGIN <= value <= cls.Undefined_END:
            __pseudo_member = cls._value2member_map_.get(value)
            if __pseudo_member is None:
                # 构造一个临时的枚举对象
                __pseudo_member = int.__new__(cls, value)
                __pseudo_member._name_ = f"GDP{value:04X}"
                __pseudo_member._value_ = value
                # 缓存以避免重复创建
                cls._value2member_map_[value] = __pseudo_member
                setattr(cls, __pseudo_member._name_, __pseudo_member)
            return __pseudo_member
        raise ValueError(f"{value} is not a valid GamingDevicePage")
    
    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

