# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/17 18:52
"""
from Tools.handle_replace import headle_re
from Common.get_data import gd


class mysql_processing:

    def mysql_re_method(self, mysql_query):
        '''
        替换mysql的方法
        :param mysql_query: 数据库表达式
        :return: 返回替换好的数据
        '''
        try:
            if str(mysql_query).find('${phone}') != -1:
                mysql_query = headle_re.str_data('${phone}', mysql_query, gd.get_phone())
            elif str(mysql_query).find('${new_phone}') != -1:
                mysql_query = headle_re.str_data('${new_phone}', mysql_query, gd.get_new_phone())
            return mysql_query
        except Exception as e:
            print('Mysql替换数据出错误了，错误信息是', e)


mp = mysql_processing()
