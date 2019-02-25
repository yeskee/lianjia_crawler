from urllib import request
import requests
import re
import time
import json
import pymysql

def getHTMLText(url):
	try:
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
		r = requests.get(url,headers=headers,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"

def getMessage(text):
	

	#定义匹配视频标签、上传时间、上传者编号、视频名称的正则表达式
	#Name='data-el="region">(.*?) </a>'
	#print(re.compile(Name).findall(text))
	No='xiaoqu/(.*?)/" target="_blank" data-log_index="'
	getNo=re.compile(No).findall(text)
	#print(getNo)
	for i in range(0,30):
		insert(int(getNo[i]))

	#匹配标签信息，然后加入结果列表中
	#result.append("".join(label[-1]))

	

if __name__=="__main__":

	url = 'https://sh.lianjia.com/chengjiao/107002099919.html'
	print(getHTMLText(url))