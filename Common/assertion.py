# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/17 10:08
"""

from Tools.handle_mysql import handle_mysql
from Tools.handle_result import handle_result_json
from Tools.handle_excel import excel_data


class assertion_class:

    def assertion(self, excepect_method, excepect_result, res, i, sheet_name, mysql_query):
        '''
        :param excepect_method: 断言方法
        :param excepect_result: 断言内容
        :param res: 网络请求result
        :param i: case_id
        :param sheet_name: sheet名
        :param mysql_query: 数据库表达式
        :return: 返回断言结果
        '''
        try:
            code = res['code']
            # print('code是------------>', code)
            msg = res['msg']
            # print('msg是------------->', msg)
        except Exception as e:
            print('返回的错误结果是:', res)
            excel_data.excel_write_data(i, 15, str(res), sheet_name)
            excel_data.excel_write_data(i, 16, 'ERROR', sheet_name)
            raise e
        result = str(res).encode('UTF-8')
        # 设置编码格式
        excel_data.excel_write_data(i, 15, result, sheet_name)
        if excepect_method == 'code':
            try:
                if excepect_result == code:
                    return True
                else:
                    return False
            except Exception as e:
                print('报错了，错误是:', e)
                raise e
        elif excepect_method == 'msg':
            try:
                if excepect_result == msg:
                    return True
                else:
                    return False
            except Exception as e:
                print('报错了，错误是:', e)
                raise e
        elif excepect_method == 'json':
            try:
                json_res = handle_result_json(res, eval(excepect_result))
                if json_res:
                    return True
                else:
                    return False
            except Exception as e:
                print('报错了，错误是:', e)
                raise e
        elif excepect_method == 'sql':
            try:
                if excepect_result == handle_mysql.fetch_one(mysql_query):
                    return True
                else:
                    return False
            except Exception as e:
                print('报错了，错误是:', e)
                raise e
        elif excepect_method == 'code_msg':
            try:
                excepect_result = str(excepect_result).split('##')
                if excepect_result[0] == str(code) and excepect_result[1] == msg:
                    return True
                else:
                    return False
            except Exception as e:
                print('报错了，错误是:', e)
                raise e
        elif excepect_method == 'result':
            try:
                excepect_result = str(excepect_result).split('##')
                if str(excepect_result[0]) == str(eval(excepect_result[1])):
                    return True
                else:
                    return False
            except Exception as e:
                print('报错了，错误是:', e)
                raise e


# 实例化
ac = assertion_class()
