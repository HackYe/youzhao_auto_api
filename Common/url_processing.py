# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/17 18:45
"""
from Tools.handle_replace import headle_re
from Tools.handle_excel import excel_data


class url_processing:

    def url_re_method(self, url, i, sheet_number, url_value=None, url_list=None):
        '''
        替换url数据
        :param url: url地址
        :param i: case_id号
        :param sheet_number: sheet号
        :param url_value: 读取依赖用例返回的value
        :param url_list: url的列表
        :return: 返回替换好的数据
        '''
        try:
            # rely_key为但个前置条件替换通用str
            if str(url).find('${rely_key}') != -1:
                url = headle_re.str_data('${rely_key}', url,
                                         eval(excel_data.get_cell_value(i, 7, sheet_number)))
            # rely_keys为多个前置条件替换通用str
            elif str(url).find('${rely_keys}') != -1:
                res_data = headle_re.strs_data(url, url_list)
                url = res_data
            return url
        except Exception as e:
            print('Url替换数据出错误了，错误信息是', e)


up = url_processing()
