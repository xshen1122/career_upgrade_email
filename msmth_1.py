# msmth_1.py
from get_url import *
import sys 
import urllib
from smth_email import send_email
SMTH_URL = 'http://m.newsmth.net/board/Career_Upgrade'
class CareerUrl():
	def __init__(self):
		self.html_list = [SMTH_URL]
		self.everyday_list = []
		self.need_list = []
		self.details=[]
		self.email = []
		self.title_list = []
    		
	def get_html_list(self):
		for i in range(2,10):
			self.html_list.append(SMTH_URL + '?p=' + str(i))

	def get_everyday_list(self):
		for item in self.html_list:
			s=get_url(urllib.urlopen(item).read())
			for item in s:
				self.everyday_list.append(item)
	def get_need_list(self):
		for item in self.everyday_list:
			if get_article_flag(item):
				self.need_list.append(get_article_url(item))
				self.title_list.append(get_title(item))
	def get_need_details(self):
		for item in self.need_list:
			every_details = get_details(item,urllib.urlopen(item).read())
			good_details = get_good_details(every_details)
			self.details.append(good_details)
	def get_need_email(self):
		for item in self.details:
			every_email = get_email(item)
			self.email.append(every_email)


if __name__ == '__main__':
	
	test1 = CareerUrl()
	test1.get_html_list()
	test1.get_everyday_list()
	test1.get_need_list()
	test1.get_need_details()
	test1.get_need_email()
	# test1.get_title()

	total_string = get_current_time() + '\n'
	total_string += '\n ************************************** \n'
	for i in range(0,len(test1.need_list)-1):
		total_string += '================================\n'
		total_string += test1.need_list[i] + '\n'
		total_string += '===' + test1.title_list[i] + '\n' 

		total_string += '================================\n'
		total_string += test1.email[i] + '\n'
		total_string += '=================\n'
		total_string += test1.details[i] + '\n'
	print total_string
	send_email(total_string)
	# filename = '2016-6-2.xml'
	# myfile = open(filename,'w')
	# myfile.write(total_string)
	# myfile.close()
