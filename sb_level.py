from urllib import request
import requests
import re
import time
import json
import math
import tb_deal

#页数控制可以由下一级程序自行控制!!!!!

#本程序的接收为
#https://sh.lianjia.com/xiaoqu/pudong/pg93/

#本程序的输出为
#小区信息的详细页面
#https://sh.lianjia.com/xiaoqu/5011000017872/
#在售二手房的详细信息
#https://sh.lianjia.com/ershoufang/c5011000013248/
#成交二手房的详细信息
#https://sh.lianjia.com/chengjiao/c5011000013248/

def all(url):
	print('2  s_level-get:',url)
	getMessage(getHTMLText(url))


def getHTMLText(url):
	try:
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
		r = requests.get(url,headers=headers,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"

#本分支中下面的函数不参与运行
def getSellingUrl(area_no):
	selling_url='https://sh.lianjia.com/ershoufang/c'+area_no+'/'
	#对接的程序是t-sell，把print的链接传递给输出的程序就好
	#print(selling_url)
	print('2  s_level->t_sell:',selling_url)
	t_sell.all(selling_url)

def getDealUrl(area_no):
	deal_url='https://sh.lianjia.com/chengjiao/c'+area_no+'/'
	#成交对应的程序是t-deal,把print输出的URL传给程序就好
	#print(deal_url)
	print('2  s_level->t_deal:',deal_url)
	tb_deal.all(deal_url)

#本分支中下面的函数不参与运行
def areaDetail(area_no):
	areaDetailUrl = 'https://sh.lianjia.com/xiaoqu/'+area_no+'/'
	#小区详细信息对应的程序是t-area,把print输出的url传给t_area就好
	#print(areaDetailUrl)
	print('2  s_level->t_area:',areaDetailUrl)
	t_area.all(areaDetailUrl)


def getMessage(text):	

	#定义匹配在售二手房数量和已近90天成交二手房数量的正则表达式
	#get_selling_no='class="totalSellCount"><span>(.*?)</span>套</a>'
	get_deal_no='/" >90天成交(.*?)套</a>'
	#匹配小区编号的正则表达式
	get_area_no='ershoufang/c(.*?)/" class="totalSellCount"'

	#上面定义的两个正则表达式匹配相应数据
	#selling_no=re.compile(get_selling_no).findall(text)
	deal_no=re.compile(get_deal_no).findall(text)
	area_no=re.compile(get_area_no).findall(text)

	#将列表中的str类型数据全部转化成int型数据，方便后面if的判断
	#注意，这里的area_no是不需要进行str到int的转换的
	#selling_no = list(map(int, selling_no))
	deal_no = list(map(int, deal_no))

	#根据小区在售房数量和近90天成效数量的分类器
	for i in range(0,len(area_no)):
		#下面这条语句可以调用函数生成小区详细信息页面的url
		print('')
		#areaDetail(area_no[i])
		if(deal_no[i]!=0):
			#正式执行下面要取消注释
			#getSellingUrl(area_no[i])
			getDealUrl(area_no[i])	
		#elif((selling_no[i]==0) and (deal_no[i]!=0)):
			#getDealUrl(area_no[i])
		#elif((selling_no[i]!=0) and (deal_no[i]==0)):
			#正式执行下面要取消注释
			#getSellingUrl(area_no[i])
	#for i in range(0,30):
		#insert(int(getNo[i]))'''



if __name__=="__main__":
	url='https://sh.lianjia.com/xiaoqu/pudong/pg3/'
	getMessage(getHTMLText(url))
