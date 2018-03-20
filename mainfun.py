__author__ = 'ping'
from django.conf import settings

settings.configure()
import tcode
from django.template import Context, Template

t = Template(tcode.ts)
c = Context(tcode.tc)
str = t.render(c)
print(str)
try:
    f = open(r'D:\output\gencode_res.txt', 'w')
    f.write(str)
except:
    print('文件操作失败！')
finally:
    if f:
        f.close()