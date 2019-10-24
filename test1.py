import pymysql
import json
conn=pymysql.connect(host="localhost", user="root", password="12345678", database="znhy", port=3306)
cur = conn.cursor()
# sql = 'SELECT  Humidity,Temperature FROM test'
# cur.execute(sql)
# datas = cur.fetchall()
# jsonData={}
# id = []
# Temperature = []
# for data in datas:
#     id.append(data[0])
#     Temperature.append(data[1])
# # jsonData['id'] = id
# # jsonData['Temperature'] = Temperature
# # Temperature = json.dumps(jsonData)
# id=json.dumps(id)
# Temperature=json.dumps(Temperature)
# cur.close()
# conn.close()
# dict={
#     'id':id,
#     'Temperature':Temperature
# }
# print(dict)
# sql = 'SELECT  Humidity,Illumination FROM test'
# cur.execute(sql)
# datas = cur.fetchall()
# jsonData = {}
# id = []
# Illumination = []
# for data in datas:
#     id.append(data[0])
#     Illumination.append(data[1])
#
# dict = {
#     'id': json.dumps(id),
#     'Illumination': json.dumps(Illumination)
# }
# print(dict)