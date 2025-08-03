if __name__ == '__main__':
    # 进行内部调试时会找不到导入的模块，所以手动添加本程序根目录到sys.path中
    # 需要注意不同层级中root_path需要调用dirname的次数是不一样的
    import sys
    from os.path import dirname, abspath
    root_path = dirname(dirname(dirname(dirname(dirname(dirname(abspath(__file__)))))))
    print(root_path)
    sys.path.append(root_path)

from  py_hidreport.items import Mainitem
from  py_hidreport.items.Main import DataMainItem

class __InputItem(DataMainItem):
    def __init__(self):
        DataMainItem.__init__(self, Mainitem.Input)

Input = __InputItem()

if __name__ == '__main__':
    print(Input())