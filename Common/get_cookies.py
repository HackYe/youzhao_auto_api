# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/21 11:23
"""
import requests


class GetCookies:

    # 获取Cookies
    def get_cookies(self):
        s = requests.Session()
        # 访问宙斯授权
        auth_url = 'http://auth.pre.sanjieke.com/v1/users/login'
        # 宙斯授权data
        auth_data = {'username': 'yuanye', 'password': 'Aa123123', 'loginType': '1', 'code': '',
                     'service': 'http://pre.admin.sanjieke.cn/Index/index'}
        # 获取票据id
        ticket_url = 'http://auth.pre.sanjieke.com/v1/cas/ticket'
        auth_res = s.post(url=auth_url, data=auth_data)
        auth_res_tgc = auth_res.json()['data']['tgt']
        ticket_data = {'tgc': '{0}'.format(auth_res_tgc), 'ty': 'st',
                       'service': 'http://pre.admin.sanjieke.cn/Index/index'}
        ticket_res = s.post(url=ticket_url, data=ticket_data)
        ticket_res_st = ticket_res.json()['data']['st']
        admin_url = 'http://pre.admin.sanjieke.cn/Index/index'
        admin_data = {'ticket': '{0}'.format(ticket_res_st)}
        s.get(url=admin_url, params=admin_data)
        admin_user_url = 'http://pre.admin.sanjieke.cn/Index/index.html'
        res = s.get(url=admin_user_url)
        cookies = res.request.headers
        cookie = cookies['Cookie']
        return cookie

    # 获取home工作台的Cookie
    def get_home_cookies(self):
        s = requests.Session()
        # 访问宙斯授权
        auth_url = 'http://auth.pre.sanjieke.com/v1/users/login'
        # 宙斯授权data
        auth_data = {'username': 'yuanye', 'password': 'Aa123123', 'loginType': '1', 'code': '',
                     'service': 'http://home.pre.sanjieke.cn/sso/admin/login'}
        # 获取票据id
        ticket_url = 'http://auth.pre.sanjieke.com/v1/cas/ticket'
        auth_res = s.post(url=auth_url, data=auth_data)
        auth_res_tgc = auth_res.json()['data']['tgt']
        ticket_data = {'tgc': '{0}'.format(auth_res_tgc), 'ty': 'st',
                       'service': 'http://home.pre.sanjieke.cn/sso/admin/login'}
        ticket_res = s.post(url=ticket_url, data=ticket_data)
        ticket_res_st = ticket_res.json()['data']['st']
        home_url = 'http://home.pre.sanjieke.cn/sso/admin/login/'
        home_data = {'ticket': '{0}'.format(ticket_res_st)}
        s.get(url=home_url, params=home_data)
        home_user_url = 'http://home.pre.sanjieke.cn'
        res = s.get(url=home_user_url)
        cookies = res.request.headers
        cookie = cookies['Cookie']
        return cookie


gc = GetCookies()

if __name__ == '__main__':
    print(gc.get_home_cookies())
