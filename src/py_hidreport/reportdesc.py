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

from py_hidreport.items import *
from py_hidreport.usages import *
from py_hidreport.pages import Pages

class ReportDescParser:
    def parse(buff:bytes):
        idx = 0
        current_page = Undefined # 当前的用例页
        context = ''
        while(idx < len(buff)):
            bTagType = buff[idx] & 0xfc
            if(bTagType == 0):
                print('error')
                break
            item = ShortItems[bTagType]
            bSize = buff[idx] & 0x03
            size = HIDItemsize[bSize]
            idx += 1
            data = int.from_bytes(buff[idx:idx+size], byteorder='little')
            line = f'{item.name()}'
            args = '()'
            if(size > 0):
                args = f'({hex(data)})'
                if(current_page != Undefined and item == Usage):
                    args = f'({current_page.usage(data)})'
                if(item == UsagePage):
                    current_page = Page(data)
                    args = f'({UsagePages(data).name})'
                if(item == Collection):
                    args = f'({MainitemCollectionPart(data).name})'
            line += args
            idx += size
            context += line
            context += '\n'
        return context

def main():
    code = ReportDescParser.parse(b'\x05\x01\x09\x06\xA1\x01\x05\x07\x19\xE0\x29\xE7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02\x95\x01\x75\x08\x81\x03\x95\x05\x75\x01\x05\x08\x19\x01\x29\x05\x91\x02\x95\x01\x75\x03\x91\x03\x95\x06\x75\x08\x15\x00\x25\x65\x05\x07\x19\x00\x29\x65\x81\x00\xC0')
    print(code)
    exec(code)

if __name__ == '__main__':
    main()