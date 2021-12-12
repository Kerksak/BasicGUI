# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import csv
#######################################################
def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) 
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	return stamp



def writetext(quantity,total):

	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) 
	# stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'Date&Time: {} Bitcoin: {} coin total value: {:,.2f} THB'.format(stamp,quantity,total))

def writecsv(data):
	# data = ['Time',10,500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')


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

#######################################################
GUI = Tk()
GUI.geometry('500x300')
GUI.title('Basic Program')


file = PhotoImage(file='images.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='Price Calculation program',font=('Angsana New',30,'bold'),fg='green')
L1.pack() #.place(x,y), .grid(row=0,column=0)

L2 = Label(GUI,text='Input number of goods',font=('Angsana New',20))
L2.pack() #.place(x,y), .grid(row=0,column=0)


v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้ในการเก็บข้อมูล
E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impack',30))
E1.pack()



def Calulate(event=None):
	quantity = v_quantity.get()
	price = 100
	print('Unit',float(quantity) * price)
	cal = float(quantity) * price
	# EN Date
	# stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# # TH Date
	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) 
	# stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')

	# # Function save data to txt
	# filename = 'data.txt'
	# with open(filename,'a',encoding='utf-8') as file:
	# 	file.write('\n'+ 'Date&Time: {} Bitcoin: {} coin total value: {:,.2f} THB'.format(stamp,quantity,cal))

	# writetext(quantity,cal)
	data = [timestamp(thai=False),quantity,cal]
	writecsv(data)


	#Pop up
	sm = sumdata()
	title = 'Total spending'
	text = 'Number of coin {} coins Total price: {:,.2f} THB'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('') #Clear data
	E1.focus()


B1 = ttk.Button(GUI, text='Calculation',command=Calulate)
B1.pack(ipadx=20,ipady=10,pady=20)

E1.bind('<Return>', Calulate)


def SummaryData(event):
	#Pop up
	sm = sumdata()
	title = 'Total amount'
	text = 'unit of sell: {} coin\n ยอดขาย: {:,.2f}'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

GUI.bind('<F1>',SummaryData)


E1.focus() # stand by cursor at E1
GUI.mainloop()


