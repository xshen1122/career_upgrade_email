# smth_email.py
# coding: utf-8





from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))



def send_email(total_string):
		# 输入Email地址和口令:
	#from_addr = raw_input('From: ')
	from_addr = 'xushen1122@sina.com'
	# password = raw_input('Password: ')
	password = 'wshaw713' # this is Shouquanma....
	# 输入SMTP服务器地址:
	# smtp_server = raw_input('SMTP server: ')
	smtp_server = 'smtp.sina.com'
	# 输入收件人地址:
	# to_addr = raw_input('To: ')
	to_addr = 'xushen1122@sina.com'
	
	

	msg = MIMEText(total_string, 'plain', 'utf-8')
	msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
	msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
	msg['Subject'] = Header(u'工作列表……' , 'utf-8').encode()

	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()
