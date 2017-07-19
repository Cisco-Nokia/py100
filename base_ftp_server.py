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

# 添加返回给用户的公网ip，由于ftp服务端会在被动模式中，将自己本机的IP地址返回给客户端，
# 但有时候，服务器是通过防火墙进行了地址映射的，因此会将自己的私有IP返回给客户端，从而导致客户端无法连接，
# 这个问题，一般在ftp客户端软件上可以自动或手动修正，但我们最好是告诉客户端公网IP为好。
# handler.masquerade_address = "1.1.1.1"

# 添加FTP被动模式的端口
handler.passive_ports = range(2000, 2333)
# 监听ip和端口
server = FTPServer(("0.0.0.0", 21), handler)
# 开始服务
server.serve_forever()