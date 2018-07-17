"""
Linear Search Algo:

"""
def linear_search(findx, search_list):
	if findx not in search_list:
		return "element not in list"
	index = 0
	iteration = 0
	while index < len(search_list):
		iteration += 1
		if search_list[index] == findx:
			print "Iteration - :" + str(iteration)
			return "Position of findx is: " + str(index)
		index +=1
	return -1



# print linear_search(24, [23,34,12,25,65,7, 24])




# def binary_search(findx, search_list):
# 	if findx not in search_list:
# 		return "Not in List"
# 	left_index = 0
# 	right_index = len(search_list) -1
# 	print right_index
# 	mid_index = int((left_index + right_index)/2)
# 	print mid_index
# 	while search_list[mid_index] != findx:
# 		if search_list[mid_index] < findx:
# 			left_index += 1
# 		elif search_list[mid_index] > findx:
# 			right_index -= 1

# 		mid_index = int((left_index+right_index)/2)

# 	return "Position for findx : " + str(mid_index)


# binary_search(14, [4,8,12,16,20,24,28])

# class Axis(object):
# 	b= 20
# 	__C = 30
# 	def __init__(self):
# 		self.A = 10
# 	def printme(self):
# 		print self.A
# 		print b
# 		print self.__C


# Axis().printme()


# class Base(object):
#     def __init__(self):
#         print "Base created"

# class ChildA(Base):
#     def __init__(self):
#         Base.__init__(self)

# class ChildB(Base):
#     def __init__(self):
#         super(ChildB, self).__init__()

# ChildA() 
# ChildB()