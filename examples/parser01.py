from py_hidreport.parser import ReportDescParser
from py_hidreport.items import *
from py_hidreport.usages import *
from py_hidreport.pages import *

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
    

if __name__ == '__main__':
    main()