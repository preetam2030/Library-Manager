import tkinter as tk
import pandas as pd
import numpy as np
from datetime import timedelta, date
import datetime
global Auid
global Apas
global brecord
global srecord
global indno
global blist
global dlist
blist=['BookId1','BookId2','BookId3','BookId4','BookId5']
dlist=['DueDate1','DueDate2','DueDate3','DueDate4','DueDate5']
Auid='nsec'
Apas='12345'
brecord=pd.read_excel('bookrecord.xlsx')
srecord=pd.read_excel('studentrecord.xlsx')
srecord[['DueDate1','DueDate2','DueDate3','DueDate4','DueDate5']] = srecord[['DueDate1','DueDate2','DueDate3','DueDate4','DueDate5']].astype(str)
brecord['DueDate'] = brecord['DueDate'].astype(str)

class Library(tk.Tk):
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		container=tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		self.Frames={}
		for F in (StartPage,Adminlogin,Admin,Studentlogin,Register,Regbook,Student,Issue,Renew,Fine,Return):#ALL PAGES
			frame=F(container,self)
			self.Frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		self.show_frame(StartPage)
	def show_frame(self,cont):
		frame=self.Frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):#1ST PAGE
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text='Library')
		label.pack(padx=10,pady=10)
		b1=tk.Button(self,text='Admin',command=lambda:controller.show_frame(Adminlogin))
		b1.pack()
		b2=tk.Button(self,text='Student',command=lambda:controller.show_frame(Studentlogin))
		b2.pack()


