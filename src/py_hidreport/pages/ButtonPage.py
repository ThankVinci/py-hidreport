from enum import IntEnum

ButtonPageId = 0x09

'''貌似这个按钮页的按钮定义是按优先级逐级递减而按压力度需要逐级递增'''
class ButtonPage(IntEnum):
    NoButtonPressed                         = 0x00
    Button1                                 = 0x01 # Primary
    Button2                                 = 0x02 # Secondary
    Button3                                 = 0x03 # Tertiary
    __Defined_Begin                         = 0x04
    __Defined_End                           = 0xFFFF
    Button                                  = lambda value:ButtonPage(value)

    @classmethod
    def _missing_(cls, value):
        if cls.__Defined_Begin <= value <= cls.__Defined_End:
            __pseudo_member = cls._value2member_map_.get(value)
            if __pseudo_member is None:
                # 构造一个临时的枚举对象
                __pseudo_member = int.__new__(cls, value)
                __pseudo_member._name_ = f"Button{value}"
                __pseudo_member._value_ = value
                # 缓存以避免重复创建
                cls._value2member_map_[value] = __pseudo_member
                setattr(cls, __pseudo_member._name_, __pseudo_member)
            return __pseudo_member
        raise ValueError(f"{value} is not a valid ButtonPage")
    
    def to_bytes(self):
        length = 0
        if(self.bit_length() <= 8):
            length = 1
        elif(self.bit_length() <= 16):
            length = 2
        elif(self.bit_length() <= 32):
            length = 4
        return super().to_bytes(length=length, byteorder='little', signed=False)

