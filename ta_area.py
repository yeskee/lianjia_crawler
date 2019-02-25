from urllib import request
import requests
import re
import time
import json
import math
import insert_tool


# 本程序的输入为：
# https://sh.lianjia.com/xiaoqu/5011000017872/
# 即小区信息的详细页面
# 
# 本程序的输出为：
# ['世茂滨江花园', '(浦东陆家嘴)潍坊西路1弄,潍坊西路2弄',
#  '93312', '2009', '31', '3410', '5011000017872', '121.520399,31.227414']
#  
# 对应为小区名、小区位置、小区挂牌均价、小区建筑时间、楼栋总数、总户数、小区编号、
# 东经，北纬坐标



def all(url):
	print('3  t_area-get:',url)
	getMessage(getHTMLText(url))
	

def getHTMLText(url):
	#访问网页获取页面txt信息的函数，返回值是网页全部信息
	try:
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
		r = requests.get(url,headers=headers,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"


def getMessage(text):

	detailMessage=list()
	get = list()
	get = ['class="detailTitle">(.*?)</h1>',
	'class="detailDesc">(.*?)</div></div>',
	'xiaoquUnitPrice">(.*?)</span>元',
	'筑年代</span><span class="xiaoquInfoContent">(.*?)年',
	'栋总数</span><span class="xiaoquInfoContent">(.*?)栋',
	'屋总数</span><span class="xiaoquInfoContent">(.*?)户',
	'    id:(.*?),',"resblockPosition:'(.*?)',"]


	for i in range(0,len(get)):
		#正则表达式匹配户型
		get_houseType=str(get[i])
		#进行匹配并将匹配结果加入列表中
		houseType=re.compile(get_houseType).findall(text)
		detailMessage.append("".join(houseType))


	print(detailMessage)
	#insert_tool.area_message(detailMessage)
	print('小区信息插入are表中')



if __name__=="__main__":
	url='https://sh.lianjia.com/xiaoqu/5011000017872/'
	getMessage(getHTMLText(url))

'''

def getMessage(text):	

	time.sleep(1)
	detailMessage=list()

	#小区名
	get_message = 'class="detailTitle">(.*?)</h1>'
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))


	#小区位置
	get_message = 'class="detailDesc">(.*?)</div></div>'
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#小区挂牌均价
	get_message = 'xiaoquUnitPrice">(.*?)</span>元'
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#小区建筑年代
	get_message = '筑年代</span><span class="xiaoquInfoContent">(.*?)年'
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#楼栋总数
	get_message = '栋总数</span><span class="xiaoquInfoContent">(.*?)栋'
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#总户数
	get_message = '屋总数</span><span class="xiaoquInfoContent">(.*?)户'
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#小区编号
	get_message = '    id:(.*?),'
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#经纬度
	get_message = "resblockPosition:'(.*?)',"
	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	print(detailMessage)
'''

