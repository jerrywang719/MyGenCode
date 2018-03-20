__author__ = 'ping'

ts = '''
{% for item in lis %}    {{ item }}
{% endfor %}
'''
ts = ts.strip()
tc = {'num': 30,'lis':['first','second','third']}