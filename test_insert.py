import pymysql

def area_message(message):
	#用来将信息存入数据库的函数
	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="network_spider", port=3306,charset='utf8')
	cursor = db.cursor()
	
	#message[0]=str(message[0])

	sql = "INSERT INTO area(area_nam) VALUES ('%s')" % \
	(message[0])

	try:
		cursor.execute(sql)
		db.commit()
		#print('videolabel提交成功')
	except Exception as e:  
		db.rollback()
		print(e)
		print('catch异常')
	finally:
		db.close()
		#print('连接关闭')
		#

if __name__=="__main__":

	message = ['康桥宝邸', '(浦东康桥)康弘路508弄', '42433', '2007', '125', '2367', '5011000011208', '121.606772,31.128658']
	print(message)
	print(type(message[0]))
	area_message(message)