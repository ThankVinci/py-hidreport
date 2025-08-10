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

from py_hidreport.items import *
from py_hidreport.usages import *
from py_hidreport.pages import *

class ReportDescParser:
    @classmethod
    def parse(cls, buff:bytes)->str:
        idx = 0
        current_page = Undefined # 当前的用例页
        context = ''
        while(idx < len(buff)):
            shortitem = ItemValue(buff[idx])
            if(shortitem == 0):
                print('error')
                break
            item = shortitem.Item()
            size = shortitem.Size()
            idx += 1
            data = int.from_bytes(buff[idx:idx+size], byteorder='little')
            line = f'{item.name()}'
            args = '()'
            if(size > 0):
                args = f'({hex(data)})'
                if(current_page != Undefined and item == Usage):
                    args = f'({current_page.usage(data)})'
                if(item == UsagePage):
                    current_page = UsagePages[data]
                    args = f'({UsagePages[data].name()})'
                if(item == Collection):
                    args = f'({MainitemCollectionPart(data).name})'
                if(item in (Input, Output, Feature)):
                    args = f'({MainitemBitPart.parse(data)})'
            line += args
            idx += size
            context += line
            context += '\n'
        return context

def main():
    bin = b'\x05\x01\x09\x06\xA1\x01\x05\x07\x19\xE0\x29\xE7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02\x95\x01\x75\x08\x81\x03\x95\x05\x75\x01\x05\x08\x19\x01\x29\x05\x91\x02\x95\x01\x75\x03\x91\x03\x95\x06\x75\x08\x15\x00\x25\x65\x05\x07\x19\x00\x29\x65\x81\x00\xC0'
    code:str = ReportDescParser.parse(bin)
    print(bin)
    code = code.replace('\n', '+')[0:-1]
    bin = eval(code)
    print(bin)
    # print(bin)
    code:str = ReportDescParser.parse(bin)
    # # code = code.replace('\n', '+')[0:-1]
    # code = 'UsagePage(Unicode)+Usage(0xffaa)'
    # bin = eval(code)
    # code = ReportDescParser.parse(bin)
    # print(code)
    # Usage(UnicodePage.UFFAA)
    print(UsagePage(GenericDesktop))
    print(UsagePage(GenericDesktop))
    print(UsagePage(GenericDesktop))
    print(LogicalMinimum(0xffffff))

def main2():
    code = '''UsagePage(GenericDesktop)
    Usage(GenericDesktopPage.Mouse)
    Collection(Application)
    Usage(GenericDesktopPage.Pointer)
    Collection (Physical)
    UsagePage (Button) 
    UsageMinimum (1)
    UsageMaximum (3)
    LogicalMinimum (0)
    LogicalMaximum (1)
    ReportCount (3)
    ReportSize (1)
    Input (Data, Variable, Absolute)
    ReportCount (1)
    ReportSize (5)
    Input (Constant)
    UsagePage (GenericDesktop)
    Usage (GenericDesktopPage.X)
    Usage (GenericDesktopPage.Y)
    LogicalMinimum (-127)
    LogicalMaximum (127)
    ReportSize (8)
    ReportCount (2)
    Input(Data, Variable, Relative)
    EndCollection()
    EndCollection()
    '''
    code = code.replace('\n','+')
    code = code.replace(' ','')
    code = code[:-1]
    # print(code)
    bin = eval(code)
    print(bin)
    code = ReportDescParser.parse(bin)
    # print(code)
    code = code.replace('\n','+')
    code = code.replace(' ','')
    code = code[:-1]
    bin = eval(code)
    print(bin)
    

if __name__ == '__main__':
    main2()