from py_hidreport.parser import ReportDescParser
from py_hidreport.items import *
from py_hidreport.usages import *
from py_hidreport.pages import *

def main():
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
    main()