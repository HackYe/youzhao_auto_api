# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/13 15:21
"""

from deepdiff import DeepDiff


def handle_result_json(dict1, dict2):
    '''
    校验格式
    '''
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False


if __name__ == "__main__":
    dict2 = {'code': 200, 'data': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZTRlZTUxZjEwOTVhZDUzODAxMjAzODg0MTFkNzU3ZTk3MjFiNDExNGZlYjUxZDA3NzlkYWZiZjQyNjZlNGQwNjQxOTY4MzI4MWQ2MGMyMmIiLCJpYXQiOjE1OTQ2MjE4NzksIm5iZiI6MTU5NDYyMTg3OSwiZXhwIjoxNTk0NjIxOTM5LCJzdWIiOiI2MDgwMDExMjAiLCJpc3MiOiJzYW5qaWVrZS1wcmUiLCJzaWQiOiJlNGVlNTFmMTA5NWFkNTM4MDEyMDM4ODQxMWQ3NTdlOTcyMWI0MTE0ZmViNTFkMDc3OWRhZmJmNDI2NmU0ZDA2NDE5NjgzMjgxZDYwYzIyYiIsInNjb3BlcyI6W119.Q5v7FFHq2DiVFr7xrbfWHdfpVvfZ35edYJxkUJ_hn7l1Rtv79JUPk6ZZSC17JyVjqiF1wbdDp3hfWP6QJgtHjg'}, 'msg': 'ok'}
    dict1 = {'code': 201, 'data': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZTRlZTUxZjEwOTVhZDUzODAxMjAzODg0MTFkNzU3ZTk3MjFiNDExNGZlYjUxZDA3NzlkYWZiZjQyNjZlNGQwNjQxOTY4MzI4MWQ2MGMyMmIiLCJpYXQiOjE1OTQ2MjE4NzksIm5iZiI6MTU5NDYyMTg3OSwiZXhwIjoxNTk0NjIxOTM5LCJzdWIiOiI2MDgwMDExMjAiLCJpc3MiOiJzYW5qaWVrZS1wcmUiLCJzaWQiOiJlNGVlNTFmMTA5NWFkNTM4MDEyMDM4ODQxMWQ3NTdlOTcyMWI0MTE0ZmViNTFkMDc3OWRhZmJmNDI2NmU0ZDA2NDE5NjgzMjgxZDYwYzIyYiIsInNjb3BlcyI6W119.'}, 'msg': 'true'}
    dict3 = {'code': 200, 'data': {'order_info': None, 'order_sn': '20200807105207100rzfu5m', 'pay_done': False, 'pay_url': 'alipay://alipayclient/?%7B%22fromAppUrlScheme%22%3A%22sanjieke%3A%5C%2F%5C%2Fsanjieke.cn%5C%2F%22%2C%22requestType%22%3A%22SafePay%22%2C%22dataString%22%3A%22app_id%3D2016082100305800%26format%3DJSON%26charset%3Dutf-8%26sign_type%3DRSA2%26version%3D1.0%26notify_url%3Dhttp%253A%252F%252Fcashier.pre.sanjieke.cn%252Fapi%252Fnotify%252Falipay%26timestamp%3D2020-08-07%2B10%253A52%253A08%26biz_content%3D%257B%2522out_trade_no%2522%253A%252220200807105208002k2gc9z%2522%252C%2522total_amount%2522%253A2.22%252C%2522subject%2522%253A%2522%255Cu57f9%255Cu8ba1%255Cu6d4b%255Cu8bd51%2B%255Cu57f9%255Cu517b%255Cu8ba1%255Cu5212%255Cu6d4b%255Cu8bd5-%255Cu4e8e%255Cu6d77%255Cu6d0b%255Cuff082%255Cuff09%2522%252C%2522product_code%2522%253A%2522QUICK_MSECURITY_PAY%2522%252C%2522timeout_express%2522%253A%252215m%2522%257D%26method%3Dalipay.trade.app.pay%26sign%3DFf9j6UPNutMHfyYPSSrHr642vGIM7CDMywHcS4XVlOmCnSVuHqxFWySwc8CL0B0zYc14VtLw9CkAZuotsxuEYrDCzZjHGyDwq9iZsyv2u5h3QC71Ac%252B%252FgigCtx9lq%252FTNYiNcr0xeyd35KBKFg3lwtwgjYh41LAo8lB%252FZNaWP4s%252B6I1p6c7GZPAskBvnYfOvxJX%252BdXlg0cV5kjTjrydZEvjVaU14wXwC4JdcznqyEhmaYqJrI1hJ%252B%252BXg%252FGgtrTsQGS7VtZc4L6rtpqCr6nwMxzELbXQpiJ1IfBwk7rd%252FzgeZ1qasX2wLESpPzy2PRJccBbDIU3mZxS8z15vwX%252F4krfg%253D%253D%22%7D'}, 'msg': 'ok'}
    print(handle_result_json(dict1,dict2))
