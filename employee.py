from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
import tempfile
import os
class employeeSystem:
	def __init__(self,root):
		self.root=root
		self.root.title("Employee Payroll Management System")
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")
		self.root.resizable(0,0)
		title=Label(self.root,text="Employee Payroll Management System",
			  font=("arial",30,"bold"),bg="yellow",fg="black",bd=10,relief=GROOVE,padx=10).place(x=0,y=0,relwidth=1)
		btn_emp=Button(self.root,text="All Employee's",command=self.employee_frame,font=("arial 15 bold"),bg="red",fg="white",bd=4).place(x=1150,y=13,width=150,height=40)

		scrolly=Scrollbar(self.root,orient=VERTICAL)
		scrollx=Scrollbar(self.root,orient=HORIZONTAL)
		scrolly.pack(side=RIGHT,fill=Y)
		scrollx.pack(side=BOTTOM,fill=X)

		
		#*********Frame1*******************************************************************************************************************************
		#************Variables******
		self.var_emp_code=StringVar()
		self.var_designation=StringVar()
		self.var_name=StringVar()
		self.var_age=StringVar()
		self.var_gender=StringVar()
		self.var_email=StringVar()
		self.var_doj=StringVar()
		self.var_dob=StringVar()
		self.var_expr=StringVar()
		self.var_pid=StringVar() #adhar card
		self.var_cno=StringVar()



		F1=LabelFrame(self.root,text="Employee Details",font=("arial",17,"bold"),bd=10,relief=GROOVE,bg="blue",fg="yellow")
		F1.place(x=0,y=70,width=650,height=630)

		#title2=Label(F1,text="Employee Details",
			#  font=("arial",20,"bold"),bg="yellow",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
		#Row 1 Frame 1
		lbl_code=Label(F1,text="Employee Code",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=0,y=20)
		self.txt_code=Entry(F1,font=("arial",17),textvariable=self.var_emp_code,bg="lightyellow",bd=8,relief=GROOVE,fg="black")
		self.txt_code.place(x=200,y=20,width=260,height=40)

		btn_search=Button(F1,text="Search",command=self.search,font=("arial 20 bold"),bg="grey").place(x=470,y=20,width=150,height=40)

		#Row 2 Frame 1
		lbl_des=Label(F1,text="Designation",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=0,y=90)
		txt_des=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_designation,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=90,width=170,height=40)
		lbl_doj=Label(F1,text="D.O.J",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=360,y=90)
		txt_doj=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_doj,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=470,y=90,width=150,height=40)

		#Row 3 Frame 1
		lbl_name=Label(F1,text="Name",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=40,y=160)
		txt_name=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_name,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=160,width=170,height=40)
		lbl_dob=Label(F1,text="D.O.B",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=360,y=160)
		txt_dob=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_dob,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=470,y=160,width=150,height=40)

		#Row 4 Frame 1
		lbl_age=Label(F1,text="Age",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=45,y=225)
		txt_age=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_age,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=225,width=170,height=40)
		lbl_expr=Label(F1,text="Experience",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=338,y=225)
		txt_expr=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_expr,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=470,y=225,width=150,height=40)

		#Row 5 Frame 1
		lbl_gender=Label(F1,text="Gender",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=30,y=290)
		txt_gender=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_gender,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=290,width=170,height=40)
		lbl_pid=Label(F1,text="Proof ID",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=350,y=290)
		txt_pid=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_pid,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=470,y=290,width=150,height=40)

		#Row 6 Frame 1
		lbl_email=Label(F1,text="Email",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=35,y=365)
		txt_email=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_email,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=365,width=170,height=40)
		lbl_contact=Label(F1,text="Contact No",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=338,y=365)
		txt_contact=Entry(F1,font=("arial",17,"bold"),textvariable=self.var_cno,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=470,y=365,width=150,height=40)

		#Row 7 Frame 1
		lbl_address=Label(F1,text="Address",
			  font=("arial",17,"bold"),bg="blue",fg="white").place(x=18,y=440)
		self.txt_address=Text(F1,font=("arial",17),bg="lightyellow",bd=8,relief=GROOVE,fg="black")
		self.txt_address.place(x=150,y=440,width=470,height=150)


		#*********Frame2**********8
		#********Variable*********
		self.var_month=StringVar()
		self.var_year=StringVar()
		self.var_bsal=StringVar()
		self.var_tdays=StringVar()
		self.var_absents=StringVar()
		self.var_medical=StringVar()
		self.var_pfund=StringVar()
		self.var_convence=StringVar()
		self.var_nsal=StringVar()

		F2=LabelFrame(self.root,text="Employee Salary Details",font="arial 17 bold",bg="blue",bd=10,relief=GROOVE,fg="yellow")
		F2.place(x=650,y=70,width=700,height=300)

		#Row 1 Frame 2
		lbl_month=Label(F2,text="Month :",
					font=("arial 17 bold"),bg="blue",fg="white").place(x=0,y=0)
		txt_month=Entry(F2,font=("arial 17 bold"),textvariable=self.var_month,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=100,y=0,width=150,height=35)

		lbl_year=Label(F2,text="Year:",font=("arial 17 bold"),bg="blue",fg="white").place(x=257,y=0)
		txt_year=Entry(F2,font=("arial 17 bold"),textvariable=self.var_year,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=325,y=0,width=85,height=35)

		lbl_bsalary=Label(F2,text="Basic Salary:",font=("arial 17 bold"),bg="blue",fg="white").place(x=420,y=0)
		txt_bsalary=Entry(F2,font=("arial 17 bold"),textvariable=self.var_bsal,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=570,y=0,width=110,height=35)

		#Row 2 Frame 2
		lbl_tdays=Label(F2,text="Total Days :",font=("arial 17 bold"),bg="blue",fg="white").place(x=10,y=50)
		txt_tdays=Entry(F2,font=("arial 17 bold"),textvariable=self.var_tdays,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=50,width=180,height=40)

		lbl_absents=Label(F2,text="Absents :",font=("arial 17 bold"),bg="blue",fg="white").place(x=375,y=50)
		txt_absents=Entry(F2,font=("arial 17 bold"),textvariable=self.var_absents,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=530,y=50,width=150,height=40)

		#Row 3 Frame 2
		lbl_med=Label(F2,text="Medical :",font=("arial 17 bold"),bg="blue",fg="white").place(x=21,y=100)
		txt_med=Entry(F2,font=("arial 17 bold"),textvariable=self.var_medical,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=100,width=180,height=40)

		lbl_pfund=Label(F2,text="Provident Fund:",font=("arial 17 bold"),bg="blue",fg="white").place(x=340,y=100)
		txt_pfund=Entry(F2,font=("arial 17 bold"),textvariable=self.var_pfund,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=530,y=100,width=150,height=40)

		#Row 4 Frame 2
		lbl_convence=Label(F2,text="Convence :",font=("arial 17 bold"),bg="blue",fg="white").place(x=10,y=150)
		txt_convence=Entry(F2,font=("arial 17 bold"),textvariable=self.var_convence,bg="lightyellow",bd=8,relief=GROOVE,fg="black").place(x=150,y=150,width=180,height=40)

		lbl_netsalary=Label(F2,text="Net Salary:",font=("arial 17 bold"),bg="blue",fg="white").place(x=368,y=150)
		txt_netsalary=Entry(F2,font=("arial 17 bold"),textvariable=self.var_nsal,bg="grey",bd=8,relief=GROOVE,fg="black").place(x=530,y=150,width=150,height=40)



		#BUTTON in Frame 2 Row 4
		btn_calculate=Button(F2,text="Calculate",command=self.calculate,font=("arial 20 bold"),bd=2,relief=GROOVE,bg="orange",fg="black").place(x=70,y=195,width=170,height=30)
		self.btn_save=Button(F2,text="Save",command=self.add,font=("arial 20 bold"),bd=2,relief=GROOVE,bg="white",fg="black")
		self.btn_save.place(x=270,y=195,width=170,height=30)
		btn_clear=Button(F2,text="Clear",command=self.clear,font=("arial 20 bold"),bd=2,relief=GROOVE,bg="green",fg="black").place(x=470,y=195,width=170,height=30)
		
		self.btn_update=Button(F2,text="Update",state=DISABLED,command=self.update,font=("arial 20 bold"),bd=2,relief=GROOVE,bg="yellow",fg="black")
		self.btn_update.place(x=70,y=230,width=170,height=30)
		self.btn_delete=Button(F2,text="Delete",state=DISABLED,command=self.delete,font=("arial 20 bold"),bd=2,relief=GROOVE,bg="violet",fg="black")
		self.btn_delete.place(x=270,y=230,width=170,height=30)
		

		#*********Frame3
		F3=Frame(self.root,bd=10,relief=GROOVE,bg="blue")
		F3.place(x=650,y=370,width=700,height=330)

		#calculator Frame
		self.var_txt=StringVar()
		self.var_operator=''

		#Function to print values on calculator
		def btn_click(num): 
			self.var_operator=self.var_operator+str(num)
			self.var_txt.set(self.var_operator)
		
		#Performs calulations
		def result():
			res=str(eval(self.var_operator))	#eval is inbuilt function that performs arithmatic operation
			self.var_txt.set(res)
			self.var_operator='' 				#for clear screen

		def clear():
			self.var_txt.set('')
			self.var_operator=''

		F4=Frame(F3,bd=7,relief=RIDGE,bg="white")
		F4.place(x=0,y=0,width=260,height=313)

		lbl_calculator=Label(F4,text="Calculator",font="arial 20 bold",bg="Red").place(x=0,y=0,relwidth=1,height=50)

		txt_cal=Entry(F4,font="arial 30 bold",bg="lightgrey",fg="black",
			textvariable=self.var_txt,justify=RIGHT).place(x=0,y=50,relwidth=1)

		# Cal Button row 1
		btn_7=Button(F4,text="7",command=lambda:btn_click(7),
			font="arial 20 bold",bg="tan",fg="black").place(x=0,y=100,width=63,height=50)
		btn_8=Button(F4,text="8",command=lambda:btn_click(8),
			font="arial 20 bold",bg="tan",fg="black").place(x=63,y=100,width=63,height=50)
		btn_9=Button(F4,text="9",command=lambda:btn_click(9),
			font="arial 20 bold",bg="tan",fg="black").place(x=126,y=100,width=63,height=50)
		btn_div=Button(F4,text="/",command=lambda:btn_click('/'),
			font="arial 20 bold",bg="tan",fg="black").place(x=189,y=100,width=61,height=50)

		# Cal Button row 2
		btn_4=Button(F4,text="4",command=lambda:btn_click(4),font="arial 20 bold",bg="tan",fg="black").place(x=0,y=150,width=63,height=50)
		btn_5=Button(F4,text="5",command=lambda:btn_click(5),font="arial 20 bold",bg="tan",fg="black").place(x=63,y=150,width=63,height=50)
		btn_6=Button(F4,text="6",command=lambda:btn_click(6),font="arial 20 bold",bg="tan",fg="black").place(x=126,y=150,width=63,height=50)
		btn_mul=Button(F4,text="*",command=lambda:btn_click('*'),font="arial 20 bold",bg="tan",fg="black").place(x=189,y=150,width=61,height=50)

		#cal Button row 3
		btn_1=Button(F4,text="1",command=lambda:btn_click(1),font="arial 20 bold",bg="tan",fg="black").place(x=0,y=200,width=63,height=50)
		btn_2=Button(F4,text="2",command=lambda:btn_click(2),font="arial 20 bold",bg="tan",fg="black").place(x=63,y=200,width=63,height=50)
		btn_3=Button(F4,text="3",command=lambda:btn_click(3),font="arial 20 bold",bg="tan",fg="black").place(x=126,y=200,width=63,height=50)
		btn_sub=Button(F4,text="-",command=lambda:btn_click('-'),font="arial 20 bold",bg="tan",fg="black").place(x=189,y=200,width=61,height=50)

		# cal Button row4
		btn_0=Button(F4,text="0",command=lambda:btn_click(0),font="arial 20 bold",bg="tan",fg="black").place(x=0,y=250,width=63,height=50)
		btn_dot=Button(F4,text="C",command=clear,font="arial 20 bold",bg="tan",fg="black").place(x=63,y=250,width=63,height=50)
		btn_plus=Button(F4,text="+",command=lambda:btn_click('+'),font="arial 20 bold",bg="tan",fg="black").place(x=126,y=250,width=63,height=50)
		btn_equal=Button(F4,text="=",command=result,font="arial 20 bold",bg="tan",fg="black").place(x=189,y=250,width=61,height=50)
		
		#Salary Frame 
		F5=LabelFrame(F3,text="Salary Receipt",font="arial 17 bold",bd=7,relief=RIDGE,bg="blue",fg="yellow")
		F5.place(x=265,y=0,width=415,height=315)

		F6=Frame(F5,bg="white",bd=2,relief=GROOVE)
		F6.place(x=0,y=0,relwidth=1,height=200)
		self.sample=f'''\tCompany Name,XYZ\n\tAddress: Xyz, Floor4
--------------------------------------------------------------
 Employee ID\t\t:	
 Salary Of\t\t:	Mom-YYYY
 Generated On\t\t:	DD-MM-YYYY
--------------------------------------------------------------
 Todays Days\t\t:	DD
 Total Present\t\t:	DD
 Total Absents\t\t:	DD
 Convence\t\t:	Rs.----
 Medical\t\t:	Rs.----
 PF\t\t:	Rs.----
 Gross Payment\t\t:	Rs.-------
 Net Salary\t\t:	Rs.-------
--------------------------------------------------------------
 This is computer generated slip,not
 required any signature
'''
		scroll_y=Scrollbar(F6,orient=VERTICAL)
		scroll_y.pack(fill=Y,side=RIGHT)

		self.txt_salary_receipt=Text(F6,font="arial 13",bg="lightyellow",yscrollcommand=scroll_y.set)
		self.txt_salary_receipt.pack(fill=BOTH,expand=1)
		scroll_y.config(command=self.txt_salary_receipt.yview)
		self.txt_salary_receipt.insert(END,self.sample)

		self.btn_print =Button(F5,text="PRINT",state=DISABLED,command=self.print,font="arial 20 bold",bg="lightblue",fg="black",bd=10,relief=GROOVE)
		self.btn_print.place(x=270,y=207,width=120,height=60)
		
		self.check_connection()

	
		self.root=ttk.Treeview(self.root,yscrollcommand=scrolly.set)
		self.root=ttk.Treeview(self.root,xscrollcommand=scrollx.set)
		scrollx.config(command=self.root.xview)
		scrolly.config(command=self.root.yview)
		self.root.pack(fill=BOTH,expand=1)


