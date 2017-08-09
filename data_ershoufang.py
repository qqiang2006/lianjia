#coding=utf8
import sqlite3
def modify_database(area,num):
    # 数据库操作
    data_base_ershoufang = sqlite3.connect('/Users/lihuixian/ershoufang/ershoufang_beijing.db')
    data_base_ershoufang.text_factory = str
    cu = data_base_ershoufang.cursor()
    cu.execute("create table  if not exists house_num(area_name TEXT UNIQUE,num integer)")
    # 异常判断数据库中表是否已经存在
    try:
        print "begin"
        data_base_ershoufang.execute("insert into house_num(area_name,num) values(?,?);",
                                    (area, num))
        print "ok"
    except sqlite3.IntegrityError:
        print "error"
    data_base_ershoufang.commit()
modify_database("海",112)
data_base_stock = sqlite3.connect('/Users/lihuixian/ershoufang/ershoufang_beijing.db')
cu = data_base_stock.cursor()
# 模糊查询股市ID
cu.execute("select * from house_num ")
stock_num_list = cu.fetchall()
print stock_num_list[0]