class Adminlogin(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label4=tk.Label(self,text='Admin')
		label4.grid(row=0,column=1)
		label5=tk.Label(self,text='User Id')
		label5.grid(row=1,column=0)
		e3=tk.Entry(self,width=40)
		e3.grid(row=1,column=1)
		label6=tk.Label(self,text='Password')#lambda x : True if (x > 10 and x < 20) else False
		label6.grid(row=2,column=0)
		e4=tk.Entry(self,show='*',width=40)
		e4.grid(row=2,column=1)
		b3=tk.Button(self,text='Login',command=lambda:admincheck(self,e3,e4,controller))
		b3.grid(row=3,column=1)
		b4=tk.Button(self,text='Back',command=lambda:adminback(e3,e4,controller))
		b4.grid(row=4,column=1)
def adminback(e3,e4,controller):
	e3.delete(0, 'end')
	e4.delete(0, 'end')
	controller.show_frame(StartPage)

def admincheck(self,e3,e4,controller):
	auid=e3.get()
	apas=e4.get()
	e3.delete(0, 'end')
	e4.delete(0, 'end')
	if (auid==Auid) and (apas==Apas):
		controller.show_frame(Admin)
	else:
		l=tk.Label(self,text='Incorrect Id or Password.')
		l.grid(row=5,column=1)


class Studentlogin(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1=tk.Label(self,text='Student')
		label1.grid(row=0,column=1)
		label2=tk.Label(self,text='User Id')
		label2.grid(row=1,column=0)
		e1=tk.Entry(self,width=40)
		e1.grid(row=1,column=2)
		label3=tk.Label(self,text='Password')
		label3.grid(row=2,column=0)
		e2=tk.Entry(self,show='*',width=40)
		e2.grid(row=2,column=2)
		b5=tk.Button(self,text='Login',command=lambda:studentcheck(self,e1,e2,controller))
		b5.grid(row=3,column=1)
		b6=tk.Button(self,text='Register',command=lambda:controller.show_frame(Register))
		b6.grid(row=3,column=2)
		b7=tk.Button(self,text='Back',command=lambda:studentback(e1,e2,controller))
		b7.grid(row=4,column=1)

def studentback(e1,e2,controller):
	e1.delete(0, 'end')
	e2.delete(0, 'end')
	controller.show_frame(StartPage)

def studentcheck(self,e1,e2,controller):
	studuid=int(e1.get())
	studpas=e2.get()
	global studind
	e1.delete(0, 'end')
	e2.delete(0, 'end')
	flag=0
	print(srecord)
	print(studuid)
	print(studpas)
	for indno in range(len(srecord.index)):
		if int(srecord.loc[indno,'StudentId'])==studuid and str(srecord.loc[indno,'Password'])==studpas:
			flag=1
			studind=indno
			print(studind)
			controller.show_frame(Student)
	if flag==0:
		l1=tk.Label(self,text='Incorrect Id or Password.')
		l1.grid(row=5,column=1)


class Register(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label7=tk.Label(self,text='Register Yourself')
		label7.grid(row=0,column=1)
		label8=tk.Label(self,text='Enter Name')
		label8.grid(row=1,column=0)
		e5=tk.Entry(self,width=40)
		e5.grid(row=1,column=2)
		label9=tk.Label(self,text='Enter User Id')
		label9.grid(row=2,column=0)
		e6=tk.Entry(self,width=40)
		e6.grid(row=2,column=2)
		label10=tk.Label(self,text='Enter Password')
		label10.grid(row=3,column=0)
		e7=tk.Entry(self,show='*',width=40)
		e7.grid(row=3,column=2)
		label11=tk.Label(self,text='Confirm Password')
		label11.grid(row=4,column=0)
		e8=tk.Entry(self,show='*',width=40)
		e8.grid(row=4,column=2)
		b8=tk.Button(self,text='Register',command=lambda:registercheck(self,e5,e6,e7,e8,controller))
		b8.grid(row=5,column=1)
		b8=tk.Button(self,text='Back',command=lambda:registerback(self,e5,e6,e7,e8,controller))
		b8.grid(row=5,column=2)

def registercheck(self,e5,e6,e7,e8,controller):
	sname=e5.get()
	suid=int(e6.get())
	e5.delete(0, 'end')
	e6.delete(0, 'end')
	if e7.get()==e8.get():
		spas=e7.get()
		e7.delete(0, 'end')
		e8.delete(0, 'end')
		n=len(srecord.index)
		srecord.loc[n,'StudentId']=suid
		srecord.loc[n,'Name']=sname
		srecord.loc[n,'Password']=spas
		srecord.to_excel('studentrecord.xlsx',index=False)
		controller.show_frame(Studentlogin)
	else:
		label7=tk.Label(self,text='Enter the same password')
		label7.grid(row=6,column=1)

def registerback(self,e5,e6,e7,e8,controller):
	e5.delete(0, 'end')
	e6.delete(0, 'end')
	e7.delete(0, 'end')
	e8.delete(0, 'end')
	controller.show_frame(Studentlogin)

class Admin(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label6=tk.Label(self,text='Welcome Admin')
		label6.grid(row=0,column=2)
		b9=tk.Button(self,text='Issue',command=lambda:controller.show_frame(Issue))
		b9.grid(row=1,column=1)
		b10=tk.Button(self,text='Renew',command=lambda:controller.show_frame(Renew))
		b10.grid(row=1,column=2)
		b11=tk.Button(self,text='Fine',command=lambda:controller.show_frame(Fine))
		b11.grid(row=2,column=1)
		b12=tk.Button(self,text='Logout',command=lambda:controller.show_frame(Adminlogin))
		b12.grid(row=2,column=3)
		b19=tk.Button(self,text='Register book',command=lambda:controller.show_frame(Regbook))
		b19.grid(row=1,column=3)
		b19=tk.Button(self,text='Register book',command=lambda:controller.show_frame(Regbook))
		b19.grid(row=1,column=3)
		b21=tk.Button(self,text='Return',command=lambda:controller.show_frame(Return))
		b21.grid(row=2,column=2)
class Issue(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label12=tk.Label(self,text='Book id')
		label12.grid(row=0,column=0)
		e9=tk.Entry(self,width=40)
		e9.grid(row=0,column=2)
		label13=tk.Label(self,text='Student id')
		label13.grid(row=1,column=0)
		e10=tk.Entry(self,width=40)
		e10.grid(row=1,column=2)
		b13=tk.Button(self,text='Issue',command=lambda:issuecheck(self,e9,e10,controller)) #BACK BUTTON TO BE ADDED
		b13.grid(row=2,column=1)

def issuecheck(self,e9,e10,controller):
	ibook=int(e9.get())
	istud=int(e10.get())
	e9.delete(0, 'end')
	e10.delete(0, 'end')
	flag=0
	studind=0
	s=''
	for indno in range(len(srecord.index)):
		stbooks=list(map(float,srecord.loc[indno,blist]))
		if int(srecord.loc[indno,'StudentId'])==istud and ibook not in stbooks:
			flag=1
			print(flag)
			for s in blist:
				if pd.isna(srecord.loc[indno,s]) and flag==1:
					flag+=1
					studind=indno
					break
			if flag!=0:
				break
	for	indno in range(len(brecord.index)):
		if int(brecord.loc[indno,'BookId'])==ibook and int(brecord.loc[indno,'Status'])==1:
			brecord.loc[indno,'StudentId']=istud
			brecord.loc[indno,'DueDate']=(date.today() + timedelta(days=30)).strftime("%d-%m-%Y")
			brecord.loc[indno,'Status']=int(0)
			srecord.loc[studind,s]=ibook
			srecord.loc[studind,dlist[blist.index(s)]]=(date.today() + timedelta(days=30)).strftime("%d-%m-%Y")
			flag+=1
			break

	if flag!=3:
		l1=tk.Label(self,text='Incorrect Id or ')
		l1.grid(row=5,column=1)
	else:
		flag=0
		print(srecord)
		print(brecord)
		srecord.to_excel('studentrecord.xlsx',index=False)
		brecord.to_excel('bookrecord.xlsx',index=False)
		controller.show_frame(Admin)


class Renew(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label14=tk.Label(self,text='Student id')
		label14.grid(row=1,column=0)
		e11=tk.Entry(self,width=40)
		e11.grid(row=1,column=2)
		b14=tk.Button(self,text='Renew',command=lambda:renewcheck(self,e11,controller))
		b14.grid(row=2,column=1)
		b15=tk.Button(self,text='Back',command=lambda:controller.show_frame(Admin))
		b15.grid(row=2,column=2)
def renewcheck(self,e11,controller):
	rstud=int(e11.get())
	e11.delete(0, 'end')
	flag=0
	for indno in range(len(srecord.index)):
		if int(srecord.loc[indno,'StudentId'])==rstud:
			for s in dlist:
				if srecord.loc[indno,s]=='nan':
					continue
				elif datetime.datetime.strptime(srecord.loc[indno,s], "%d-%m-%Y").date()>=date.today():
					srecord.loc[indno,s]=(date.today() + timedelta(days=30)).strftime("%d-%m-%Y")
					bid=srecord.loc[indno,blist[dlist.index(s)]]
					for ind in range(len(brecord.index)):
						if brecord.loc[ind,'BookId']==bid:
							brecord.loc[ind,'DueDate']=(date.today() + timedelta(days=30)).strftime("%d-%m-%Y")
				else:
					flag=1
					break
			if flag==1:
				break
	if flag==1:
		label15=tk.Label(self,text='Fines Due')
		label15.grid(row=3,column=0)
	else:
		flag=0
		print(srecord)
		print(brecord)
		srecord.to_excel('studentrecord.xlsx',index=False)
		brecord.to_excel('bookrecord.xlsx',index=False)
		controller.show_frame(Admin)
class Fine(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label16=tk.Label(self,text='Student id')
		label16.grid(row=1,column=0)
		e12=tk.Entry(self,width=40)
		e12.grid(row=1,column=2)
		b16=tk.Button(self,text='Pay fine',command=lambda:finecheck(self,e12,controller))
		b16.grid(row=2,column=1)
		b17=tk.Button(self,text='Back',command=lambda:controller.show_frame(Admin))
		b17.grid(row=2,column=2)

def finecheck(self,e12,controller):
	fstud=int(e12.get())
	e12.delete(0, 'end')
	totalfine=0
	for indno in range(len(srecord.index)):
		if int(srecord.loc[indno,'StudentId'])==fstud:
			for s in dlist:
				if srecord.loc[indno,s]=='nan':
					continue
				elif datetime.datetime.strptime(srecord.loc[indno,s], "%d-%m-%Y").date()<date.today():
					totalfine+=(date.today()-datetime.datetime.strptime(srecord.loc[indno,s], "%d-%m-%Y").date()).days
			break
	label17=tk.Label(self,text='Fine Due')
	label17.grid(row=3,column=0)
	label18=tk.Label(self,text=totalfine)
	label18.grid(row=3,column=1)
	print(totalfine)
	for s in dlist:
			if srecord.loc[indno,s]=='nan':
				continue
			else:
				srecord.loc[indno,s]=(date.today() + timedelta(days=30)).strftime("%d-%m-%Y")
				bid=srecord.loc[indno,blist[dlist.index(s)]]
				for ind in range(len(brecord.index)):
					if brecord.loc[ind,'BookId']==bid:
						brecord.loc[ind,'DueDate']=(date.today() + timedelta(days=30)).strftime("%d-%m-%Y")
	print(srecord)
	print(brecord)
	srecord.to_excel('studentrecord.xlsx',index=False)
	brecord.to_excel('bookrecord.xlsx',index=False)


class Student(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label8=tk.Label(self,text='Welcome ')
		label8.grid(row=0,column=1)
		b12=tk.Button(self,text='Show details',command=lambda:detailcheck(self,controller))
		b12.grid(row=6,column=1)
		b18=tk.Button(self,text='Logout',command=lambda:controller.show_frame(Studentlogin))
		b18.grid(row=6,column=0)
def detailcheck(self,controller):
	label19=tk.Label(self,text=srecord.loc[studind,'Name'])
	label19.grid(row=0,column=2)
	if pd.isna(srecord.loc[studind,'BookId1']):
		print(1)
	else:
		bid=int(srecord.loc[studind,'BookId1'])
		bidx = brecord.loc[brecord['BookId']==bid].index[0]
		label20=tk.Label(self,text=brecord.loc[bidx,'Name'])
		label20.grid(row=1,column=0)
		label21=tk.Label(self,text=srecord.loc[studind,'DueDate1'])
		label21.grid(row=1,column=1)
	if pd.isna(srecord.loc[studind,'BookId2']):
		print(2)
	else:
		bid=int(srecord.loc[studind,'BookId2'])
		bidx = brecord.loc[brecord['BookId']==bid].index[0]
		label22=tk.Label(self,text=brecord.loc[bidx,'Name'])
		label22.grid(row=2,column=0)
		label23=tk.Label(self,text=srecord.loc[studind,'DueDate2'])
		label23.grid(row=2,column=1)
	if pd.isna(srecord.loc[studind,'BookId3']):
		print(3)
	else:
		bid=int(srecord.loc[studind,'BookId3'])
		bidx = brecord.loc[brecord['BookId']==bid].index[0]
		label24=tk.Label(self,text=brecord.loc[bidx,'Name'])
		label24.grid(row=3,column=0)
		label25=tk.Label(self,text=srecord.loc[studind,'DueDate3'])
		label25.grid(row=3,column=1)
	if pd.isna(srecord.loc[studind,'BookId4']):
		print(4)
	else:
		bid=int(srecord.loc[studind,'BookId4'])
		bidx = brecord.loc[brecord['BookId']==bid].index[0]
		label26=tk.Label(self,text=brecord.loc[bidx,'Name'])
		label26.grid(row=4,column=0)
		label27=tk.Label(self,text=srecord.loc[studind,'DueDate4'])
		label27.grid(row=4,column=1)
	if pd.isna(srecord.loc[studind,'BookId5']):
		print(5)
	else:
		bid=int(srecord.loc[studind,'BookId5'])
		bidx = brecord.loc[brecord['BookId']==bid].index[0]
		label28=tk.Label(self,text=brecord.loc[bidx,'Name'])
		label28.grid(row=5,column=0)
		label29=tk.Label(self,text=srecord.loc[studind,'DueDate5'])
		label29.grid(row=5,column=1)

class Regbook(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label30=tk.Label(self,text='Register Book')
		label30.grid(row=0,column=1)
		label31=tk.Label(self,text='Enter  Book Id')
		label31.grid(row=1,column=0)
		e13=tk.Entry(self,width=40)
		e13.grid(row=1,column=2)
		label32=tk.Label(self,text='Enter Book Name')
		label32.grid(row=2,column=0)
		e14=tk.Entry(self,width=40)
		e14.grid(row=2,column=2)
		label33=tk.Label(self,text='Enter Author Name')
		label33.grid(row=3,column=0)
		e15=tk.Entry(self,width=40)
		e15.grid(row=3,column=2)
		b19=tk.Button(self,text='Register',command=lambda:regbookcheck(self,e13,e14,e15,controller))
		b19.grid(row=4,column=1)
		b20=tk.Button(self,text='Back',command=lambda:regbookback(self,e13,e14,e15,controller))
		b20.grid(row=4,column=2)

def regbookcheck(self,e13,e14,e15,controller):
	buid=int(e13.get())
	bname=e14.get()
	baut=e15.get()
	e13.delete(0, 'end')
	e14.delete(0, 'end')
	e15.delete(0, 'end')
	if buid not in list(map(int,brecord['BookId'])):
		n=len(brecord.index)
		brecord.loc[n,'BookId']=buid
		brecord.loc[n,'Name']=bname
		brecord.loc[n,'Author']=baut
		brecord.loc[n,'Status']=1
		brecord.to_excel('bookrecord.xlsx',index=False)
		controller.show_frame(Admin)
	else:
		label34=tk.Label(self,text='There is already a book with this ID')
		label34.grid(row=5,column=1)

def regbookback(self,e13,e14,e15,controller):
	e13.delete(0, 'end')
	e14.delete(0, 'end')
	e15.delete(0, 'end')
	controller.show_frame(Admin)

class Return(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label35=tk.Label(self,text='Book id')
		label35.grid(row=1,column=0)
		e16=tk.Entry(self,width=40)
		e16.grid(row=1,column=2)
		b17=tk.Button(self,text='Return',command=lambda:returncheck(self,e16,controller))
		b17.grid(row=2,column=1)
		b18=tk.Button(self,text='Back',command=lambda:controller.show_frame(Admin))
		b18.grid(row=2,column=2)
def returncheck(self,e16,controller):
	rtbook=int(e16.get())
	e16.delete(0, 'end')
	print(rtbook)
	flag1=1
	for indno in range(len(brecord.index)):
		if int(brecord.loc[indno,'BookId'])==rtbook:
			if datetime.datetime.strptime(brecord.loc[indno,'DueDate'], "%d-%m-%Y").date()>=date.today():
				stid=brecord.loc[indno,'StudentId']
				for ind in range(len(srecord.index)):
					if srecord.loc[ind,'StudentId']==stid:
						for s in blist:
							if int(srecord.loc[ind,s])==rtbook:
								srecord.at[ind,s]=np.NaN
								srecord.at[ind,dlist[blist.index(s)]]='nan'
								brecord.at[indno,'StudentId']=np.NaN
								brecord.loc[indno,'Status']=1
								brecord.loc[indno,'DueDate']='nan'
								flag1=3
								break
					if flag1==3:
						break
			else:
				flag1=1
				break
			if flag1==3:
				break

	if flag1==1:
		label15=tk.Label(self,text='Fines Due')
		label15.grid(row=3,column=0)
	elif flag1==3:
		flag1=0
		print(srecord)
		print(brecord)
		srecord.to_excel('studentrecord.xlsx',index=False)
		brecord.to_excel('bookrecord.xlsx',index=False)
		controller.show_frame(Admin)
	else:
		label15=tk.Label(self,text='Incorrect Id or book not issued')
		label15.grid(row=3,column=0)

app=Library()
app.mainloop()
