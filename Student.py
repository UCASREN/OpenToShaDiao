#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time     : 2019/4/11 16:42
@Author   : Hu Renlin
@Contact  : 
@File     : Student.py
@Desc     :
'''
import json
from collections import namedtuple


class Student(object):
    def __init__(self, name=None, age=None, courses=None, family=None):
        self.name = name
        self.age = age
        self.courses = courses
        self.family = family


class course(object):
    def __init__(self, name=None, score=None):
        self.name = name
        self.score = score

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

if __name__ == '__main__':
    name = '小明'
    age = 20
    courses = []
    courses.append(course('语文', 100))
    courses.append(course('数学', 200))
    family = {}
    family['妈妈'] = 'A'
    family['爸爸'] = 'B'
    demo = Student(name, age, courses, family)
    # print(demo.__dict__)
    # for item in demo.courses:
    #     print(item.name, item.score)
    # for key, value in demo.family.items():
    #     print(key, value)

    ## 序列化
    json_data = json.dumps(demo, default=lambda obj: obj.__dict__, ensure_ascii=False)
    print(json_data)

    ## 反序列化
    # x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    demo2 = json.loads(json_data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print(demo2)
    for item in demo2.courses:
        print(item.name, item.score)
    print(demo2.family)
    for key in demo2.family:
        print(key)

