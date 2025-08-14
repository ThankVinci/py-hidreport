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
from py_hidreport.parser import ReportDescParser

# 此处可以自定义Context, 只要继承ReportDescContext, 并注册为ReportDescContext的唯一实例，那么在调用shortitem的时候就会自动将一部分数据传到context
# 那么就可以进行描述符状态解析，如果有异常可以在context这边raise出错误
class ReportDescDefContext(ReportDescContext):
    def push(self, buff:bytes):
        prev = self.prev()
        if(prev):
            previtem = ReportDescParser.parseitem(prev)
            print(previtem.name())
        super().push(buff)

def main():
    ReportDescContext.Set(ReportDescDefContext())
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
    UsagePage(VendordefinedFF00)
    UsagePage(VendordefinedFF01)
    '''
    code = code.replace('\n','+')
    code = code.replace(' ','')
    code = code[:-1]
    exec(code)
    # print(ReportDescContext.Data())

if __name__ == '__main__':
    main()