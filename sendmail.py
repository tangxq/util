"""发送邮件"""
import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger('main.sendreport')

def sendreport(file_new):
    """发送带附件的邮件，邮件正文为读取附件内容"""
    msg = MIMEMultipart()
    with open(file_new, 'rb') as f:
        mail_body = f.read()
    # 添加邮件正文
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
    # 添加附件
    att1 = MIMEText(mail_body, 'html', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(att1)
    # 设定邮件标题
    msg['subject'] = Header('邮件标题', 'utf-8')
    msg['From'] = 'xxxxx@163.com'
    msg['From'] = Header('Tester', 'utf-8')
    # 收件人,设置多个收件人时用;隔开
    msg['To'] = 'xxxxx@163.com'
    try:
        smtp = smtplib.SMTP('smtp.qiye.163.com', '25')
        # smtp.set_debuglevel(1)
        smtp.login('user', 'password')  #登录邮箱的账户和密码
        smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
        smtp.quit()
        print('report has send out!')
        logger.warning('report has send out!')
        return 0
    except smtplib.SMTPException:
        print("Error: report send fail!")
        logger.warning("Error: report send fail!")
        return 1


def sendreport_nofile(strs):
    """发送内容为字符邮件"""
    # 邮件正文
    msg = MIMEText(strs)
    # 邮件标题
    msg['subject'] = Header('邮件标题', 'utf-8')
    msg['From'] = '发件人'
    msg['From'] = Header('Tester', 'utf-8')
    # 收件人，设置多个收件人用;隔开
    msg['To'] = 'xxxx@163.com;xxx@163.com'
    try:
        smtp = smtplib.SMTP('smtp.qiye.163.com', '25')
        # smtp.set_debuglevel(1)
        smtp.login('user', 'password')  # 登录邮箱的账户和密码
        smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
        smtp.quit()
        print('report has send out!')
    except smtplib.SMTPException:
        print("Error: report send fail!")

if __name__ == '__main__':
    sendreport('E:/hui/report/result.html')
