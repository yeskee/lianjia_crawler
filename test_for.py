from urllib import request
import requests
import re
import time
import json
import math

#本程序的输入为
#在售二手房的详细信息页面
#https://sh.lianjia.com/ershoufang/107100159081.html
#
#本程序输出为(很显然回车是我加上的)：
#['2室2厅1厨1卫', '111.52', '1040', '93257', '南 北', 
#'高楼层 (共16层)', '唯一住宅', '满五年', '107100159081', 
#'5011000016299', '2018-03-31']
#
#信息依次为户型、面积(单位平方米)、售价(单位万)、每平方米价格(单位元)、
#朝向、是否唯一、是否满五年、链家房间编号、所属小区链家编号、挂牌时间。



def all(url):
	print('4  four_sell:',url)
	test_for(getHTMLText(url))


def getHTMLText(url):
	try:
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
		r = requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"


def test_for(text):

	detailMessage=list()
	get = list()
	get = ["房屋户型</span>(.*?)</li>",'建筑面积</span>(.*?)㎡</li>',
	"totalPrice:'(.*?)',","price:'(.*?)',","房屋朝向</span>(.*?)</li>",
	"所在楼层</span>(.*?)</li>","isUnique:'(.*?)',","registerTime:'(.*?)',",
	"houseId:'(.*?)',","resblockId:'(.*?)',"]


	for i in range(0,len(get)):
		#正则表达式匹配户型
		get_houseType=str(get[i])
		#进行匹配并将匹配结果加入列表中
		houseType=re.compile(get_houseType).findall(text)
		detailMessage.append("".join(houseType))


	#正则表达式匹配挂牌时间
	get_perM2_Price='<span>(.*?)</span>'
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	#模糊匹配，匹配结果的列表中第9个是挂牌时间。最好多测试一下这个模糊匹配
	detailMessage.append("".join(perM2_Price[8]))

	print(detailMessage)





def getMessage(text):	

	detailMessage=list()

	#正则表达式匹配户型
	get_houseType="房屋户型</span>(.*?)</li>"
	#进行匹配并将匹配结果加入列表中
	houseType=re.compile(get_houseType).findall(text)
	detailMessage.append("".join(houseType))

	#正则表达式匹配面积
	get_area='建筑面积</span>(.*?)㎡</li>'
	#进行匹配并将匹配结果加入列表中
	area=re.compile(get_area).findall(text)
	detailMessage.append("".join(area))

	#正则表达式匹配总价
	get_totalPrice="totalPrice:'(.*?)',"
	#进行匹配并将匹配结果加入列表中
	totalPrice=re.compile(get_totalPrice).findall(text)
	detailMessage.append("".join(totalPrice))

	#正则表达式匹配元/平方米
	get_perM2_Price="price:'(.*?)',"
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	detailMessage.append("".join(perM2_Price))

	#正则表达式匹配朝向
	get_perM2_Price="房屋朝向</span>(.*?)</li>"
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	detailMessage.append("".join(perM2_Price))

	#正则表达式匹配楼层
	get_perM2_Price="所在楼层</span>(.*?)</li>"
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	detailMessage.append("".join(perM2_Price))

	#正则表达式匹配挂牌时间
	get_perM2_Price='<span>(.*?)</span>'
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	#模糊匹配，匹配结果的列表中第9个是挂牌时间。最好多测试一下这个模糊匹配
	detailMessage.append("".join(perM2_Price[8]))


	#正则表达式匹配是否唯一
	get_perM2_Price="isUnique:'(.*?)',"
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	detailMessage.append("".join(perM2_Price))

	#正则表达式匹配是否五年
	get_perM2_Price="registerTime:'(.*?)',"
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	detailMessage.append("".join(perM2_Price))


	#正则表达式匹配房间编号
	get_perM2_Price="houseId:'(.*?)',"
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	detailMessage.append("".join(perM2_Price))

	#正则表达式匹配小区编号
	get_perM2_Price="resblockId:'(.*?)',"
	#进行匹配并将匹配结果加入列表中
	perM2_Price=re.compile(get_perM2_Price).findall(text)
	detailMessage.append("".join(perM2_Price))



	print(detailMessage)




if __name__=="__main__":
	url='https://sh.lianjia.com/ershoufang/107100159081.html'
	test_for(getHTMLText(url))