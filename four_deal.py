from urllib import request
import requests
import re
import time
import json
import math
import insert_tool

# 本程序输入为：
# https://sh.lianjia.com/chengjiao/107000055721.html
# https://sh.lianjia.com/chengjiao/107000075967.html
# 就是已成交二手房详细信息页面
# 再写的话加正则表达式就可以了，想要什么信息就加什么表达式
# 最后的结果是一个列表。不同的信息在不同的位置，向数据库中
# insert的话调好编号就可以了。
# 
# 程序输出为：
# ['2室2厅1厨2卫', '139.18', '1251.8', '89942', '南', '高楼层 (共49层)', '2017-09-17',
#  '107000055721', '5011000017872', '2018-05-30', '256', '1300']
#  
#  对应分别是户型、面积、总价、元/平方米、朝向、楼层、挂牌日期、房屋编号、
#  小区编号、成交周期、挂牌价格、成交日期。


def all(url):
	print('4  four_deal:',url)
	getMessage(getHTMLText(url))

def getHTMLText(url):
	try:
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
		r = requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"

def getMessage(text):
	detailMessage=list()
	get = list()
	get = ['房屋户型</span>(.*?)\s*</li><li>','筑面积</span>(.*?)㎡\s*</li><li>',
	'class="dealTotalPrice"><i>(.*?)</i>万</span>','</i>万</span><b>(.*?)</b>元/平</div>',
	'房屋朝向</span>(.*?)\s*</li><li>','所在楼层</span>(.*?)\s*</li><li>',
	'挂牌时间</span>(.*?)\s*</li><li>',"houseCode:'(.*?)',",
	"resblockId:'(.*?)',",
	"</span><span><label>(.*?)</label>成交周期"]

	
	for i in range(0,len(get)):
		#正则表达式匹配
		get_message=str(get[i])
		#进行匹配并将匹配结果加入列表中
		message=re.compile(get_message).findall(text)
		detailMessage.append("".join(message))
		
		
	#单独匹配的最近一次的成交日期
	get_message='链家成交,(.*?)</p></li>'

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	detailMessage[10] = detailMessage[10][0:10]


	print(detailMessage)
	insert_tool.deal_message(detailMessage)
	print('成交二手房信息插入deal表中')
	#print(detailMessage[11][0:10])

if __name__=="__main__":
	url='https://sh.lianjia.com/chengjiao/107100124225.html'
	getMessage(getHTMLText(url))

'''
def getMessage(text):	

	time.sleep(1)
	detailMessage=list()

	#房屋户型
	get_house_type = '房屋户型</span>(.*?)\s*</li><li>'

	get_house_type=re.compile(get_house_type).findall(text)
	detailMessage.append("".join(get_house_type))

	#建筑面积
	get_builtup_area = '筑面积</span>(.*?)㎡\s*</li><li>'

	builtup_area=re.compile(get_builtup_area).findall(text)
	detailMessage.append("".join(builtup_area))

	#正则表达式匹配总价
	get_dealTotalPrice='class="dealTotalPrice"><i>(.*?)</i>万</span>'

	dealTotalPrice=re.compile(get_dealTotalPrice).findall(text)
	detailMessage.append("".join(dealTotalPrice))

	#正则表达式匹配每平米价格
	get_price_SQ_metre='</i>万</span><b>(.*?)</b>元/平</div>'

	price_SQ_metre=re.compile(get_price_SQ_metre).findall(text)
	detailMessage.append("".join(price_SQ_metre))

	#房屋朝向
	get_message='房屋朝向</span>(.*?)\s*</li><li>'

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#所在楼层
	get_message='所在楼层</span>(.*?)\s*</li><li>'

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#挂牌日期
	get_message='挂牌时间</span>(.*?)\s*</li><li>'

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))




	#房间编号
	get_message="houseCode:'(.*?)',"

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#小区编号
	get_message="resblockId:'(.*?)',"

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#成交日期
	get_message="链家成交,(.*?)</p>"

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#成交周期
	get_message="</span><span><label>(.*?)</label>成交周期"

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))

	#挂牌价格
	get_message="<label>(.*?)</label>挂牌价格"

	message=re.compile(get_message).findall(text)
	detailMessage.append("".join(message))





	print(detailMessage)

'''
