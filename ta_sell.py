from urllib import request
import requests
import re
import time
import json
import four_sell

#本程序输入为
#https://sh.lianjia.com/ershoufang/c5011000017872/
#即在售二手房目录
#本目录页码由本程序控制
#
#本程序输出为
#https://sh.lianjia.com/ershoufang/107100421502.html
#即在售二手房详细信息链接

def all(url):
	print('3  t_sell-get:',url)
	sellingPageControl(url)

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
#获取的是不含页数的小区在售二手房目录
#可以在这个目录下面抓所有房子的名称，抓不到或者都进去爬过了就可以结束了
def sellingPageControl(url):
	i = 1
	while True:
		now_page = url+'pg'+str(i)+'/'
		#传递url给getMessage
		i = i + 1
		print(' t_sell 当前小区目录页面为页面为：',now_page)
		if getMessage(getHTMLText(now_page)) == 0:
			return


def getMessage(text):

	#获取销售标题和房间号码的正则表达式
	get_selling_tirtle='alt="(.*?)"></a><div class="info clear">'
	get_house_code='LOGCLICK" data-hid="(.*?)"'

	selling_tirtle=re.compile(get_selling_tirtle).findall(text)
	house_code=re.compile(get_house_code).findall(text)
	#列表不为空，就是这个页面还有房子数据。
	if len(selling_tirtle) != 0:
		#这样可以方便地控制销售标题和对应的房间号码一起输出
		for i in range(0,len(selling_tirtle)):
			#print('  编号及二手房标题：',i+1,selling_tirtle[i])
			houseDetail_Url = 'https://sh.lianjia.com/ershoufang/'+house_code[i]+'.html'
			#print('二手房详情页面URL为：')
			#print(houseDetail_Url)
			#print('t-sell下传开始')
			print('3  t_sell->four_sell:',houseDetail_Url)
			#four_sell.all(houseDetail_Url)
			#print('t-sell下传结束')
	else:
		return 0


if __name__=="__main__":
	url='https://sh.lianjia.com/ershoufang/c5011000013988/'
	sellingPageControl(url)