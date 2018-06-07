# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



class E_mail:
    
    def __init__(self, my_email, password, target_addr):
        self.from_addr = my_email
        self.password = password
        self.to_addr = target_addr
        self.smtp_server = 'smtp.'+ my_email[  my_email.find('@')+1  : ]
        self.msg = '占位符'
        self.server = smtplib.SMTP(self.smtp_server, 25)
        self.server.login(self.from_addr, self.password)


    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr(  (Header(name, 'utf-8').encode(), addr)  )


    def message_txt(self, sender, title, content):
        self.msg = MIMEText(content, 'plain', 'utf-8')
        self.msg['From'] = self._format_addr(sender + ' <%s>' % self.from_addr)
        self.msg['To'] = self._format_addr('admin <%s>' % self.to_addr)
        self.msg['Subject'] = Header(title, 'utf-8').encode()


    def message_file(self, sender, title, content, file):
        self.msg = MIMEMultipart()
        self.msg['From'] = self._format_addr('sender <%s>' % self.from_addr)
        self.msg['To'] = self._format_addr('admin <%s>' % self.to_addr)
        self.msg['Subject'] = Header(title, 'utf-8').encode()
        self.msg.attach(MIMEText(content, 'plain', 'utf-8'))
        with open(file, 'rb') as f:
            mime = MIMEBase('image', 'png', filename='test.png')
            mime.add_header('Content-Disposition', 'attachment', filename='img.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            self.msg.attach(mime)


    def send_out(self):
       # server.set_debuglevel(1)
        self.server.sendmail(self.from_addr, self.to_addr, self.msg.as_string())
        print('已发送')
        
    def q(self):
        self.server.quit()



if __name__ == '__main__':

    ss = E_mail('machaooyeah@163.com', 'dddd1314', 
                ['1209113666@qq.com','673017599@qq.com'])    
#    ss.message_txt('嘿呀','python','这是一个用python发送的邮件')
    ss.message_file('开局一条鲲','养鲲','大鲲',"D:\\n.jpg")
    ss.send_out()
    ss.q()









