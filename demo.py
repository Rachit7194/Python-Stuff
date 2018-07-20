#!/usr/bin/env python
"""1.
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""
# def numbers_io():
# 	new_l = [i for i in range(2000,32000) if (i%7==0) and (i%5!=0)]
# 	# print new_l
# 	return new_l

# print(numbers_io())


"""
2. 
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
#Ans 1
# def compute_factorial(number):
# 	if number == 0:
# 		return 1
# 	return number * compute_factorial(number-1)

# print(compute_factorial(5))

#Ans 2
# num = int(raw_input("Enter the number : "))
# n = 1

# while num > 0:
					# 	# if num is 5
# 	n=n*num
					# 	#now n is 5
# 	num = num -1
					# 	#now num is 4
					# 	#2nd iteration
					# 	#num= 4, n = 5
					# 	#n = 5*4, num = 3
					# 	#n = 20*3, num = 2
					# 	#n  = 60*2, num =1
					# 	#return

# print n




"""
3. 
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
# Ans1
# num = int(raw_input("Enter the number : "))
# print {i:i*i for i in range(1,num+1)}

 
"""
4.
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

# Ans1
# num = raw_input("Enter the numbers : \n")
# print [int(x) for x in num.split(",")]
# print tuple(int(x) for x in num.split(","))


"""
5.
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

# Answer
# class Stringmanipulation(object):
# 	def __init__(self):
# 		self.s = ""

# 	def get_string(self):
# 		self.s = raw_input("Enter the name: ")
# 		return self.s

# 	def print_string(self):
# 		return self.s.upper()



# mystring = Stringmanipulation()
# print mystring.get_string()
# print mystring.print_string()

"""
6.
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

# Ans 1
# import math
# def calc_prob(l=[], C=50, H=30):
# 	return [int(math.sqrt((2*C*x)/H)) for x in l]

# usr_input = map(int, raw_input("Enter csv values:").split(","))
# print calc_prob(usr_input)




"""
7.
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
# 
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""
#Answer:
# usr_input = map(int, raw_input("Enter the numbers by comma-separated values:").split(","))
# usr_input = map(int, raw_input("Enter csv values:").split(","))

# row,col  = usr_input
# print row,col

# # multilist = [[0 for col in range(col)] for row in range(row)]
# multilist = []

# for row1 in range(row):
#     for col1 in range(col):
#         multilist[row1][col1]= row1*col1
       
# print(multilist)

# input_str = raw_input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# print multilist
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col

# print multilist



"""
8.
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""
#Ans:
# user_input =  list(map(str, raw_input("Enter the words using comma separated values: ").split(",")))
# print user_input
# print sorted(user_input)



"""
9.
Question:

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""

#Answer:
# user_input = map(str, raw_input("Enter the words using comma separated values: ").split(","))
# print [item.upper() for item in user_input]


"""
10.
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""
#Answer:
# user_input = map(str, raw_input("Please write the sentence with duplicate entries :\n").split(" "))
# new_list = list(set(user_input))
# print new_list



"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""

#Answer1:
# usr_input = raw_input().split(",")
# print [x for x in usr_input if int(x)%5==0]
# print [item for item in usr_input if int(item)%5==0]

#Answer2:

# value = []
# items=[x for x in raw_input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     print intp
#     if not intp%5:
#         value.append(p)

# print ','.join(value)


"""
Question:
12.
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

#Answer:
# val =[]
# def give_even(start=1000, end=3000):
# 	# return [x for x in range(start,end+1) if map(lambda x :int(x)%2==0, str(x).split()) is True]
# 	for x in range(start, end+1):
# 		y= list(str(x).split())
# 		new_y =  list("".join(y[0].split()))
# 		for i in new_y:
# 			if (int(i)%2 == 0):
# 				val.append(x)
# 			else:
# 				break

# 	print list(set(val))

#Answer2:

# print give_even()
# values = []
# for i in range(1000, 3001):
#     s = str(i)

#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print ",".join(values)



#Question 13
"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
#Answer:
# def calc_str_int(string_l=""):
# 	if string_l:
# 		digits, strings  =  [ item for item in string_l.split(" ") if item.isdigit()], [item for item in string_l.split() if isinstance(item, str) and not item.isdigit()]
# 		return {"DIGITS":len(digits), "STRINGS":len(strings)}


# print calc_str_int('hello world! 123 1212 efrr ere 1342 2323w')



#Question 14:
"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

"""
#Answer:
# def calc_str_int(string_l=""):
# 	if string_l:
# 		uppers  =  [ item for item in string_l if item.isupper()]
# 		return {"UPPER":len(uppers)}

