#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#author:yjzhai

import os
import xlrd
import pymysql

class test(object):
    def __init__(self):
        self.host="localhost",
        self.port=3306,
        self.user="root",
        self.password="123456",
        self.db="test"
        # 获取excel路径
        excel_dir = os.path.dirname(os.path.abspath(__file__))
        self.excel_record=os.path.join(excel_dir,"学生信息.xls")
        self.sheet_name="学生信息"

    def read_excel(self):
        try:
            if os.path.exists(self.excel_record):
                print("原始文件存在，开始读取数据....")
            else:
                print("原始文件不存在...")
                return False
        except Exception as e:
            print(e)
        #读取excel
        book=xlrd.open_workbook(self.excel_record)
        #定位到sheet页
        sheet=book.sheet_by_name(self.sheet_name)
        #读取excel每行具体数据，从第二行开始是要跳过标题
        for r in range(1,sheet.nrows):
            col1=sheet.cell(r,0).value
            col2=sheet.cell(r,1).value
            col3=sheet.cell(r,2).value
            values=(col1,col2,col3)
            conn=self.connect_mysql()
            cursor = conn.cursor()
            query_sql = """"insert into student_info (stu_id,stu_name,stu_score) values(%s,%s,%s)"""
            cursor.execute(query_sql,values)
        cursor.close()
        conn.commit()
        conn.close()


    def connect_mysql(self):
        conn=pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset="utf8"
        )
        return conn

if __name__=="__main__":
    test=test()
    test.read_excel()
