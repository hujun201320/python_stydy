from window_login import WindowLogin
from request_protocol import RquestProtocol
from client_socket import ClientSocket
from threading import Thread
from config import *


class Client(object):

    def __init__(self):
        '''初始化客户端资源'''
        # 初始化登录窗口
        self.window = WindowLogin()
        self.window.on_reset_button_click(self.clear_inputs)
        self.window.on_login_button_click(self.send_login_data)

        # 创建客户端套接字
        self.conn = ClientSocket()


        # 初始化消息处理函数
        self.response_handle_function = {}
        self.response_handle_function[RESPONSE_LOGIN_RESULT] = self.response_login_handle
        self.response_handle_function[RESPONSE_CHAT] = self.response_chat_handle


    def startup(self):
        '''开启窗口'''
        self.conn.connect()
        Thread(target=self.response_handle).start()#创建并开启一个子线程来接收消息
        self.window.mainloop()

    def clear_inputs(self):
        '''清空窗口内容'''
        self.window.clear_username()
        self.window.clear_password()

    def send_login_data(self):
        '''发送登录消息到服务器'''
        # 获取到用户输入的账号密码
        username = self.window.get_username()
        password = self.window.get_password()

        # 生成协议文本
        request_text = RquestProtocol.request_login_result(username, password)

        # 发送协议文本到服务器
        print('发送给服务器的登录文本为：'+request_text)
        self.conn.send_data(request_text)
        recv_data = self.conn.recv_data()
        print(recv_data)

    def response_handle(self):
        '''不断的接收服务器的新消息'''
        while True:
           # 获取服务器消息
           recv_data = self.conn.recv_data()
           print('收到服务器消息了：'+ recv_data)

           # 解析消息内容
           response_data = self.parse_response_data(recv_data)

           # 根据消息内容分别进行处理
           handle_function = self.response_handle_function[response_data['response_id']]

           if handle_function():
               handle_function(response_data)
        #    if response_data['response_id'] == RESPONSE_LOGIN_RESULT:
        #        self.response_login_handle(response_data)
        #    elif response_data['response_id'] == RESPONSE_CHAT:
        #        self.response_chat_handle(response_data)


    def parse_response_data(self,recv_data):
        '''
        登录的响应消息：1001|成功|失败|昵称|账号
        聊天的响应消息：1002|发送者的昵称|消息内容
        '''

        response_data_list = recv_data.split(DELIMITER)

        # 解析消息的各个组成部分
        response_data = dict()
        response_data['response_id'] = response_data_list[0]

        if response_data['response_id'] == RESPONSE_LOGIN_RESULT:
            '''登录结果的响应'''
            response_data['result'] = response_data_list[1]
            response_data['nickname'] = response_data_list[2]
            response_data['username'] = response_data_list[3]

        elif response_data['response_id'] == RESPONSE_CHAT:
            # 聊天信息的响应
            response_data['nickname'] = response_data_list[1]
            response_data['message'] = response_data_list[2]

        return response_data

    def response_login_handle(self,response_data):
        '''登录结果响应'''
        print('接收到登录信息~~',response_data)

    def response_chat_handle(self,response_data):
        '''聊天信息响应'''
        print('接收到聊天消息~~~',response_data)
            






if __name__ == '__main__':
    client = Client()
    client.startup()