# print calc_str_int('Hello world!')


#Question 15:
"""
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

#Answer:

# def calc_value(num=0):
# 	if num:
# 		# return int("%s".format(num)) + int("%s%s".format(num,num)) + int("%s%s%s".format(num,num,num)) + int("%s%s%s%s".format(num,num,num,num))
# 		return int( "%s" % (num) ) + int( "%s%s" % (num,num) ) + int( "%s%s%s" % (num,num,num) ) +  int( "%s%s%s%s" % (num,num,num,num))
# 	else:
# 		return 1


# print calc_value(num =9)




# def check_cal_values(func):
# 	def inner(a,b):
# 		if b == 0:
# 			return "Please enter valid value"
# 		# Now time to call actual function 
# 		func(a,b)
# 	return inner


# @check_cal_values
# def divide_values(a=10,b=5):
# 	print "Before division"
# 	div =  a/b
# 	print "division is successfull"
# 	print div



# print divide_values(10,5)




# class A(object):
# 	def a(self):
# 		print "a"

# 	def a(self):
# 		print "a1"


# A().a()
# #Answer : 


class Cup(object):
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = "dsdfsfsf"  # private variable

    def fill(self, beverage):
        self.__content = beverage
        print self.__content
        print self._color

    def empty(self):
        self.__content = None
        print self.__content



mycup = Cup("red")
print mycup._Cup__content
# print mycup._Cup_color

# mycup.fill("wine")




# mycup.fill("wine")


# def simpleGeneratorFun():
# 	# return1      #never use return
#     yield 1
#     yield 2
#     yield 3


# print [ x for x in simpleGeneratorFun()]


# for value in simpleGeneratorFun(): 
#     print(value)






a=1

def f():
    print 'Inside f() : ', a
 
# Variable 'a' is redefined as a local
def g():    
    a = 2
    print 'Inside g() : ',a
 
# Uses global keyword to modify global 'a'
def h():    
    global a
    a = 3
    print 'Inside h() : ',a
 
# Global scope
# print 'global : ',a
# f()
# print 'global : ',a
# g()
# print 'global : ',a
# h()
# print 'global : ',a



# class Base(object):
# 	def __init__(self):
# 		print "I will print first 1"



# class Child(Base):
# 	def __init__(self):
# 		super().__init__()
# 		print "i will print second 2"



# childObj = Child()



# class Bird:
    
#     def __init__(self):
#         print("Bird is ready")

#     def whoisThis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# # child class
# class Penguin(Bird):

#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")

#     def whoisThis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")

# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()


####################### Multiple inheritance

# class StudentA(object):
# 	batch = "CSE"

# 	def remarks(self):
# 		print "I am brilliant"
		


# class StudentB(object):
# 	"""docstring for StudentB"""
# 	def __init__(self):
# 		pass
# 		# super(StudentB, self).__init__()
# 		# self.arg = arg

# 	def remarks(self):
# 		print "I am Quick Learner"
	


# class StudentC(StudentA, StudentB):
# 	def __init__(self):
# 		print "in student C"
# 		print StudentA.batch
# 		self.neverprint()

# 	@staticmethod
# 	def neverprint(self):
# 		print "Yes i can print from class's object"


# 	def printbyrefernce(self):
# 		# self.neverprint()

# 		print "Yayyy"


# objC = StudentC.neverprint()
# # print objC.batch
# print objC.neverprint()
# print objC



# class Pet(object)	



#############################################################################################################################

# class A(object):
# 	def m(self):
# 		print "called method From class A"


# class B(A):
# 	def m(self):
# 		print "called from class B"
# 		super().m()


# class C(A):
# 	def m(self):
# 		print "called from class C"
# 		super().m()

# class D(B,C):
# 	def m(self):
# 		print "called from class D"
# 		super().m()


# obj = D()
# print obj.m()


# class A(object):
#     def __init__(self, i):
#         self.i = i
#     def run(self, value):
#         return self.i * value

# class B(A):
#     def __init__(self, i, j):
#         super(B, self).__init__(i)
#         self.j = j
#     def run(self, value):
#         return super(B, self).run(value) + self.j



# objB = B("Rachit", "Varun")
# print objB.run(4)


# vowels = ('a', 'e', 'i', 'o', 'u')
# fsetadd = vowels.ad
# fSet = frozenset(vowels)
# print('The frozen set is:', fSet)
# print('The empty frozen set is:', frozenset())
x = frozenset(["VueJS", "zeo", "python", "php", ".net"])
# x.add("VueJS")
# x.add("VueJS")
# print x
# print(dir(set))
 

from collections import Counter
print Counter("abracadabra").most_common()