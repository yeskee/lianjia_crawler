from urllib import request
import requests
import re
import time
import json
import math
import sb_level

#本程序的生成结果
#本程序调整好页数之后把带有页数的url传送给下级程序
#https://sh.lianjia.com/xiaoqu/pudong/pg93/
#https://sh.lianjia.com/xiaoqu/pudong/pg94/
#https://sh.lianjia.com/xiaoqu/minhang/pg1/
#https://sh.lianjia.com/xiaoqu/minhang/pg2/



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



if __name__=="__main__":
	districtName=list()
	districtName=['pudong','minhang','baoshan','xuhui','putuo','yangpu',
			'changning','songjiang','jiading','huangpu','jingan','zhabei',
			'hongkou','qingpu','fengxian','jinshan','chongming','shanghaizhoubian']
	CNName=['浦东','闵行','宝山','徐汇','普陀','杨浦',
			'长宁','松江','嘉定','黄埔','静安','闸北',
			'虹口','青浦','奉贤','金山','崇明','上海周边']

	#第一个循环用来控制行政区
	x = len(districtName)
	for i in range(0,x):
		print('各区对应编号为：',i,CNName[i])

	while True:

		no = input("请输入要爬取信息的行政区对应的编号: ")
		no = int(no)
		print('您输入的号码是:',no,'对应的行政区是:',CNName[no])

		print('您----确----定----吗？\n')
		check = input('确认无误输入1，否则输入0重新输入行政区： ')

		check = int(check)

		if check == 0:
			continue

		link = "https://sh.lianjia.com/xiaoqu/"+districtName[no]+"/"

		#把页面里显示的有多少个小区抓下来
		#然后小区总数除以30向上取整就是目录的页数
		#控制一下生成这么多页数的url就可以覆盖全部该行政区下的全部小区
		get_area_Count = '>共找到<span> (.*?) </span>个小区'
		area_Count=re.compile(get_area_Count).findall(getHTMLText(link))

		page_Count = int(area_Count[0])/30
		page_Count = math.ceil(page_Count)
		#第二个循环在控制行政区的基础上控制当前是该区目录第几页
		#最后形成的url传给下一级代码
		#现在已经可以控制生成改目录下面的全部页数了
		for j in range(1,page_Count+1):
			link_page = link+'pg'+str(j)+'/'
			#把这里生成的url传递给s_level就好
			#print(first_link_page)
			print('1  f_level->s_level:',link_page)
			sb_level.all(link_page)
		
		print('继续执行爬取任务吗?\n')
		status = input('继续执行输入1，否则输入0退出程序： ')

		status = int(status)

		if status == 0:
			break

'''

for i in range(0,2):
	#第一个链接，控制行政区
	first_link = "https://sh.lianjia.com/xiaoqu/"+districtName[i]+"/"

	#把页面里显示的有多少个小区抓下来
	#然后小区总数除以30向上取整就是目录的页数
	#控制一下生成这么多页数的url就可以覆盖全部该行政区下的全部小区
	get_area_Count = '>共找到<span> (.*?) </span>个小区'
	area_Count=re.compile(get_area_Count).findall(getHTMLText(first_link))

	page_Count = int(area_Count[0])/30
	page_Count = math.ceil(page_Count)
	print(page_Count)
	#第二个循环在控制行政区的基础上控制当前是该区目录第几页
	#最后形成的url传给下一级代码
	#现在已经可以控制生成改目录下面的全部页数了
	#for j in range(1,page_Count+1):
		#first_link_page = first_link+'pg'+str(j)+'/'
		#把这里生成的url传递给s_level就好
		#print(first_link_page)
'''