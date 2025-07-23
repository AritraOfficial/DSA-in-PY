# ````````````````````  Question 1  `````````````````` 
# li = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
# print (li[1][-1]) 

# Explanation :>> 
# li[1] refers to the second element 'Pratik'. li[1][-1] accesses the last character of 'Pratik', which is 'k'.
# ======================================================================


# ````````````````````  Question 2  `````````````````` 
# li = [1, 2, 3, 4] 
# li.append([5,6,7,8]) 
# print(li) 

# Explanation :>> 
# The append() method adds a given object to an existing list. However, if you pass a list to the append method, it will not combine the two lists. Instead, the entire list that is passed will be added as a single element to the original list.
# ======================================================================


# ````````````````````  Question 3  `````````````````` 
# def addToList(a):
#     a += [100], [2300]
# b = [[10,20,30,40], [9,123,234,1325]]
# addToList(b)
# print(b, len(b))

# Explanation :>> 
# In Python, everything is a reference, and references are passed by value. Parameter passing in Python works like reference passing in Java. This means the function can change the value that the passed argument points to. As a result, the value of the variable in the caller’s scope can be changed. The function “addToList” adds the element 100 to the list. This increases the length of the list by 1. Therefore, the output of the program is 5.
# Each [] consider as individual, if there are multiple values in one [], that also consider as []=one individual 
# ======================================================================


# ````````````````````  Question 4  `````````````````` 
# a = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
# b = a 
# c = a[:] 
# # c = a 
# # b = a[:] 

# b[0] = 'Code'
# c[1] = 'Mcq'

# count = 0
# for c in (a, b, c): 
# 	if c[0] == 'Code': 
# 		count += 1
# 	if c[1] == 'Mcq': 
# 		count += 10
# print (a , count) 

# Explanation :>> 
""" When we assign a to b, we create a second reference to the same list. Changes to b affect a. When we assign the slice of all elements in a to c, we create a full copy of a that can be modified independently. Any change in c will not affect a. 
    So while checking, ‘Code’ gets matched and the count increases to 1, but Mcq doesn't get matched since it's only available in c. 
Now checking b, ‘Code’ gets matched again, raising the count to 2. 
Finally, while checking c, which is separate from both a and b, only Mcq gets matched and the count becomes 12. """
# Match 'a' = 1, match 'b' = 1, total => a+b =1+1 = 2 then match quiz (in c) = 10, total => a+b+c = 1+1+10 = 12 
# increase 1 or 10 (as given, BUT it can be different value, if you give like count +=100, also same, 100+100+10 = 210)
# ======================================================================


# ````````````````````  Question 5  `````````````````` 
# def gfg(x,li=[]): 
# 	for i in range(x): 
# 		li.append(i*i) 
# 	print(li) 

# gfg(5,[4,3,2,1]) 

# Explanation :>> 
#The function appends squares of numbers from 0 to x-1(index) to the given list li. Since the list [3,2,1] is passed explicitly, the result is [3, 2, 1, 0, 1, 4].
# It just make the square.
# ======================================================================