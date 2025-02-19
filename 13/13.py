# Библиотека ipaddress
import ipaddress
from ipaddress import *

# первый и последний Ip адрес - служебные

# построить сеть ip_net(f'{Узел}/{маска}') => сеть

net = ipaddress.ip_network(f'192.168.248.176/255.255.255.240')
for i in net:
    if str(i).count('1') ==  str(i).count('0'):
        print(i)