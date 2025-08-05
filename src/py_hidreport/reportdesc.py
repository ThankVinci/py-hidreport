from enum import IntEnum
from typing import Callable, Any

if __name__ == '__main__':
    # 进行内部调试时会找不到导入的模块，所以手动添加本程序根目录到sys.path中
    # 需要注意不同层级中root_path需要调用dirname的次数是不一样的
    import sys
    from os.path import dirname, abspath
    root_path = dirname(dirname(abspath(__file__)))
    print(root_path)
    sys.path.append(root_path)

# 用于创建报告描述符
# 能够序列化描述符为二进制流，也能够反序列化回来
# 具有检查描述符格式是否正常的功能

# 报告描述符状态机
# 可以检查和添加一行描述符，如果描述符不符合规则则报错

from py_hidreport.Items import *
from py_hidreport.hidusage import *
from py_hidreport.pages import Pages

class ReportDescState(IntEnum):
    INITIAL     = 0
    MAINITEM    = 1
    GLOBALITEM  = 2
    LOCALITEM   = 3

class ReportDescDecoder:
    def __init__(self):
        ...
    
    def decode(self, buff:bytes):
        idx = 0
        print(len(buff))
        current_page = UsagePages.Undefined # 当前的用例页
        context = ''
        while(idx < len(buff)):
            bTagType = buff[idx] & 0xfc
            if(bTagType == 0):
                print('error')
                break
            item = ShortItem(bTagType)
            bSize = buff[idx] & 0x03
            size = HIDItemsize[bSize]
            idx += 1
            data = int.from_bytes(buff[idx:idx+size], byteorder='little')
            line = f'{item.getname()}'
            if(current_page != UsagePages.Undefined and item == Usage):
                line += f'({Pages[current_page](data).name})'
            else:
                line += f'({hex(data)})'
            # print(current_page.name)
            # print(item)
            # print(UsagePage)
            if(item == UsagePage):
                current_page = UsagePages(data)
            idx += size
            context += line
            context += '\n'
        return context
    
    def next(self):
        ...

class ReportDescStateMachine:
    def __init__(self):
        self.__state = ReportDescState.INITIAL
        self.__data  = b''
    
    def append(self, shortitem:ShortItem, arg:Any):
        self.__data += shortitem(arg)

    def serialize(self):
        return self.__data        

class ReportDescSerializer:
    def __init__(self):
        pass

class ReportDescDeSerializer:
    def __init__(self):
        pass

def main():
    statemachine = ReportDescStateMachine()
    statemachine.serialize()

if __name__ == '__main__':
    decoder = ReportDescDecoder()
    context = decoder.decode(b'\x05\x01\x09\x06\xA1\x01\x05\x07\x19\xE0\x29\xE7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02\x95\x01\x75\x08\x81\x03\x95\x05\x75\x01\x05\x08\x19\x01\x29\x05\x91\x02\x95\x01\x75\x03\x91\x03\x95\x06\x75\x08\x15\x00\x25\x65\x05\x07\x19\x00\x29\x65\x81\x00\xC0')
    exec(context)
    print(context)
    UsagePage(0x1)
    Usage(Keyboard)
    Collection(0x1)
    UsagePage(0x7)
    UsageMinimum(0xe0)
    UsageMaximum(0xe7)
    LogicalMinimum(0x0)
    LogicalMaximum(0x1)
    ReportSize(0x1)
    ReportCount(0x8)
    Input(0x2)
    ReportCount(0x1)
    ReportSize(0x8)
    Input(0x3)
    ReportCount(0x5)
    ReportSize(0x1)
    UsagePage(0x8)
    UsageMinimum(0x1)
    UsageMaximum(0x5)
    Output(0x2)
    ReportCount(0x1)
    ReportSize(0x3)
    Output(0x3)
    ReportCount(0x6)
    ReportSize(0x8)
    LogicalMinimum(0x0)
    LogicalMaximum(0x65)
    UsagePage(0x7)
    UsageMinimum(0x0)
    UsageMaximum(0x65)
    # Input(0x0)
    EndCollection(0x0)