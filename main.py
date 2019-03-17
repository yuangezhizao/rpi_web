#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
'''
    :Author: yuangezhizao
    :Time: 2019/3/17 0017 19:39
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
'''
from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
