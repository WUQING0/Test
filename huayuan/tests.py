from django.test import TestCase

# Create your tests here.
from huayuan import models
import pymysql
conn=pymysql.connect(host="localhost", user="root", password="12345678", database="znhy", port=3306)
cur = conn.cursor()
sql = 'SELECT  Humidity,Temperature FROM test'
cur.execute(sql)
u = cur.fetchall()
print(u)