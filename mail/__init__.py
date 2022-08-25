import smtplib
from email.mime.text import MIMEText


def sendmail(content, mail):

    # 邮箱服务端-自己填写（如果是qq邮箱就把163改成qq）
    mail_server = 'smtp.163.com'
    # 发件人邮箱-自己填写
    sender_mail = 'xxx'
    # 邮箱发件授权码-自己填写
    mail_authcode = 'xxx'
    # 定义邮件的接收者
    received_mail = [mail]

    # 纯文本形式的邮件内容的定义，通过MIMEText进行操作，plain为默认的文本的展示形式
    email = MIMEText('', 'plain', 'utf-8')  # 此处第一个参数为邮件内容
    email['Subject'] = content  # 此处content为主题
    email['From'] = sender_mail  # 发件人
    email['To'] = ','.join(received_mail)  # 收件人

    # 发送邮件
    # 一般邮箱的端口号是465，具体邮箱端口号可自行百度，一般使用SMTP即可，SSL可选
    smtp = smtplib.SMTP_SSL(mail_server, port=465)
    smtp.login(sender_mail, mail_authcode)
    smtp.sendmail(sender_mail, ','.join(received_mail), email.as_string())

    smtp.quit()
    print('恭喜，邮件发送成功!')
