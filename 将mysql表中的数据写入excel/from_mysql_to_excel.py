#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#author:yjzhai

import pymysql
import xlwt
import os
from time import strftime

class Test(object):
    def __init__(self):
        self.host="127.0.0.1"
        self.port=3306
        self.db_name="test"
        self.username="root"
        self.password='123456'

    #连接数据库
    def get_data(self,sql):
        conn=pymysql.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            port=self.port,
            db=self.db_name,
            charset="utf8"
        )
        #设置游标
        cursor=conn.cursor()
        cursor.execute(sql)
        #获取执行结果的所有数据
        data=cursor.fetchall()
        #获取数据库中所有字段名
        self.fields=[field[0] for field in cursor.description]
        cursor.close()
        conn.close()
        return data

    def write_excel(self):
        sql="select * from student_info"
        file_name="学生信息"+strftime("%Y%m%d%H%M%S")+".xls"
        data=self.get_data(sql)
        #函数遇到return就立即停止，不再往下执行，不管是true还是false
        if not data:
            print("数据为空")
            return False
        #如果文件已经存在，则删除已有文件
        if os.path.exists(file_name):
            os.remove(file_name)
        #创建excel
        file=xlwt.Workbook()
        #新增sheet页
        sheet1=file.add_sheet("学生信息")
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        #Python 2.3. 以上版本可用，2.6 添加 start 参数。
        for col,field in enumerate(self.fields):
            sheet1.write(0,col,field)

        raw=1
        for datas in data:
            for col,value in enumerate(datas):
                sheet1.write(raw,col,value)
            raw+=1
        file.save(file_name)

        if not os.path.exists(file_name):
            print("文件写入失败")
            return False
        else:
            print("文件写入成功")
            return True
if __name__ == "__main__":
    test=Test()
    test.write_excel()