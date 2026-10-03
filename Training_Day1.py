#question 1
# WAP to remove duplicate characters from the string

# name = "prashant"
# new_name = ""
# for i in name:
#     if i not in new_name:
#         new_name += i

# print("Original name:", name)
# print("After removing duplicates:", new_name)

#------------------------------------------------------------------------------------------
#question 2
#wap to accept three paper marks like m1,m2,m3 and calculate  total,
# percentage,and check if user is passed in all subject so print pass
# else print fail and check if percentage is greater than 65 and user is having
# one project so print he/she is elegible for placement  drive else print not eligible .

# m1 = int(input("Enter marks for paper 1: "))
# m2 = int(input("Enter marks for paper 2: "))
# m3 = int(input("Enter marks for paper 3: "))
# total = m1 + m2 + m3
# percentage = (total / 300) * 100
# print("Total marks:", total)
# print("Percentage:", percentage)
# project = int(input("Enter project status (1 for yes, 0 for no): "))

# if m1 >= 40 and m2 >= 40 and m3 >= 40:
#     print("Pass")
#     if percentage > 65 and project == 1:
#         print("Eligible for placement drive")
#     else:
#         print("Not eligible for placement drive")
# else:
#     print("Fail")

#------------------------------------------------------------------------------------------
#mcq1
# a = [1,2,3,4,5,6,7,8,9]
# a[::2]= 10,20,30,40,50,60
# print(a)

#mcq2
# a = [1,2,3,4,5]
# print(a[3:0:-1]) # Output: [4, 3, 2] ,  0 pe stop matlab wo zero se pehle stop hoga 

#mcq3
# def func(value,values):
#     var = 1
#     values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0]) # Output: 3 [44, 2, 3] ,  yaha pe t ka value change nahi hoga kyuki wo immutable hai aur v ka value change hoga kyuki wo mutable hai    

#mcq4
# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# for i in range(0,4):
#     print(arr[i].pop())

#mcq5
# def f(i,values = []):
#     values.append(i)
#     print(values)

# f(1)
# f(2)
# f(3)
#For example, calling f(1) will print [1], calling f(2) will print [1, 2], and so on. 
# This is because the default list is mutable and retains its state across function calls.

#mcq6
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]= arr[i]
# for i in range(0,6):
#     print(arr[i],end=" ") # Output: 2 3 4 5 6 6 , yaha pe last ka value 6 print hoga kyuki 
   # humne last ka value change nahi kiya hai
   
#mcq7
# a = {(1,2):1,(2,3):2,(4,5):3} #{} mytlb dictuionary hai aur dictionary me key immutable hoti hai isliye humne tuple use kiya hai
# #() tuple hai aur yaha dict me tuple ko key ke roop me use kiya hai aur uske corresponding value ko assign kiya hai
# print(a[4,5])
#ans: 3 , yaha pe humne tuple ko key ke roop me use kiya hai aur uske corresponding value ko print kiya hai

#mcq8
# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])
# #error hai 

#mcq9
# fruit ={}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
        
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(fruit) # Output: {'Apple': 1, 'Banana': 1, 'apple': 1} , yaha pe humne fruit dictionary me key ke roop me fruit name ko use kiya hai aur uske corresponding value ko increment kiya hai agar wo key already exist karta hai to else me new key add kiya hai
# print(len(fruit)) # Output: 3 , yaha pe humne fruit dictionary me total number of keys ko print kiya hai

#mcq10
#for k in arr me jo k hai agar dictionary rahi toh wo  key ko access karega aur agar list rahi toh wo value ko access karega
# arr = {}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# print(arr) # Output: {1: 2, '1': 2} , yaha pe humne arr dictionary me key ke roop me integer 1 
# #aur string '1' ko use kiya hai aur uske corresponding value ko increment kiya hai
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum) # Output: 4 , yaha pe humne arr dictionary me total number of values ko sum kiya hai aur usko print kiya hai
#ans: 4 why kyuki arr dictionary me 2 keys hai aur unke corresponding values ko sum kiya hai aur usko print kiya hai

#mcq11
#arr[1.0] = 4 shows that dictionary keys can be of different data types, including floats. 
# In this case, the key is a float (1.0) and its corresponding value is 4. 
# agar 1.1 liya toh wo new key hoga aur uska value 4 hoga, agar 1.0 liya toh wo existing key hoga aur uska value 4 hoga
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict) # Output: {1: 4, '1': 2} , yaha pe humne my_dict dictionary me key ke roop me integer 1, string '1' aur float 1.0 ko use kiya hai aur unke corresponding values ko assign kiya hai
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]  
# print(sum) # Output: 6 , yaha pe humne my_dict dictionary me total number of values ko sum kiya hai aur usko print kiya hai

