# coding: utf-8
import re
import urllib
import xml.etree.cElementTree as ET
import time
def get_url(xml):
	s=re.findall('href="/article.{100}',xml)
	return s
# mystring = 'href="/article/Career_Upgrade/434699">【pica8北京品科】自动化测试开发工程师</a>(0)</div><div>2016-'
# mystring1 = 'href="/article/Career_Upgrade/434617">【校招/社招】【中国科学院信息工程研究所】系统运维工'

def get_article_flag(mystring):
	s = re.findall('测试',mystring)

	if s != []:
		return True
	else:
		return False

def get_article_url(mystring):
	s=re.findall('/article/Career_Upgrade/.{6}',mystring)
	SMTH_URL = 'http://m.newsmth.net'
	return SMTH_URL + s[0]
def get_title(mystring):
	s=re.findall('>.*', mystring)
	if s != []:
		return s[0]
	else:
		return 'No Title'

# item = 'http://m.newsmth.net/article/Career_Upgrade/414520'
# xml = urllib.urlopen(item).read()

# print ET.fromstring(xml)
def get_details(need_item, xml):
	patten_details = 'tid="' +need_item[-6:]+ '".*pagead2.googles'
	
	s = re.findall(patten_details, xml)
	
	if s != []:

		return s[0][35:-40]
	else:
		print 'no pattens found'
		raise ValueError
def get_email(str1):

	s_email = re.findall('([\w\.\-]+@[\w\.\-]+)',str1)
	
	if s_email != []:
		return s_email[0]
	else:
		print 'no email found'
		return 'no Email'



def get_good_details(mystr):
	return mystr.replace('&nbsp;', ' ').replace('<br>', ' ').replace('<br/>', ' ')
def get_current_time():
		return  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	