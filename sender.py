from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = '04parti85@gmail.com'
    receivers = '1155191951@link.cuhk.edu.hk'
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('Lambert', 'utf-8')
    message['To'] = Header('Matthew', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.gmail.com', 587)
    # 请自行修改下面的登录口令
    smtper.ehlo()
    smtper.starttls()
    smtper.ehlo()
    smtper.login(sender, 'rmjpymbgqtxnnchy')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('邮件发送完成!')


if __name__ == '__main__':
    main()