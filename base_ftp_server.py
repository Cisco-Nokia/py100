#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

"""
编写一个简易的ftp server
"""


# 实例化用户，这是ftp验证的首要条件
authorizer = DummyAuthorizer()
# 添加用户的相关信息，具体参数可以查看DummyAuthorizer类中的add_user方法
authorizer.add_user("user", "12345", "/home/", perm="elradfmw")
# 添加匿名用户
authorizer.add_anonymous("/home/lynn")
#初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer
# 添加FTP被动模式的端口
handler.passive_ports = range(2000, 2333)
# 监听ip和端口
server = FTPServer(("0.0.0.0", 21), handler)
# 开始服务
server.serve_forever()