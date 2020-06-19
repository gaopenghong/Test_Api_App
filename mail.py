# # encoding: utf-8
# import os
# import re
# import smtplib
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from socket import gaierror, error
#
#
# project_path = os.path.dirname(os.path.dirname(__file__))
# # 基础路径
# base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
# # 导出、下载文件目录
# export_path = project_path + '/file/export'
# # 导入文件目录
# template_path = project_path + '/file/template'
#
# class Email:
#     def __init__(self, title="自动化测试报告", message='附件为自动化测试报告，欢迎下载 ', path=None):
#         """
#         初始化Email
#         :param title: 邮件标题，必填。
#         :param message: 邮件正文，非必填。
#         :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
#         """
#         self.title = title
#         self.message = message
#         self.files = path
#         self.msg = MIMEMultipart('related')
#
#         self.server = 'smtp.163.com'
#         self.sender = 'gphisf@126.com'
#         self.receiver = '1833016532@qq.com'
#         self.password = 'wsgph666'
#
#     def _attach_file(self, att_file):
#         """将单个文件添加到附件列表中"""
#         att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
#         att["Content-Type"] = 'application/octet-stream'
#         file_name = re.split(r'[\\|/]', att_file)
#         att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
#         self.msg.attach(att)
#
#     def send(self):
#         self.msg['Subject'] = self.title
#         self.msg['From'] = self.sender
#         self.msg['To'] = self.receiver
#
#         # 邮件正文
#         if self.message:
#             self.msg.attach(MIMEText(self.message))
#
#         # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
#         if self.files:
#             if isinstance(self.files, list):
#                 for f in self.files:
#                     self._attach_file(f)
#             elif isinstance(self.files, str):
#                 self._attach_file(self.files)
#
#         # # 连接服务器并发送
#         try:
#             smtp_server = smtplib.SMTP(self.server)  # 连接sever
#         except (gaierror and error) as e:
#             print('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
#         else:
#             try:
#                 smtp_server.login(self.sender, self.password)  # 登录
#             except smtplib.SMTPAuthenticationError as e:
#                 print('用户名密码验证失败！%s', e)
#             else:
#                 smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
#             finally:
#                 smtp_server.quit()  # 断开连接
#                                  '同时检查收件人地址是否正确'.format(self.title, self.receiver))
#                 print('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，同时检查收件人地址是否正确'.format(self.title, self.receiver))
#
#
# def send_email_text(subject, content, filepath, sender, passwd, receivers, email_server='smtp.exmail.qq.com'):
#     # 发送方邮箱   
#     sender = sender
#     # 填入发送方邮箱的授权码
#     passwd = passwd
#     # 收件人邮箱
#     receivers = receivers
#
#     try:
#         s = smtplib.SMTP_SSL()  # 邮件服务器
#         s.connect(email_server, 465)
#         s.login(sender, passwd)
#     except smtplib.SMTPException as e:
#         print("Error, 登录失败")
#     else:
#         print('登录成功')
#         receivers = receivers + ',' + sender
#         msgRoot = MIMEMultipart()
#         part = MIMEText(content, 'html', _charset="utf-8")
#         msgRoot.attach(part)
#         # 添加附件部分
#         for path in filepath:
#             part = MIMEApplication(open(path, 'rb').read())
#             part.add_header('Content-Disposition', 'attachment', filename=path)
#             msgRoot.attach(part)
#         email_receivers = []
#         msg_root_to = ''
#         for receiver in receivers.split(','):
#             if '@' in receiver:
#                 email_receivers.append(receiver)
#                 msg_root_to = msg_root_to+receiver + ','
#             else:
#                 email_receivers.append(receiver + '@foryou56.com')
#                 msg_root_to = msg_root_to+receiver + '@foryou56.com,'
#         msgRoot['Subject'] = subject
#         msgRoot['From'] = sender
#         msgRoot['To'] = msg_root_to
#         s.sendmail(sender, email_receivers, msgRoot.as_string())
#         print("邮件发送成功")
#     finally:
#         s.quit()
#
#
# if __name__ == '__main__':
#     file_path = project_path + '\\report\\report_agent_app.html'
#     em = Email(path=file_path)
#     em.send()
#
#
#
#
#
#
#
