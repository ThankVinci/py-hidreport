# Python USB HID Report Descriptor

A realization of report descriptor parser and codec context.

## parser example

```python
from py_hidreport.items import *
from py_hidreport.usages import *
from py_hidreport.pages import *
from py_hidreport.parser import ReportDescParser
bin = b'\x05\x01\x09\x06\xA1\x01\x05\x07\x19\xE0\x29\xE7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02\x95\x01\x75\x08\x81\x03\x95\x05\x75\x01\x05\x08\x19\x01\x29\x05\x91\x02\x95\x01\x75\x03\x91\x03\x95\x06\x75\x08\x15\x00\x25\x65\x05\x07\x19\x00\x29\x65\x81\x00\xC0'
code:str = ReportDescParser.parse(bin)
prnt(code)
```

## codec example

```python
from py_hidreport.items import *
from py_hidreport.usages import *
from py_hidreport.pages import *
from py_hidreport.ctx import ReportDescStdContext

ReportDescContext.Set(ReportDescStdContext())

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
exec(code)
print(ReportDescContext.Data())

```