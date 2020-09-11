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
        response = requests.post(url=url, data=data, headers=header, files=file, cookies=cookie,
                                 proxies=gd.get_proxies())
        res = response.text
        return res

    def send_post_json(self, url, data, header=None, file=None, cookie=None):
        '''
        发送post请求
        '''
        response = requests.post(url=url, json=data, headers=header, files=file, cookies=cookie,
                                 proxies=gd.get_fixed_proxies())
        res = response.text
        return res

    def send_get(self, url, data, header=None, file=None, cookie=None):
        '''
        发送get请求
        '''
        response = requests.get(url=url, params=data, headers=header, files=file, cookies=cookie,
                                proxies=gd.get_proxies())
        res = response.text
        return res

    def send_get_json(self, url, data, header=None, file=None, cookie=None):
        '''
        发送get请求
        '''
        response = requests.get(url=url, json=data, headers=header, files=file, cookies=cookie,
                                proxies=gd.get_fixed_proxies())
        res = response.text
        return res

    def send_put(self, url, data, header=None, file=None, cookie=None):
        '''
        发送put请求
        '''
        response = requests.put(url=url, data=data, headers=header, files=file, cookies=cookie,
                                proxies=gd.get_proxies())
        res = response.text
        return res

    def send_delete(self, url, data, header=None, file=None, cookie=None):
        '''
        发送put请求
        '''
        response = requests.delete(url=url, data=data, headers=header, files=file, cookies=cookie,
                                   proxies=gd.get_proxies())
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
                if 'automation' not in url:
                    res = self.send_post_json(url, data, header, file, cookie)
                else:
                    res = self.send_post(url, data, header, file, cookie)
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
    data = {"id": "", "user_role_id": "10", "user_id": "608001695"}
    home_url = 'http://home.pre.sanjieke.cn/api/app-youzhao/invitation/code/add'
    home_data = {"type":10,"invitation_times":1,"user_ids":["608001821"],"invitation_code_num":1,"status":10}
    header = {'Accept': '*/*',
              'Content-Type': 'application/json',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Cookie': 'admin_id=10000050; admin_jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDAzOTQwODgsImlkIjoxMDAwMDA1MCwiaXNzIjoic2prLXpldXMtc3lzdGVtIiwibmFtZSI6Inl1YW55ZSIsIm9yaWdfaWF0IjoxNTk5Nzg5Mjg4LCJ1aWQiOjEwMDAwMDUwLCJ1bmFtZSI6Inl1YW55ZSJ9.kXl1SDoPVh6m3OdNvqpZMk8IApDvQLkrx-k0Ln9xtUhEVuv-QnXsOvOGfqsbROb0x1KeHW7jp0rWmc35w-men4Mb56d0Ng9D-S1RISCZ8lhO6L0lbI6b6hnI3zE0BHbDnQNW7owYXTes0pUz0_4dIvD3lZxk5acZZ3envZG_3k8; admin_login_time=1599789288; admin_name=%E8%A2%81%E9%87%8E; admin_phone=18500336630; admin_sign=7fd7092a4e51fe954108bae06aa4f93b; home_login_id=10000050; home_login_key=594ebCgiGzdbm9xQQyk%2B81O8BuJ6au3obOUlm1sFICgNuVxwmw; home_login_name=%E8%A2%81%E9%87%8E; home_login_phone=18500336630'}
    res = request.run_main('post', home_url, home_data, header)
    print(res)
