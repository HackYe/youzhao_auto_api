# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/17 17:13
"""
from Tools.handle_replace import headle_re
from Common.get_data import gd
from Tools.handle_mysql import handle_mysql
from Tools.handle_excel import excel_data
import json


class data_processing:

    def data_re_method(self, data, mysql_query, i, sheet_number, data_value=None, data_list=None):
        '''
        替换data封装
        :param data: 需要替换的data
        :param mysql_query: 数据库查询语句
        :param sheet_number: sheet号
        :param data_value: 读取依赖用例返回的value
        :param data_list: data列表
        :return: 替换好的data
        '''
        try:
            # 1.处理替换手机逻辑
            if str(data).find('${phone}') != -1:
                data = eval(headle_re.str_data('${phone}', data, gd.get_phone()))
                if str(data).find('${sql}') != -1:
                    data = eval(headle_re.str_data('${sql}', data, handle_mysql.fetch_one(mysql_query)))

            # 2.设置密码逻辑
            elif str(data).find('${pwd}') != -1:
                data = eval(headle_re.str_data('${pwd}', data, gd.get_password()))
                if str(data).find('${rely_key}') != -1:
                    data = eval(
                        headle_re.str_data('${rely_key}', data,
                                           eval(excel_data.get_cell_value(i, 5, sheet_number))))

            # 3.处理修改密码逻辑
            elif str(data).find('${newpassword}') != -1:
                data = eval(headle_re.str_data('${newpassword}', data, gd.get_new_password()))
                if str(data).find('${repeat_password}') != -1:
                    data = eval(headle_re.str_data('${repeat_password}', data, gd.get_password()))
                    if str(data).find('${rely_key}') != -1:
                        data = eval(
                            headle_re.str_data('${rely_key}', data,
                                               eval(excel_data.get_cell_value(i, 5, sheet_number))))

            # 4.处理修改手机号逻辑
            elif str(data).find('${new_phone}') != -1:
                data = eval(headle_re.str_data('${new_phone}', data, gd.get_new_phone()))
                if str(data).find('${sql}') != -1:
                    data = eval(headle_re.str_data('${sql}', data, handle_mysql.fetch_one(mysql_query)))
                    if str(data).find('${rely_key}') != -1:
                        data = eval(
                            headle_re.str_data('${rely_key}', data,
                                               eval(excel_data.get_cell_value(i, 5, sheet_number))))

            # 5.transaction_id随机数生成（固定sjk+时间戳）
            elif str(data).find('${transaction_id}') != -1:
                data = headle_re.str_data('${transaction_id}', data, 'SJK' + str(gd.get_Timestamp()))
                if str(data).find('${rely_keys}') != -1:
                    res_data = headle_re.strs_data(data, data_list)
                    data = eval(res_data)

            # 6.处理验证码和更换手机号token逻辑
            elif str(data).find('${sql}') != -1:
                data = headle_re.str_data('${sql}', data, handle_mysql.fetch_one(mysql_query))
                if str(data).find('${rely_key}') != -1:
                    data = eval(
                        headle_re.str_data('${rely_key}', data,
                                           eval(excel_data.get_cell_value(i, 5, sheet_number))))

            # 7.处理修改手机号不需要验证码逻辑
            elif str(data).find('${new_phone_no_code}') != -1:
                data = headle_re.str_data('${new_phone_no_code}', data, gd.get_new_phone())
                if str(data).find('${rely_key}') != -1:
                    data = eval(
                        headle_re.str_data('${rely_key}', data,
                                           eval(excel_data.get_cell_value(i, 5, sheet_number))))

            # 8.rely_key为单个前置条件替换通用str
            elif str(data).find('${rely_key}') != -1:
                data = eval(headle_re.str_data('${rely_key}', data,
                                               eval(excel_data.get_cell_value(i, 5, sheet_number))))

            # 9.rely_keys为多个前置条件替换通用str
            elif str(data).find('${rely_keys}') != -1:
                res_data = headle_re.strs_data(data, data_list)
                data = eval(res_data)

            # 10.替换SQL逻辑
            elif str(data).find('${sql}') != -1:
                data = eval(headle_re.str_data('${sql}', data, handle_mysql.fetch_one(mysql_query)))

            else:
                data = eval(data)
            return data
        except Exception as e:
            print('Data替换数据出错误了，错误信息是', e)


dp = data_processing()
