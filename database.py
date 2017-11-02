import mysql.connector
import mysql
import sys



children = []
class kid:
	def __init__(self,v,w,x,y,z):
		self.name = v
		self.age = w
		self.grade = x
		self.address = y
		self.phone = z


	def getName(self):
		return self.name

	def describe(self):
			print "Child name: " + str(self.name)
			print "Child age: " + str(self.age)
			print "Child grade: " + str(self.grade)
			print "Child address: " + str(self.address)
			print "Child phone number: " + str(self.phone)

def pull(name):
	# lggic
	# get a kid from children
	# take the kid out of childen
	for x in children:
		if name == x.getName():
			children.remove(x)

def kidInfo(x):
	print x.describe()

def allDisplay():
	map(kidInfo,children)


def allDisplayname():
	for x in children:
		print x.name


def display(name):
	# find a kid from children list
	# kid.describe()
	for x in children:
		if name == x.getName():
			x.describe()

cnx = mysql.connector.connect(user = 'root', password = "max990322",host = '127.0.0.1', database = 'joowon')
cursor = cnx.cursor()
cursor.execute("SELECT * from kid")

data = cursor.fetchall()
for alldata in data:
	v = alldata[0]
	w = alldata[1]
	x = alldata[2]
	y = alldata[3]
	z = alldata[4]
	children.append(kid(v,w,x,y,z))
cnx.commit()
cnx.close()


cnx = mysql.connector.connect(user = 'root', password = "max990322",host = '127.0.0.1', database = 'joowon')
cursor = cnx.cursor()
while 1 > 0:
	print "Welcome to the Kid's Summer Program!"
	print "1. Register a Kid"
	print "2. Pull kid from program"
	print "3. See kid's information"
	print "4. Exit"
	number = raw_input()
	if number == "1":
		print "What is the child's name? ",
		v = raw_input()
		print "What is his/her age? ",
		w = raw_input()
		print "What grade is he/she in? ",
		x = raw_input()
		print "What is his/her address? ",
		y = raw_input()
		print "What is his/her phone number? ",
		z = raw_input()
		children.append(kid(v,w,x,y,z))
		add_kid = ("INSERT INTO kid" "(name, age, grade, address, phone)" "VALUES (%s, %s, %s, %s, %s)")
		data_kid = (v,w,x,y,z)
		cursor.execute(add_kid,data_kid)
		cnx.commit()
		cnx.close()
		print "Your child, " + v + " has been added to the system."
	elif number == "2":
		print "Which kid would you like to pull out (type name)?"
		name = raw_input()
		pull(name)
		print "Your child, " + name + ", has been removed."
		print "Remaining kids in program: "
		allDisplayname()

	elif number == "3":
		print "Which child's information would you like to see?"
		name = raw_input()
		display(name)
	elif number == "4":
		print "Thank you!"
		'''
		for child in children:
			v = child.name
			w = child.age
			x = child.grade
			y = child.address
			z = child.phone
			add_kid = ("INSERT INTO kid" "(name, age, grade, address, phone)" "VALUES (%s, %s, %s, %s, %s)")
			data_kid = (v,w,x,y,z)
			cursor.execute(add_kid,data_kid)
			cnx.commit()
		cnx.close()
		exit()
		'''
	else:
		print "Not an option, please select a number 1 - 4."

