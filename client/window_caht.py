from tkinter import Toplevel,Text,Button,END,UNITS
from tkinter.scrolledtext import ScrolledText
from time import localtime,strftime,time






class WindowChat(Toplevel):
    


    def __init__(self):
        super(WindowChat,self).__init__()
        # 设置窗口的大小
        self.geometry('%dx%d' % (795,505))


        # 添加组件
        self.add_widget()


        self.on_send_button_click(lambda:self.append_message('张三','你好'))


        # 窗口不可更改
        self.resizable(False,False)




    def add_widget(self):
        '''添加组件的方法'''
        # 聊天区
        chat_text_area = ScrolledText(self)
        chat_text_area['width'] = 110
        chat_text_area['height'] = 30
        chat_text_area.grid(row=0,column=0,columnspan=2)

        chat_text_area.tag_config('green',foreground = '#008B00')
        chat_text_area.tag_config('system',foreground = 'red')
        self.children['chat_text_area'] = chat_text_area


        # 输入区
        chat_input_area = Text(self,name='chat_input_area')
        chat_input_area['width'] = 100
        chat_input_area['height'] = 7
        chat_input_area.grid(row=1,column=0,pady=10)

        # 发送按钮
        send_button = Button(self,name = 'send_button')
        send_button['text'] = '发送'
        send_button['width'] = 5
        send_button['height'] = 2
        send_button.grid(row=1,column=1)

    def notice_button(self):
        noticeButton =Button(self,name='notice_buton')
        noticeButton['text'] = '接收'
        noticeButton['width'] = 5
        noticeButton['height'] = 2
        noticeButton.grid(row=0,column=0)


    def set_title(self,title):
        '''设置标题'''
        self.title('欢饮%s 进入聊天室' % title)

    def on_send_button_click(self,command):
        '''注册事件，当发送按钮被点击时执行 command方法'''
        self.children['send_button']['command'] = command

    def get_input(self):
        '''获取输入框内容'''
        return self.children['chat_input_area'].get(0.0,END)

    def clear_input(self):
        '''清空输入框内容'''
        self.children['chat_input_area'].delete(0.0,END)

    def append_message(self,sender,message):
        '''添加一条消息到聊天区'''
        send_time =strftime('%Y-%m-%d %H: %M:%S',localtime(time())) 
        send_info = '%s: %s\n' % (sender,send_time)
        # btn = Button(self,name='notice_btn')
        # btn['text'] = '接收'
        # btn['width'] = 5
        # btn['height'] = 2
        # btn.grid(row=0,column=0)
        
        self.children['chat_text_area'].insert(END,send_info,'green')
        self.children['chat_text_area'].insert(END,' '+message+ '\n')

        # 向下滚动屏幕
        self.children['chat_text_area'].yview_scroll(3,UNITS)

    def on_window_closed(self,command):
        '''注册关闭窗口时执行的指令'''
        self.protocol('WM_DELETE_WINDOW',command)


        




if __name__ == '__main__':
    WindowChat().mainloop()
