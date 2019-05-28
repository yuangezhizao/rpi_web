#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
'''
    :Author: yuangezhizao
    :Time: 2019/3/17 0017 19:39
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
