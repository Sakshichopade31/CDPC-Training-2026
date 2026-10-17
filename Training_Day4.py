# import csv

# roll_no = input("Enter Roll No: ")
# name = input("Enter Name: ")
# mobile = input("Enter Mobile: ")
# p1 = float(input("Enter marks for P1: "))
# p2 = float(input("Enter marks for P2: "))
# p3 = float(input("Enter marks for P3: "))
# email = input("Enter Email: ")

# total = p1 + p2 + p3
# percentage = round(total / 3, 2)
# result = "pass" if all(mark >= 40 for mark in (p1, p2, p3)) else "fail"

# with open("StudentResults.csv", "a", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     if file.tell() == 0:
#         writer.writerow(
#             ["RollNo", "Name", "Mobile", "P1", "P2", "P3", "Email", "Total", "Percentage", "Result"]
#         )
#     writer.writerow(
#         [roll_no, name, mobile, p1, p2, p3, email, total, percentage, result]
#     )

# print(f"Student result has been saved: {result}")

# n = int(input())
# k = int(input())
# prices = list(map(int, input().split()))

# freq = {}
# count = 0

# for price in prices:
#     if k == 0:
#         count += freq.get(price, 0)
#     else:
#         count += freq.get(price - k, 0)
#         count += freq.get(price + k, 0)

#     freq[price] = freq.get(price, 0) + 1

# print(count)


#LinkList - address me store krega aur data structure me store krtq
#add node in beginning  
# #add node in betweekn 

# class Node:
#     def __init__(self,value):
#         self.data = value 
#         self.next = None
        
# class Linkedlist:
#     def __init__(self):
#         self.head = None
        
# linkedlistObj.head = Node(10)
# second = Node(20)
# third = Node(30)
# fourth = Node(40)
# fifth = Node(50)

# linkedlistObj.head.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth

# current = linkedlistObj.head
# while current is not None:
#     print("|", current.data, "|", ">", end="")
#     current = current.next

#5 for dynamic ways
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None  #head is starting node
        self.tail = None   # tail is last node

    # add node at the end
    def addNodeEnd(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def displayLinkedList(self):
        current = self.head
        while current is not None:
            print("|", current.data, "|", ">", end=" ")
            current = current.next
        print("None")

linkedobj = LinkedList()
linkedobj.addNodeEnd(10)
linkedobj.addNodeEnd(20)
linkedobj.addNodeEnd(30)
linkedobj.displayLinkedList()
