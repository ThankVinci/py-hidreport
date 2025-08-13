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
        if(not isinstance(buff, bytes)):
            raise ValueError(f'{buff} is not a bytes')
        idx = 0
        current_page = Undefined # 当前的用例页
        context = ''
        while(idx < len(buff)):
            shortitem = ItemValue(buff[idx])
            if(shortitem == 0):
                raise ValueError(f'{shortitem} is zero')
            item = shortitem.Item()
            size = shortitem.Size()
            idx += 1
            data = int.from_bytes(buff[idx:idx+size], byteorder='little')
            line = f'{item.name()}'
            args = '()'
            if(size > 0):
                args = f'({hex(data)})'
                if(item is Usage and not (current_page is Undefined)):
                    args = f'({current_page.usage(data)})'
                if(item is UsagePage):
                    current_page = UsagePages[data]
                    args = f'({UsagePages[data].name()})'
                if(item is Collection):
                    args = f'({MainitemCollectionPart(data).name})'
                if(item in (Input, Output, Feature)):
                    args = f'({MainitemBitPart.parse(data)})'
            line += args
            idx += size
            context += line
            context += '\n'
        return context
    
    @classmethod
    def parseitem(cls, buff:bytes):
        if(not isinstance(buff, bytes)):
            raise ValueError(f'{buff} is not a bytes')
        if(len(buff) <= 0):
            raise ValueError(f'{buff} is empty')
        # 只用于解析出单个item
        shortitem = ItemValue(buff[0])
        if(shortitem == 0):
            raise ValueError(f'{shortitem} is zero')
        item = shortitem.Item()
        return item
        