#*************************************All Function**************************************************************************************************************************	
	def search(self):
		try:
			con=pymysql.connect(host="localhost",user="root",password="",db="ems")
			cur=con.cursor()
			cur.execute("select *from emp_salary where e_id=%s",(self.var_emp_code.get()))  
			row=cur.fetchone()
			#print(row)
			if row ==None:
				messagebox.showerror("Error","Invalid Employee ID,please try another ID",parent=self.root)
			else:			
				print(row)
				self.var_emp_code.set(row[0])
				self.var_designation.set(row[1])
				self.var_name.set(row[2])
				self.var_age.set(row[3])
				self.var_gender.set(row[4])
				self.var_email.set(row[5])
				self.var_doj.set(row[6])
				self.var_dob.set(row[7])
				self.var_expr.set(row[8])
				self.var_pid.set(row[9])
				self.var_cno.set(row[10])
				self.txt_address.delete('1.0',END)
				self.txt_address.insert(END,row[11])
				self.var_month.set(row[12])
				self.var_year.set(row[13])
				self.var_bsal.set(row[14])
				self.var_tdays.set(row[15])
				self.var_absents.set(row[16])
				self.var_medical.set(row[17])
				self.var_pfund.set(row[18])
				self.var_convence.set(row[19])
				self.var_nsal.set(row[20])
				file_=open('Salary_receipt/'+str(row[21]),'r')
				self.txt_salary_receipt.delete('1.0',END)
				for i in file_:
					self.txt_salary_receipt.insert(END,i)
				file_.close()
				self.btn_save.config(state=DISABLED)
				self.btn_update.config(state=NORMAL)
				self.btn_delete.config(state=NORMAL)
				self.txt_code.config(state='readonly')
				self.btn_print.config(state=NORMAL)	
		except Exception as ex:
				messagebox.showerror("Error",f"Error due to: {str(ex)}")

	def clear(self):
		self.btn_save.config(state=NORMAL)
		self.btn_update.config(state=DISABLED)
		self.btn_delete.config(state=DISABLED)
		self.btn_print.config(state=DISABLED)
		self.txt_code.config(state=NORMAL)

		self.var_emp_code.set('')
		self.var_designation.set('')
		self.var_name.set('')
		self.var_age.set('')
		self.var_gender.set('')
		self.var_email.set('')
		self.var_doj.set('')
		self.var_dob.set('')
		self.var_expr.set('')
		self.var_pid.set('')
		self.var_cno.set('')
		self.txt_address.delete('1.0',END)
	
		self.var_month.set('')
		self.var_year.set('')
		self.var_bsal.set('')
		self.var_tdays.set('')
		self.var_absents.set('')
		self.var_medical.set('')
		self.var_pfund.set('')
		self.var_convence.set('')
		self.var_nsal.set('')
		self.txt_salary_receipt.delete('1.0',END)
		self.txt_salary_receipt.insert(END,self.sample)


	def delete(self):
		if self.var_emp_code.get()=='':
			messagebox.showerror("Error","Employee id must be required")
		else:
			try:
				con=pymysql.connect(host="localhost",user="root",password="",db="ems")
				cur=con.cursor()
				cur.execute("select *from emp_salary where e_id=%s",(self.var_emp_code.get()))  
				row=cur.fetchone()
				#print(row)
				if row ==None:
					messagebox.showerror("Error","Invalid Employee ID,please try another ID",parent=self.root)
				else:
					op=messagebox.askyesno("Confirm","Do you really want to delete?")
					print(op)
					if op==True:
						cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
						con.commit()
						con.close()
						messagebox.showinfo("Error","Employee Record Deleted Succesfully",parent=self.root)						
						self.clear()
			except Exception as ex:
					messagebox.showerror("Error",f"Error due to: {str(ex)}")


	def add(self):
		if self.var_emp_code.get()=='' or self.var_nsal.get()=='' or self.var_name.get()=='':
			messagebox.showerror("Error","Employee Details are required")

		else:
			try:
				con=pymysql.connect(host="localhost",user="root",password="",db="ems")
				cur=con.cursor()
				cur.execute("select *from emp_salary where e_id=%s",(self.var_emp_code.get()))  
				row=cur.fetchone()
				#print(row)
				if row !=None:
					messagebox.showerror("Error","This Employee id  has already available in our record,try again with another id",parent=self.root)
				else:			
					cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
					(
						self.var_emp_code.get(),
						self.var_designation.get(),
						self.var_name.get(),
						self.var_age.get(),
						self.var_gender.get(),
						self.var_email.get(),
						self.var_doj.get(),
						self.var_dob.get(),
						self.var_expr.get(),
						self.var_pid.get(),
						self.var_cno.get(),
						self.txt_address.get('1.0',END),
						self.var_month.get(),
						self.var_year.get(),
						self.var_bsal.get(),
						self.var_tdays.get(),
						self.var_absents.get(),
						self.var_medical.get(),
						self.var_pfund.get(),
						self.var_convence.get(),
						self.var_nsal.get(),
						self.var_emp_code.get()+".txt"												
					)		
					)
					con.commit()
					con.close()
					file_=open('Salary_receipt/'+self.var_emp_code.get()+".txt",'w')
					file_.write(self.txt_salary_receipt.get('1.0',END))
					file_.close()

					messagebox.showinfo("Success","Record Added Successfully")

					self.btn_print.config(state=NORMAL)

			except Exception as ex:
				messagebox.showerror("Error",f"Error due to: {str(ex)}")
			
	def update(self):
		if self.var_emp_code.get()=='' or self.var_nsal.get()=='' or self.var_name.get()=='':
			messagebox.showerror("Error","Employee Details are required")

		else:
			try:
				con=pymysql.connect(host="localhost",user="root",password="",db="ems")
				cur=con.cursor()
				cur.execute("select *from emp_salary where e_id=%s",(self.var_emp_code.get()))  
				row=cur.fetchone()
				#print(row)
				if row ==None:
					messagebox.showerror("Error","This Employee id  is Invalid,try again with another id",parent=self.root)
				else:			
					cur.execute("UPDATE `emp_salary` SET `Designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
					(						
						self.var_designation.get(),
						self.var_name.get(),
						self.var_age.get(),
						self.var_gender.get(),
						self.var_email.get(),
						self.var_doj.get(),
						self.var_dob.get(),
						self.var_expr.get(),
						self.var_pid.get(),
						self.var_cno.get(),
						self.txt_address.get('1.0',END),
						self.var_month.get(),
						self.var_year.get(),
						self.var_bsal.get(),
						self.var_tdays.get(),
						self.var_absents.get(),
						self.var_medical.get(),
						self.var_pfund.get(),
						self.var_convence.get(),
						self.var_nsal.get(),
						self.var_emp_code.get()+".txt",
						self.var_emp_code.get()												
					)		
					)
					con.commit()
					con.close()
					file_=open('Salary_receipt/'+self.var_emp_code.get()+".txt",'w')
					file_.write(self.txt_salary_receipt.get('1.0',END))
					file_.close()

					messagebox.showerror("Success","Record Updated Successfully")

			except Exception as ex:
				messagebox.showerror("Error",f"Error due to: {str(ex)}")
			



	def calculate(self):
		if self.var_month.get()=='' or self.var_year.get()=='' or self.var_month.get()=='' or self.var_bsal.get()=='' or self.var_tdays.get()=='' or self.var_absents.get()=='' or self.var_medical.get()=='' or self.var_pfund.get()=='' or self.var_convence.get()=='': 
			messagebox.showerror('Error','All field are required')
		else:
			per_day=int(self.var_bsal.get())/int(self.var_tdays.get())
			work_day=int(self.var_tdays.get())-int(self.var_absents.get())
			sal_=per_day*work_day
			deduct=int(self.var_medical.get())+int(self.var_pfund.get())
			addition=int(self.var_convence.get())
			net_sal=sal_-deduct+addition
			self.var_nsal.set(str(round(net_sal,2)))

			#***************Update the receipt*********************************
			new_sample=f'''\tCompany Name,XYZ\n\tAddress: Xyz, Floor4
--------------------------------------------------------------
 Employee ID\t\t:	{self.var_emp_code.get()}
 Salary Of\t\t:	{self.var_month.get()}-{self.var_month.get()}
 Generated On\t\t:	{str(time.strftime("%d-%m-%Y"))}
--------------------------------------------------------------
 Todays Days\t\t:	{self.var_tdays.get()}
 Total Present\t\t:	{str(int(self.var_tdays.get())-int(self.var_absents.get()))}
 Total Absents\t\t:	{self.var_absents.get()}
 Convence\t\t:	Rs.{self.var_convence.get()}
 Medical\t\t:	Rs.{self.var_medical.get()}
 PF\t\t:	Rs.{self.var_pfund.get()}
 Gross Payment\t\t:	Rs.{self.var_bsal.get()}
 Net Salary\t\t:	Rs.{self.var_nsal.get()}
--------------------------------------------------------------
 This is computer generated slip,not
 required any signature
'''			
			self.txt_salary_receipt.delete('1.0',END)
			self.txt_salary_receipt.insert(END,new_sample)

			
	def check_connection(self):
		try:
			con=pymysql.connect(host="localhost",user="root",password="",db="ems")
			cur=con.cursor()
			cur.execute("select *from emp_salary")
			rows=cur.fetchall()
			print(rows)
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to: {str(ex)}")

	def show(self):
		try:
			con=pymysql.connect(host="localhost",user="root",password="",db="ems")
			cur=con.cursor()
			cur.execute("select *from emp_salary")
			rows=cur.fetchall()
			#print(rows)
			self.employeee_tree.delete(*self.employeee_tree.get_children())
			for row in rows:
				self.employeee_tree.insert('',END,values=row)
			con.close()
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to: {str(ex)}")

	def employee_frame(self):
		self.root2=Toplevel(self.root)
		self.root2.title("Employee Payroll Management System")
		self.root2.geometry("1000x500+120+90")
		self.root2.config(bg="white")
		#self.root2.resizable(0,0)
		title=Label(self.root2,text="All Employee Details",
			  font=("arial",30,"bold"),bg="black",fg="white",bd=10,relief=GROOVE,padx=10).pack(side=TOP,fill=X)
		self.root2.focus_force()

		scrolly=Scrollbar(self.root2,orient=VERTICAL)
		scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
		scrolly.pack(side=RIGHT,fill=Y)
		scrollx.pack(side=BOTTOM,fill=X)


		self.employeee_tree=ttk.Treeview(self.root2,columns=('e_id', 'Designation', 'name', 'age', 'gender', 'email', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
		self.employeee_tree.heading('e_id',text='EID')
		self.employeee_tree.heading('Designation',text='Designation')
		self.employeee_tree.heading('name',text='Name')
		self.employeee_tree.heading('age',text='Age')
		self.employeee_tree.heading('gender',text='Gender')
		self.employeee_tree.heading('email',text='Email')
		self.employeee_tree.heading('doj',text='D.O.J')
		self.employeee_tree.heading('dob',text='D.O.B')
		self.employeee_tree.heading('experience',text='Experience')
		self.employeee_tree.heading('proof_id',text='Proof ID')
		self.employeee_tree.heading('contact',text='Contact')
		self.employeee_tree.heading('address',text='Address')
		self.employeee_tree.heading('month',text='Month')
		self.employeee_tree.heading('year',text='Year')
		self.employeee_tree.heading('basic_salary',text='Basic Salary')
		self.employeee_tree.heading('t_days',text='Total Days')
		self.employeee_tree.heading('absent_days',text='Absent Days')
		self.employeee_tree.heading('medical',text='Medical')
		self.employeee_tree.heading('pf',text='PFund')
		self.employeee_tree.heading('convence',text='Convence')
		self.employeee_tree.heading('net_salary',text='Net Salary')
		self.employeee_tree.heading('salary_receipt',text='Salary Receipt')
		self.employeee_tree['show']='headings'
		self.employeee_tree.column('e_id',width=100)
		self.employeee_tree.column('Designation',width=100)
		self.employeee_tree.column('name',width=100)
		self.employeee_tree.column('age',width=100)
		self.employeee_tree.column('gender',width=100)
		self.employeee_tree.column('email',width=100)
		self.employeee_tree.column('doj',width=100)
		self.employeee_tree.column('dob',width=100)
		self.employeee_tree.column('experience',width=100)
		self.employeee_tree.column('proof_id',width=100)
		self.employeee_tree.column('contact',width=100)
		self.employeee_tree.column('address',width=500)
		self.employeee_tree.column('month',width=100)
		self.employeee_tree.column('year',width=100)
		self.employeee_tree.column('basic_salary',width=100)
		self.employeee_tree.column('t_days',width=100)
		self.employeee_tree.column('absent_days',width=100)
		self.employeee_tree.column('medical',width=100)
		self.employeee_tree.column('pf',width=100)
		self.employeee_tree.column('convence',width=100)
		self.employeee_tree.column('net_salary',width=100)
		self.employeee_tree.column('salary_receipt',width=100)
		scrollx.config(command=self.employeee_tree.xview)
		scrolly.config(command=self.employeee_tree.yview)
		self.employeee_tree.pack(fill=BOTH,expand=1)

		self.show()
		self.root2.mainloop()

	def print(self):
		file_=tempfile.mktemp(".txt")
		open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
		os.startfile(file_,'print')

root=Tk()
obj=employeeSystem(root)
root.mainloop()