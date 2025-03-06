# Библиотека ipaddress
import ipaddress
from ipaddress import *

# первый и последний Ip адрес - служебные

# построить сеть ip_net(f'{Узел}/{маска}') => сеть

net = ipaddress.ip_network(f'192.168.34.0/255.255.255.240')
for i in net:
    print(i)