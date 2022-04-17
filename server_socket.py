import socket
from config import *


class ServerSoket(socket.socket):
    '''自定义套接字，负责初始化服务器套接字的相关参数'''

    def __init__(self):
        '''设置TCP类型'''
        super(ServerSoket,self).__init__(socket.AF_INET,socket.SOCK_STREAM)
        
        # 绑定地址和端口
        self.bind((SERVER_IP,SERVER_PORT))

        # 设置为监听模式

        
        self.listen(128)

