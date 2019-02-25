import pymysql

#['3室2厅1厨2卫', '237.13', '2300', '96994', '西', 
#'高楼层 (共62层)', '不唯一', '未满两年',
# '107100106253', '5011000017872', '2018-03-16']
#
#信息依次为户型、面积(单位平方米)、售价(单位万)、每平方米价格(单位元)、
#朝向、是否唯一、是否满五年、链家房间编号、所属小区链家编号、挂牌时间。


def sell_message(message):
	#用来将信息存入数据库的函数
	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="network_spider", port=3306,charset='utf8')
	cursor = db.cursor()
	try:
		message[1]=float(message[1])
		message[2]=float(message[2])
		message[3]=float(message[3])
	except Exception as a:
		return

	sql = "INSERT INTO on_sale(house_type,house_area,house_single_price,house_total_price,house_direction,house_floor,house_listingTime,house_labe,house_no,house_area_id,house_labea) \
		VALUES ('%s','%f','%f','%f','%s','%s',str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),'%s','%s','%s','%s')" % \
		(message[0],message[1],message[2],message[3],message[4],message[5],message[10],message[6],message[8],message[9],message[10])

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


#  ['1室1厅1厨1卫', '54.65', '260', '47576', '南', '低楼层 (共5层)', 
#  '2018-03-21', '107100124225', '5011000017528', '38', '2018-04-28']


def deal_message(message):
	#用来将信息存入数据库的函数
	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="network_spider", port=3306,charset='utf8')
	cursor = db.cursor()
	
	try:
		message[1]=float(message[1])
		message[2]=float(message[2])
		message[3]=float(message[3])
		message[9]=float(message[9])
	except Exception as a:
		return

	sql = "INSERT INTO deal(house_type,house_area,house_single_price,house_direction,house_floor,house_listingTime,house_no,house_area_id,house_dealTime,house_cycle,house_dealPrice) \
		VALUES ('%s','%f','%f','%s','%s',str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),'%s','%s',str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),'%d','%f')" % \
		(message[0],message[1],message[3],message[4],message[5],message[6],message[7],message[8],message[10],message[9],message[2])

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


#本函数输入为：
#['康桥宝邸', '(浦东康桥)康弘路508弄', '42433', '2007', '125', '2367', '5011000011208', '121.606772,31.128658']

def area_message(message):
	#用来将信息存入数据库的函数
	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="network_spider", port=3306,charset='utf8')
	cursor = db.cursor()
	
	message[2]=float(message[2])
	message[3]=int(message[3])
	message[4]=int(message[4])
	message[5]=int(message[5])

	sql = "INSERT INTO are(area_name,area_address,area_avgPrice,area_years,area_buildingNum,area_houseNum,area_No,area_location) \
	 VALUES ('%s','%s','%f','%d','%d','%s','%s','%s')" % \
	(message[0],message[1],message[2],message[3],message[4],message[5],message[6],message[7])

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



if __name__=="__main__":
	#message = ['3室2厅1厨2卫', '237.13', '2300', '96994', '西', '高楼层 (共62层)', "不唯一", "未满两年", "107100106253", "5011000017872", "2018-03-16"]
	#print(message)
	#sell_message(message)
	#
	#message = ['1室1厅1厨1卫', '54.65', '260', '47576', '南', '低楼层 (共5层)', '2018-03-21', '107100124225', '5011000017528', '38', '2018-04-28']
	#print(message)
	#deal_message(message)
	#
	message = ['康桥宝邸', '(浦东康桥)康弘路508弄', '42433', '2007', '125', '2367', '5011000011208', '121.606772,31.128658']
	print(message)
	area_message(message)
	