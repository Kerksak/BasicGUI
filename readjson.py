
import json


def readjson():
	with open('data.json',encoding='utf-8') as file:
		data = json.load(file)
		print(type(data))
		print(data[0])

	return data


def writejson(data):
	jsonobject = json.dumps(data,ensure_ascii=False,indent=4)
	with open('fruit.json','w',encoding='utf-8') as file:
		file.write(jsonobject)


data = {'124243244':['Banana',100,5],
		'124243245':['Durain',150,99],
		'124243246':['Apple',200,10],
		'124243247':['มะพร้าว',300,20]}

writejson(data)