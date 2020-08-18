# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/14 15:33
"""
from Common.html_read import one_click_reading
import time
import requests


def robot_push(report):
    new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=74ca4fb9-4025-447e-adfa-5ede5dbc3095'
    header = {'Content-Type': 'application/json'}
    data = {'msgtype': 'text',
            'text': {'content': '这是三节课app接口的测试报告，请查收！\n测试时间：{0}\n测试结果：{1}'.format(new_time, one_click_reading(report)),
                     'mentioned_list': ['@all']}
            }
    try:
        res = requests.post(url, headers=header, json=data, verify=False)
        print('Push信息成功')
        return res
    except Exception as e:
        print('发送失败，原因是', e)


if __name__ == '__main__':
    data = '../Outputs/html/2020-08-13-14-53-57_report.html'
    print(robot_push(data))
