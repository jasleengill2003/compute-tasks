#!/usr/bin/env python
# coding: utf-8

# # Q3

# In[6]:


n = int(input("enter number of students: "))
student_marks = {}
sonuc = 0
average = float()
for i in range(n):
    name, *line = input("enter the marks: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("eneter students name: ")
avg = (student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2])/3
print(avg)


# # Q4

# In[7]:


n = int(input("enter number of email addresses: "))
lst = {}
for i in range(n):
    lst[i] = input("enter email address: ")
    at_rate = 0
    dot = 0
def email_checker(dict):
    for i in range(n):
        email = lst[i].strip().lower()
        lenght = len(email)
        if not "@" in email:
            del lst[i]
            return
        elif not (".com" or ".org" or ".edu" or ".gov" or ".net") in email[-4:]:
            del lst[i]
            return
email_checker(lst)
print(lst)


# # Q5

# In[8]:


string1 = input("enter a string: ")
lst = list(string1)
n = int(input("specify index: "))
a = input("specify character: ")
lst[n] = a
string1 = ''.join(lst)
print(string1)


# # Q6

# In[9]:


number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35, 75, 30]

def num_equal(list):
    n = len(list)
    if list[0] == list[n-1]:
        print("the first and last element of the list are equal")
    else:
        print("the first and last element of the list are not equal")
num_equal(number_x)
num_equal(number_y)


# # Q7

# In[10]:


n = int(input("enter number of rows: "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end = "")
    print("\n")


# In[ ]:


##didnt understand what to do in q2 and q2 is giving error


# # Q1

# In[ ]:


n = int(input("enter number of students: "))
x = int(input("enter number of subjects: "))
student_marks = {}
for i in range(n):
    name, *line = (input("enter the marks: ")).split()
    scores = list(map(float, line))
    student_marks[name] = scores
for name in range(n):
    avg = (student_marks[name][0] + student_marks[name][1] + student_marks[name][2])/3
    print(avg)

