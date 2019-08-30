# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:57:00 2019

@author: Artemis
"""

from functools import reduce
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

map_result = list(map(lambda x:x*x, [1, 2, 3]))
print(map_result)
    
reduce_result = reduce(lambda x,y: x*y, map_result)
print(reduce_result)

"""map/reduce 作业"""
#第一题
def rename(string):
    return string.lower().capitalize()

map_result = map(rename, ['adam', 'LISA', 'barT'])
print(list(map_result))

#第二题
def prod(l):
    return reduce((lambda x, y: x * y), l)

result = prod([1, 2, 3])
print(result)


"""filter作业"""
def not_prime(num):
    if num == 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(list(filter(not_prime, list(range(1,101)))))

""""decorator 装饰器"""
def log(func):
    # *args 可变参数， **kw是关键字参数 ,常见使用如下
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now(i,j):
    print("2019-8-27",i,j)
    return i, j
print(now(12,24))

######################
import base64
data = {
    "content": "口  厌津增框枕青制  团器编 2895520 家 02018年22月25旦 图 称!常州彤扬国昼伟造有限公司 购 图 毯区园园号90020400560063320 91429207CK86228872302007780 C 买 地址囤：适目常州钟樱经济开发区国园图1801830720819868528618 码 6 国 6 贷物或应税图服图图称 规型国 数 阐险 金 额 图 圈 00 输服图运服务费 园 次 C因 要 一 圖 蛋 联 购 园 记 0 合 旺 罗 阶税合计大写 区园作圆圆叁角分 3 有 月2 之 14 码 函 销 称滴滴出行科技有限公司 图 纳税区正矛园 001201163409833307 话田公 团 账限 注 厦核 田磊 团 张函 销售章 ",
    "height": 2048,
    "orgHeight": 2048,
    "orgWidth": 2731,
    "prism_version": "1.0.9",
    "prism_wnum": 70
    }

encode_json = (base64.b64encode(str(data).encode(encoding='utf-8'))).decode()
print(encode_json)
decode_json = (base64.b64decode(encode_json)).decode()
print(decode_json)
print(type(decode_json))

#################################
from pathlib import Path
p1 = Path('/') / 'home' / 'data/img'
print(p1)

p2 = Path('.')
l = [i for i in p2.iterdir() if i.is_dir()]
print(p2.resolve())

print(list(map(str,list(p2.rglob('*')))))
p3 = Path('1.txt')
print(p3.resolve())
print(p3.cwd())

#########################################
import functools
int16 = functools.partial(int, base=16)
print(int16('465465'))

################################
class Screen(object):
    #@property装饰器负责把一个方法变成属性调用   
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height
        
    @property
    def resolution(self):
        return self._height * self._width
    
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
    
#######################################
from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr'))
print(type(Month))
print(Month.Jan) 
print(Month.__members__.items()) 
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender=Enum('Gender',('Male', 'Female'))):
        self.name = name
        self.gender = gender
        
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
    
#################################



