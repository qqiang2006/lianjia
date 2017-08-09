#coding=utf8
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import time
from pyExcelerator import *

all_area={'haidian':'海淀','changping':'昌平','daxing':'大兴','dongcheng':'东城','chaoyang':'朝阳','shunyi':'顺义','xicheng':'西城','fengtai':'丰台','fangshan':'房山','mentougou':'门头沟','pinggu':'平谷',
          'huairou':'怀柔','yanqing':'延庆','miyun':'密云','yanjiao':'燕郊'}

#操作数据库函数
def modify_database(area,num):
    # 数据库操作
    data_base_ershoufang = sqlite3.connect('/Users/lihuixian/ershoufang/ershoufang_beijing.db')
    data_base_ershoufang.text_factory = str
    cu = data_base_ershoufang.cursor()
    cu.execute("create table  if not exists house_num(area_name TEXT UNIQUE,num integer)")
    # 异常判断数据库中表是否已经存在
    try:
        data_base_ershoufang.execute("insert into house_num(area_name,num) values(?,?);",
                                    (area, num))
        print "ok"

    except sqlite3.IntegrityError:
        print "error"
        break


for i in all_area:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    if i == 'yanjiao':
        tmp=urllib2.Request('http://lf.lianjia.com/ershoufang/' + i + '/',headers=headers)
    else:
        tmp=urllib2.Request('http://bj.lianjia.com/ershoufang/' + i + '/',headers=headers)
    http=urllib2.urlopen(tmp)
    req=http.read()
    # print(req)
    print(all_area[i]),
    #写入名称
    bsobj=BeautifulSoup(req,'html5lib')
    # print bsobj.prettify()
    try:
        value=bsobj.findAll('meta',{'name':'description'})[0]
        result=re.findall(r'\d+', str(value))[0]
        print result + "套"
        #ws.write(ID,1,all_area[i])  # 在1行1列写入bit
        ID+=1
        #加请求延时
        #time.sleep(1)
    except:
        print "the IP is block!"
        continue


