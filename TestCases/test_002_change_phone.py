# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/29 14:22
"""

import unittest
import ddt
from Common.assertion import ac
from Base.base_request import request
from Tools.handle_excel import excel_data
from Tools.handle_init import handle_ini
from Tools.handle_replace import headle_re
from Tools.handle_mysql import handle_mysql
from Common.get_data import gd
from Common.get_cookies import gc
from Common.data_processing import dp
from Common.url_processing import up
from Common.mysql_processing import mp
import time
import json

# sheet下标(从0开始)
sheet_number = 3
# sheet名称(sheet对应的名字)
sheet_name = 'Scene_002'
# 获取token的行号(从1开始)
token_row = 4
# 获取excel
test_data = excel_data.get_excel_data(sheet_number)



@ddt.ddt
class TestRunMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 连接数据库
        handle_mysql.__init__()
        # 每次执行用例前手机号+1
        excel_data.excel_write_data(3, 2, gd.get_phone() + 1)
        # 每次执行用例前修改手机号+1
        excel_data.excel_write_data(4, 2, gd.get_new_phone() + 1)

    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭数据库连接
        handle_mysql.close()

    @ddt.data(*test_data)
    def test_run_case(self, test_data):
        global header, code, msg, data_list, res_data, url_list
        global data_value, url_value
        case_id = test_data[0]
        i = excel_data.get_rows_number(case_id, sheet_number)
        sleep = test_data[18]
        is_run = test_data[2]
        if str(is_run).upper() == 'YES':
            print('正在测试的用例是{}'.format(test_data[1]))
            if sleep != None:
                time.sleep(sleep)
            method = test_data[8]
            url = test_data[7]
            data_condition = test_data[3]
            rely_value = test_data[4]
            url_condition = test_data[5]
            url_rely_value = test_data[6]
            if rely_value != None:
                rely_value = str(rely_value).split(',')
            if url_rely_value != None:
                url_rely_value = str(url_rely_value).split(',')
            # data的前置条件
            if data_condition != None:
                data_list = []
                if str(data_condition).find(',') != -1:
                    rely_key = str(data_condition).split(',')
                    test_value = zip(rely_key, rely_value)
                    for items in test_value:
                        rows_number = excel_data.get_rows_number(items[0], sheet_number)
                        data_value = excel_data.get_cell_value(rows_number, 15, sheet_number)
                        res = eval(items[1])
                        data_list.append(res)
                else:
                    rows_number = excel_data.get_rows_number(data_condition, sheet_number)
                    data_value = excel_data.get_cell_value(rows_number, 15, sheet_number)
            if url_condition != None:
                url_list = []
                if str(url_condition).find(',') != -1:
                    url_rely_key = str(url_condition).split(',')
                    test_value = zip(url_rely_key, url_rely_value)
                    for items in test_value:
                        rows_number = excel_data.get_rows_number(items[0])
                        url_value = excel_data.get_cell_value(rows_number, 15, sheet_number)
                        res = eval(items[1])
                        url_list.append(res)
                else:
                    rows_number = excel_data.get_rows_number(url_condition)
                    url_value = excel_data.get_cell_value(rows_number, 15, sheet_number)
            mysql_query = test_data[17]
            if mysql_query != None:
                mysql_query = mp.mysql_re_method(mysql_query)
            data = test_data[9]
            # 处理url
            if url != None:
                if url_condition == None:
                    url = up.url_re_method(url, i, sheet_number)
                else:
                    url = up.url_re_method(url, i, sheet_number, url_value, url_list)
            # 处理data
            if data != None:
                if data_condition == None:
                    data = dp.data_re_method(data, mysql_query, i, sheet_number)
                else:
                    data = dp.data_re_method(data, mysql_query, i, sheet_number, data_value, data_list)
            is_header = test_data[11]
            if is_header.upper() == 'YES':
                header = eval(handle_ini.get_value(key='header', node='no_token', file_name='header.ini'))
                # print('不带token的header是------>', header)
            elif is_header.upper() == 'TOKEN':
                header = handle_ini.get_value(key='header', node='token', file_name='header.ini')
                # 读取header 新的sheet这块需要更改成获取token的坐标
                header = eval(headle_re.re_data(header, gd.get_token(token_row, 15, sheet_number)))
                # 替换header里变量
                # print('带token的header是------>', header)
            elif is_header.upper() == 'ADMIN':
                # 替换Admin后台header
                header = handle_ini.get_value(key='header', node='Admin', file_name='header.ini')
                header = eval(headle_re.re_data(header, gc.get_cookies()))
                print('获取到的Admin_header是', header)
            else:
                header = None
            file = test_data[16]
            if file != None:
                # 判断是否有值
                file = eval(test_data[16])
            excepect_method = test_data[12]
            excepect_result = test_data[13]
            res = request.run_main(method, url, data, header, file)
            # 断言
            assertion_result = ac.assertion(excepect_method, excepect_result, res, i, sheet_name, mysql_query)
            try:
                self.assertTrue(assertion_result)
                excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
            except Exception as e:
                excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                print('返回的错误结果是:', res)
                raise e
            print('返回的数据是--------->', res)


if __name__ == '__main__':
    unittest.main()