#mcq12
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# print(my_dict) # Output: {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12} , yaha pe humne my_dict dictionary me key ke roop me tuples ko use kiya hai aur unke corresponding values ko assign kiya hai
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum) # Output: 30 , yaha pe humne my_dict dictionary me total number of values ko sum kiya hai aur usko print kiya hai
# print(my_dict[(1,2)]) # Output: 12 , yaha pe humne my_dict dictionary me key ke roop me tuple (1,2) ko use kiya hai aur uske corresponding value ko print kiya hai

#mcq13
# box = {}
# jars = {}
# crates = {}
# box['biscuits']= 1
# box['cake']=3
# jars['jam']= 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates)) # Output: 2 , yaha pe humne crates dictionary me total number of keys ko print kiya hai

#mcq14
# dict = {'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print(dict[_])# Output: 96 98 97 , yaha pe humne dict dictionary me keys ko sorted order me print kiya hai
#     print(_) # Output: a b c , yaha pe humne dict dictionary me keys ko sorted order me print kiya hai

#mcq15
# rec = {"Name": "Python","Age":20}
# r = rec.copy() #ye copy method dictionary ka shallow copy banata hai, iska matlab ye hai ki agar original dictionary me koi change hota hai to copied dictionary me wo change reflect nahi hoga
# print(id(r)==id(rec))
# print(id(rec))
# print(id(r)) 
#yaha jo output me random  numvbers aye hai wo memory address hai, iska matlab ye hai ki original dictionary aur copied dictionary ke memory address alag hai, iska matlab ye hai ki dono alag alag objects hai

#------------------------------------------------------------------------------------------
#question 3
#moves zeros to end 
# sample = [0,1,0,3,12]
# for i in sample:
#     if i == 0:
#         sample.append(i)
#         sample.remove(i)
# print(sample)
#------------------------------------------------------------------------------------------
#question 4
#second  largest number in the list
# sample = [7,3,9,2,8]
# sample.sort(reverse=True)
# print(sample)
# print(sample[1])
#--------------------------------------------------------------------------------
#question 5
#given an array , return an array where each element is the product of all the elements in the array except the element itself
#use two passes one left to right and one right to left
# sample = [1,2,3,4]
# left = [1]*len(sample) #1 is used as a placeholder for multiplication, as multiplying by 1 does not change the value
# right = [1]*len(sample)
# for i in range(1,len(sample)):
#     left[i] = left[i-1]*sample[i-1]
# for i in range(len(sample)-2,-1,-1):
#     right[i] = right[i+1]*sample[i+1]
# result = [left[i]*right[i] for i in range(len(sample))] #matlab ye hai ki left aur right ke corresponding elements ko multiply karke result me store karna hai   
# print(result)
#--------------------------------------------------------------------------------
#question 6
# #find intersection of three arrays
# sample1 = [1, 2, 3]
# sample2 = [2, 3, 4]
# sample3 = [3, 4, 5]
# # intersection = list(set(sample1) & set(sample2) & set(sample3))
# # print(intersection)

# #alternate method

# for i in sample1:
#     if i in sample2 and i in sample3:
#         print(i)
#--------------------------------------------------------------------------------
#question 7
#find the maximum number of consecutive 1's in the binary array
#logic: iterate through the array and keep track of the current count of consecutive 1's. If a 0 is encountered, reset the current count to 0. Keep track of the maximum count encountered so far.
# sample = [1,1,0,1,1,1,0,1,1,1,1]
# max_count = 0
# current_count = 0
# for i in sample:
#     if i == 1:
#         current_count += 1
#         max_count = max(max_count, current_count)
#     else:
#         current_count = 0
# print(max_count)
#--------------------------------------------------------------------------------
#question 8
#wap to accept any single chr and check the entered chr is in upper case , lower case, digit, or speacial symbols and according to that print msg.
# ch = input("Enter a single character: ")

# if ch.isupper():
#     print("Entered character is in uppercase.")
# elif ch.islower():
#     print("Entered character is in lowercase.")
# elif ch.isdigit():
#     print("Entered character is a digit.")
# else:
#     print("Entered character is a special symbol.")

#--------------------------------------------------------------------------------
# question 9
# count vowels and consonants in a stringn = "helpforcode"
# n = "helpforcode"
# vowels = 0
# consonants = 0
# for character in n.lower():
#     if character in "aeiou":
#         vowels += 1
#     elif character.isalpha():
#         consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
#--------------------------------------------------------------------------------
