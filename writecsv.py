# writecsv.py
import csv

def writecsv(data):
	# data = ['Time',10,500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

d = ['2021-05-11 13:00:50',50,5000]
writecsv(d)


def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	
	result = readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return (sumquan,sumtotal)

result = sumdata()
print(result)




# readcsv()

# result = readcsv()
# # print(result)

# sumlist_quan = []
# for d in result:
# 	sumlist_quan.append(float(d[1]))

# print(sumlist_quan, sum(sumlist_quan))

# sumlist_quan2 = sum([float(d[1]) for d in result])


