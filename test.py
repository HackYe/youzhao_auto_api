# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/17 10:58
"""
import re

i = 'S111232'
data = bool(re.search('^O[0-9]*', i)) or bool(re.search('^P[0-9]*', i))
print(data)