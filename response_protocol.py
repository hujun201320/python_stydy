from tkinter.tix import REAL
from config import *

class ResponseProtocol(object):
    # 服务器响应协议格式字符串处理
    
    @staticmethod
    def response_login_result(result,nickname,username):

        '''
        生成用户登录返回的结果字符串
        param:result:值为0表示登录失败，值为1表示登录成功过
        param:nichname:登录用户的昵称，如果登录失败则为空
        param:username:登录用户的账号，如果登录失败则为空
        return:供返回给登录用户的登录结果字符串，
        '''

        return DELIMITER.join([RESPONSE_LOGIN_RESULT,result,nickname,username])

    @staticmethod
    def response_chat(nickname,messages):

        '''
        生成返回给用户的消息字符串
        param:nichname:发消息的用户昵称
        param:message:消息正文
        return:返回给用户的消息字符串
        '''

        return DELIMITER.join([RESPONSE_CHAT,nickname,messages])

    