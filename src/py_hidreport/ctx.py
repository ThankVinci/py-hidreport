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

# 此处可以自定义Context, 只要继承ReportDescContext, 并注册为ReportDescContext的唯一实例，那么在调用shortitem的时候就会自动将一部分数据传到context
# 那么就可以进行描述符状态解析，如果有异常可以在context这边raise出错误
class ReportDescDefContext(ReportDescContext):
    def push(self, buff:bytes):
        super().push(buff)