# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/9 11:27
"""

import requests
import json
from Tools.handle_init import handle_ini
from Common.get_data import gd


class BaseRequest:
    def send_post(self, url, data, header=None, file=None, cookie=None):
        '''
        发送post请求
        '''
        response = requests.post(url=url, data=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def send_post_json(self, url, data, header=None, file=None, cookie=None):
        '''
        发送post请求
        '''
        response = requests.post(url=url, json=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def send_get(self, url, data, header=None, file=None, cookie=None):
        '''
        发送get请求
        '''
        response = requests.get(url=url, params=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def send_get_json(self, url, data, header=None, file=None, cookie=None):
        '''
        发送get请求
        '''
        response = requests.get(url=url, json=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def send_put(self, url, data, header=None, file=None, cookie=None):
        '''
        发送put请求
        '''
        response = requests.put(url=url, data=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def send_delete(self, url, data, header=None, file=None, cookie=None):
        '''
        发送put请求
        '''
        response = requests.delete(url=url, data=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def run_main(self, method, url, data, header=None, file=None, cookie=None):
        '''
        执行方法，传递method、url、data等参数
        '''
        global res
        base_url = handle_ini.get_value(node=gd.get_env())
        # print(base_url)
        if 'http' not in url:
            url = base_url + url
            if method.upper() == 'GET':
                res = self.send_get(url, data, header, file, cookie)
            elif method.upper() == 'POST':
                res = self.send_post(url, data, header, file, cookie)
            elif method.upper() == 'PUT':
                res = self.send_put(url, data, header, file, cookie)
            elif method.upper() == 'DELETE':
                res = self.send_delete(url, data, header, file, cookie)
            else:
                print('请求错误，请核对！')
        else:
            if method.upper() == 'GET':
                res = self.send_get_json(url, data, header, file, cookie)
            elif method.upper() == 'POST':
                res = self.send_post_json(url, data, header, file, cookie)
            elif method.upper() == 'PUT':
                res = self.send_put(url, data, header, file, cookie)
            elif method.upper() == 'DELETE':
                res = self.send_delete(url, data, header, file, cookie)
            else:
                print('请求错误，请核对！')
        try:
            res = json.loads(res)
        except:
            print('这个结果是一个text')
        # print('------>', res)
        return res


request = BaseRequest()

if __name__ == "__main__":
    # request = BaseRequest()
    # request.run_main('get', '/coupon/list', "{'username':'11111'}")
    url = 'http://pre.admin.sanjieke.cn/User/saveRole'
    data = {"id": "", "user_role_id": "10", "user_id": "608001696"}
    header = {'Accept': '*/*',
              'Content-Type': 'text/plain',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Cookie': 'PHPSESSID=sjlq9h8v4ejt114vlgpogo72he; admin_id=10000050; admin_jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTg2MTU3NDYsImlkIjoxMDAwMDA1MCwiaXNzIjoic2prLXpldXMtc3lzdGVtIiwibmFtZSI6Inl1YW55ZSIsIm9yaWdfaWF0IjoxNTk4MDEwOTQ2LCJ1aWQiOjEwMDAwMDUwLCJ1bmFtZSI6Inl1YW55ZSJ9.EbHpXlU7qAl9wOvzHZQo3AIm-9v5oFtgB5LKj5crTFC_fKTPZ_QPcfw8h9HZGcTxJ0OzJcluQCnEAXzhTf8vhGMYPT8cAdKdDTbWqabK7ERBfNy915ghAUMcVKtZYt-S6ni3CRlF3FKUD3CgdtYuMibgpaCoXmthpCwrNVTZNZg; admin_login_time=1598010947; admin_name=%E8%A2%81%E9%87%8E; admin_phone=18500336630; admin_sign=2f2d3af0332b199a978cdb35ac856e02; admin_uid=608001067; admin_uname=Hello'}
    res = request.run_main('post', url, data, header)
    print(res)
