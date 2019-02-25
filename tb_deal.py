from urllib import request
import requests
import re
import time
import json
import math
import four_deal

#在成交的小区目录中提取已经成交的房子链接，
#这样直接把链接传给最终的爬取程序即可。
#程序可以自己判断是不是把这个目录里所有的
#已售二手房具体信息链接都弄下来了
#
#本程序输入为:
#即小区成交目录,页码由本程序控制
#https://sh.lianjia.com/chengjiao/c5011000018309/
#
# 本程序输出为：
# https://sh.lianjia.com/chengjiao/107000055721.html
# https://sh.lianjia.com/chengjiao/107000075967.html
# https://sh.lianjia.com/chengjiao/107100093829.html
# https://sh.lianjia.com/chengjiao/107100066316.html
# 是成交二手房详细信息的链接

def all(url):
	print('3  t_deal-get:',url)
	dealPageControl(url)

def getHTMLText(url):
	try:
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
		r = requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"

#获取在售二手房信息

def dealPageControl(url):

	i = 1
	while True:
		print(' t_deal 当前页数为：',i)
		#now_page就是当前传给getmessage的页面
		now_page = url+'pg'+str(i)+'/'
		i = i + 1
		#传递url给getMessage
		print(' t_deal 当前小区成交目录页面为：',now_page)
		if getMessage(getHTMLText(now_page)) == 0:
			break



def getMessage(text):	

	#获取销售标题和房间号码的正则表达式
	get_deal_house_code='class="title"><a href="https://sh.lianjia.com/chengjiao/(.*?).html'

	deal_house_code=re.compile(get_deal_house_code).findall(text)

	#列表不为空，就是这个页面还有房子数据。
	if len(deal_house_code) != 0:
		print('交易二手房详细信息略去，本页面二手房数量为：',len(deal_house_code))
		print()
		#产生最终的完成交易的二手房详细信息页面
		for i in range(0,len(deal_house_code)):
			dealHouseDetail_Url = 'https://sh.lianjia.com/chengjiao/'+deal_house_code[i]+'.html'
			#输出当前生成的已售二手房详细信息页面的url，还有这个房子在这个页面的排序
			#排序就是该页的第几个，取值范围[0-29]
			#到时直接把这个链接传给爬取具体信息的程序就可以了
			#print(i,dealHouseDetail_Url)
			print('3  t_deal->four_deal:',dealHouseDetail_Url)
			#four_deal.all(dealHouseDetail_Url)
	else:
		return 0


if __name__=="__main__":
	url='https://sh.lianjia.com/chengjiao/c5011000017872/'
	dealPageControl(url)