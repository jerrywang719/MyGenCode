__author__ = 'ping'
from django.conf import settings
settings.configure()

from django.template import Context, Template
s = '''{% if num <= 100 and num >= 0 %}
num在0到100之间
{% else %}
数值不在范围之内！
{% endif %}'''
t = Template(s)
c = Context({'num': 30})
str = t.render(c)
print(str)