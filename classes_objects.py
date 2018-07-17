#!usr/bin/env python

class Car(object):
	pass

honda = Car() # creating a object
tata = Car()  # creating a object

honda.carname = "Honda City"

print honda.carname
# here we can assign as multiple variable as we want to the instance of the class
# But what if there are more than 50 variables assign to single/multiple instance/s of the class
# it will create a more memory and will more time on execution


# So there is concept/method call init method(also known as constructor, used in other language)

# __init__() : initialized the value of the variables
		# - self : Basically a reference to the object which is going to be calling this function

# so new class generated will be as below:

class Car(object):
	def __init__(self, modelname, price, year):
		self.modelname = modelname    # <--- reference the object
		self.year = year
		self.price = price

	def price_rise(self):
		self.price =  int(self.price * 1.15)

honda = Car('HondaCity', 100000, 2017 )
honda.cc = 2500
print honda.modelname
print honda.cc
print honda.__dict__
print honda.price
honda.price_rise()
print honda.price



