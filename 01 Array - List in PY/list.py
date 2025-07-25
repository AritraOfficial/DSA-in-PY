''' ````````````````````````````````````````````` || LIST  || ````````````````````````````````````````````` '''


# =====================================================================================================================================
'''                                                Define a Demo List                                                           '''

# List_Demo = []   #<----------- Empty List
# List_demo = [1, 233.5, 'Aritra', True, "AriX"]     #<--------- Hold multiple types elements at once. 
# print(List_demo)

# ___________________________________  INDEXING  _____________________________________
# print("First element from STARTING POINT & Last Element from END Point ->> ", List_demo[0])
# print("Last Element from Start Point & First element from last ->> ", List_demo[-1])

# ___________________________________  Using 'title()' method  _____________________________________
# title() - is method where --- words start with uppercase characters and all remaining cased characters have lower case.

# who = ['arim.', 'successful', 'ai & data scientist', 'specialized']
# print(who[2].title())
# print(f"I am {who[0].title()}, working as {who[2].title()}, {who[3]}.")
# =====================================================================================================================================


# =====================================================================================================================================
'''                                             Using   'list()'  constructor  method                                            ''' 

# Convert an  iterable(like - DICT, FLOAT, TUPLE, STR) into list. 
# b = list((1,2,3,4.9, "AriX", True))
# print(b, '\n TYPE OF B:', type(b))
# =====================================================================================================================================


# =====================================================================================================================================
'''                                       2D List >> Demonstrate LIST ARE MUTABLE  | Shallow Copy                                  '''

# a = [[1, 2, 3],
#      [4, 5, 6]]
# a1 = list(a)    # <--------- Shallow Copy

# a1[1][2] = 5000   #<---- Change the value 
# print(a)    
# =====================================================================================================================================


# =====================================================================================================================================
'''                                             Modifying Elements in a List                                                    '''

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles[0] = 'ducati' 
# print(motorcycles)
# =====================================================================================================================================


# =====================================================================================================================================
'''                                                  Adding Elements to a List                                                  '''
# a = []   #<--- empty list 
# ___________________________________  Using 'append' method  _____________________________________
# a.append('Aritra')
# ___________________________________  Using 'extend[]' method  _____________________________________
# a.extend(['Mukherjee', 'AI', 'ML', 'DL'])
# ___________________________________  Using 'insert' method  _____________________________________
# a.insert(0, 'Data Scientist')
# print(a)
# ======================================================================================================================================


# ======================================================================================================================================
'''                                                    Removing Elements from List                                                  '''
# a = [100, 12, 90, 40, 7000, 'false']
# print('Before remove array > ', a)
# ___________________________________  Using 'remove()' method  _____________________________________
# r = 40
# a.remove(r)
# print('After using remove() >', a, "remove element> ", r)
# ___________________________________  Using 'remove() - Removing an Item by Value' method  _____________________________________
# a.remove('false')
# print(a)    
# ___________________________________  Using 'pop()' method  _____________________________________
# pop_val= a.pop(2)
# print('After using pop() >', a)
# ___________________________________  Using 'del' method  _____________________________________
# del a[0]
# print('After using del >', a)
# ======================================================================================================================================


# ======================================================================================================================================
'''                                                      Organizing a List                                                          '''
# a = ['xyz', 'ari', 'super', 'mukherjee', '40']
# print('The Original array > ', a)
# ___________________________________  Using 'sort()' method  _____________________________________
#a.sort()
# print('After sort array >', a)
# print('The Original array > ', a) #<-- give same as sort array because - Sorting a List Permanently with the sort() Method
# ___________________________________  Using 'sorted()' method  _____________________________________
# print('After sort array >', sorted(a))
# print('The Original array > ', a) #<-- give same as sort array because - Sorting a List Temporarily with the sorted() Function
# ======================================================================================================================================


# ======================================================================================================================================
'''                                                     Printing a List in Reverse Order                                            '''
# a = ['xyz', 'ari', 'super', 'mukherjee', '40']
# print('The Original array > ', a)
# a.reverse()
# print('After reverse array > ', a)
# ---------------------------------------------------------------------------
'''                         Finding The Length of List                  '''
# print('Length of list  >>', len(a))
# ======================================================================================================================================



# ======================================================================================================================================
'''                                           Looping through an entire list                                                        '''
# a = ['xyz', 'ari', 'super', 'mukherjee', '40']
# for i in a:
#     print(i)
# ----------------------------------------------------------------------
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#  print(f"{magician.title()}, that was a great trick!")
#  print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")
# ======================================================================================================================================



# ======================================================================================================================================
'''                                          Making Numerical Lists

                                           Using the range () Function                                                              '''
# for value in range(1,5):
#     print(value)
# --------------------------------------------------------------------------------------------------------------
'''                                      Using range() to Make a List of Numbers                            ''' 
# number = list(range(1,10))
# print(number)
# --------------------------------------------------------------------------------------------------------------
#                                          Find the Even and Odd by using range()
# even_number = list(range(2,15,2))
# print("Even Numbers> ", even_number)
# odd_num = list(range(3,20,3))
# print("Odd Number > ", odd_num)
# the range() function starts with the value 2 and the adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value 15.
# --------------------------------------------------------------------------------------------------------------
'''                                     Find the square in list range()                                      '''
# square = []
# for value in range(1,13):
#     s = value ** 2
#     # square.insert(0, s)  #<--- same but it returns the values in reverse 
#     square.append(s)
# print(square)
# ````` Enhanced Code - List Comprehensions ```````
# The approach described earlier for generating the list squares consisted of using three or four lines of code.
# squares = [value**2 for value in range(1, 11)]
# print(squares)
# ======================================================================================================================================



# ======================================================================================================================================
'''                                             Simple Statistics with a List of Numbers                                            '''
# num = list(range(1,11))
# print(min(num))
# print(max(num))
# print(sum(num))
# number = 1
# for i in num:
#     number *= i
# print(number)
# # ````` Enhanced Code ```````
# import math 
# print(math.prod(num))
# ======================================================================================================================================



# ======================================================================================================================================
'''                                                         Slicing a List                                                          '''
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[3:])
# --------------------------------------------------------------------------------------------------------------
'''                                             Looping Through Slicing                                    '''
# for i in players[:3]:
#     print(i.title())
# --------------------------------------------------------------------------------------------------------------
'''                                             Copying a List                                             '''
# a = players[:]      # create a same copy list as 
# print(a)
# ======================================================================================================================================



# ======================================================================================================================================
'''                                                    Nested Lists in Python                                                  '''
# import numpy as np 
# m = np.array([[1,2,3],                      
#               [4,5,6],
#               [9,10,12]])
# print(m[1][2])
# Indexing Looks like --- 
#      0  1  2
#     -- -- --
#   0| 1  2  3
#   1| 4  5  6 
#   2| 7  8  9     #print(m[1][2])  <---- o/p=6
# ======================================================================================================================================