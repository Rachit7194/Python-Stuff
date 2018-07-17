# import re

# # find particular words nad
# #:return the list of matches from the list

# string ="""
# 		Rachit is 24 and Varun is 25
# 		Naresh is 26 and Jaysavsani is 26
# 		"""

# ages = re.findall(r"\d{1,3}", string)
# names = re.findall(r"[A-z][a-z]*", string)
# print names
# print ages



# # re for finding particular words more than one

# string = "my name is rachit and my nickname is also rachit"
# particular_word =  re.findall("rachit", string)
# # print type(particular_word)



# # re iterator
# # span method gives starting and ending index for particular string pattern searched.

# for i in re.finditer("rachit", string):
# 	print i.span()

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner


# @make_pretty
# def ordinary():
#     print("I am ordinary")


# ordinary()
# pretty = make_pretty(ordinary)
# print pretty()




def check_calc(func):
	def modification(a,b):
		print("I am going to divide",a,"and",b)
		if int(b) < 1:
			return "Please give valid"
		return func(a,b)
	return modification



@check_calc
def divide(a=10,b=5):
	print a,b
	return a/b


# divide()


# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! cannot divide")
#          return

#       return func(a,b)
#    return inner

# @smart_divide
# def divide(a,b):
#     return a/b



print divide(a=10,b=0)