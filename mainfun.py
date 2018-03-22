__author__ = 'ping'
from django.conf import settings

settings.configure()
# import tcode
from django.template import Context, Template

try:
    f = open(r'H:\aa\tempcode.txt', 'r')
    exec(f.read())
except:
    print('文件操作失败！')
finally:
    if f:
        f.close()

t = Template(ts)
c = Context(tc)
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