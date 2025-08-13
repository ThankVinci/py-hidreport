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
                    if(data in UsagePages.keys()):
                        current_page = UsagePages[data]
                    elif(data >= VendordefinedFF00.value() and data <= VendordefinedFFFF.value()):
                        current_page = Page(data)
                    args = f'({current_page.name()})'
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

def main():
    # 键盘
    buff = b'\005\001\t\006\241\001\005\a\031\340)\347\025\000%\001u\001\225\b\201\002\225\001u\b\201\001\225\005u\001\005\b\031\001)\005\221\002\225\001u\003\221\001\225>u\b\025\000&\377\000\005\a\031\000*\377\000\201\000\300'
    buff = b'\005\001\t\006\241\001\205\001\005\a\031\340)\347\025\000%\001u\001\225\b\201\002\031\000*\377\000\025\000&\377\000u\b\225>\201\000\300\005\001\t\200\241\001\205\002\031\201)\203\025\000%\001u\001\225\003\201\002\225\005\201\001\300\005\f\t\001\241\001\205\003\031\000*\377\037\025\000&\377\037u\020\225\001\201\000\300\006\001\377\n\001\377\241\001\205\006\025\000&\377\000\t/u\b\225\003\201\000\300'
    buff = b'\006\001\377\t\001\241\001\t\002u\b\225@\025\000&\377\000\201\002\t\003u\b\225@\025\000&\377\000\221\002\300'
    # 鼠标
    buff = b'\005\001\t\002\241\001\t\001\241\000\005\t\031\001)\020\025\000%\001\225\020u\001\201\002\005\001\026\001\200&\377\177u\020\225\002\t0\t1\201\006\025\201%\177u\b\225\001\t8\201\006\005\f\n8\002\225\001\201\006\300\300'
    buff = b'\005\001\t\006\241\001\205\001\005\a\031\340)\347\025\000%\001u\001\225\b\201\002\201\003\225\006u\b\025\000&\377\000\031\000*\377\000\201\000\300\005\f\t\001\241\001\205\003u\020\225\002\025\001&\214\002\031\001*\214\002\201\000\300\005\001\t\200\241\001\205\004u\002\225\001\025\001%\003\t\202\t\201\t\203\201`u\006\201\003\300\006\000\377\t\001\241\001\205\020u\b\225\006\025\000&\377\000\t\001\201\000\t\001\221\000\300\006\000\377\t\002\241\001\205\021u\b\225\023\025\000&\377\000\t\002\201\000\t\002\221\000\300'
    print(buff, len(buff))
    code = ReportDescParser.parse(buff)
    print(code)
if __name__ == '__main__':
    main()