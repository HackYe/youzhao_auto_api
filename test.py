# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/17 10:58
"""
# import re
#
# i = 'S111232'
# data = bool(re.search('^O[0-9]*', i)) or bool(re.search('^P[0-9]*', i))
# print(data)

import requests

url = 'http://pre.admin.sanjieke.cn/User/saveRole'
auto_url = 'http://cashier.i.pre.3jk.ink:36008/api/notify/automation'
data = {"id": "", "user_role_id": "10", "user_id": "608001696"}
auto_data = {'transaction_id': 'YZ1599539563779893', 'total_amount': '1', 'order_sn': '123'}
header = {'Accept': '*/*',
          'Content-Type': 'text/plain',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9',
          'Cookie': 'PHPSESSID=sjlq9h8v4ejt114vlgpogo72he; admin_id=10000050; admin_jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTg2MTU3NDYsImlkIjoxMDAwMDA1MCwiaXNzIjoic2prLXpldXMtc3lzdGVtIiwibmFtZSI6Inl1YW55ZSIsIm9yaWdfaWF0IjoxNTk4MDEwOTQ2LCJ1aWQiOjEwMDAwMDUwLCJ1bmFtZSI6Inl1YW55ZSJ9.EbHpXlU7qAl9wOvzHZQo3AIm-9v5oFtgB5LKj5crTFC_fKTPZ_QPcfw8h9HZGcTxJ0OzJcluQCnEAXzhTf8vhGMYPT8cAdKdDTbWqabK7ERBfNy915ghAUMcVKtZYt-S6ni3CRlF3FKUD3CgdtYuMibgpaCoXmthpCwrNVTZNZg; admin_login_time=1598010947; admin_name=%E8%A2%81%E9%87%8E; admin_phone=18500336630; admin_sign=2f2d3af0332b199a978cdb35ac856e02; admin_uid=608001067; admin_uname=Hello'}
res = requests.post(auto_url, data=auto_data)
print(res.json())
