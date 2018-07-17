#usr/bin/env python

#Single inheritance:

class Car(object):
	def __init__(self, modelname, price, year, fuel):
		self.modelname = modelname    # <--- reference the object
		self.year = year
		self.price = price
		self.fuel = fuel
	def price_rise(self):
		self.price =  int(self.price * 1.15)



class Fastestcar(Car):
	pass

# Lamborghini = Fastestcar("Gallerion", 2014, 566666666)
# print Lamborghini.price 
# Lamborghini.price_rise()
# print Lamborghini.price


######################################################################## Multiple inheritance


class Vintagecar(Car):
	pass



class Musclecar(Fastestcar, Vintagecar):
	pass




# Vindiesal_cielo = Musclecar("Vindiesal", 8900000,  2014)
# print Vindiesal_cielo.modelname
# Vindiesal_cielo.price_rise()
# print Vindiesal_cielo.price



######################################################################## Multilevel Inheritance


class Oldagecar(Car):
	def on_petrol(self):
		self.fuel = "petrol"




class small_car(Oldagecar):
	def average(self):
		return "14km/ltr"



omni = small_car("maruti_omni", 300000, 1992, "diesel")
print omni.modelname
omni.on_petrol()
print omni.fuel
print omni.average()
print omni.price
omni.price_rise()
print omni.price



#################################################################### Hybrid Inheritance



#combination of Multiple inheritance and Multilevel inheritance

class A():
	def __init__(self, w):
		self.w = w


class B(A):
	def __init__(self, x, w, y):
		self.x = x
		print "Init of class B"
		super(B, self).__init__(w, y)


class C(A):
	def __init__(self, w, y):
		self.y =y
		print "Init of class C"
		super(C, self).__init__(w)


class D(B,C):
	def __init__(self, w, x, y, z):
		self.z = z
		print "Init of class D"
		super(D, self).__init__(w,x,y)


d = D(1,2,3,4)
print d.mro()