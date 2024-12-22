#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python program to create a list, a dictionary, and a set. Perform basic operations like adding, removing, and modifying elements.

# Create a list
my_list = [1, 2, 3, 4, 5]
print("Create a list",my_list)

# Adding elements to the list
my_list.append(6)
print("Added an element to the list",my_list)

# Removing an element from the list
my_list.remove(3)
print("Removed an element from the list",my_list)

# Modifying an element in the list
my_list[0] = 10
print("Modified an element in the list",my_list)

# Create a dictionary
my_dict = {'Name': 'John', 'Age': 25, 'City': 'Delhi'}
print("Create a dictionary",my_dict)

# Adding a key-value pair to the dictionary
my_dict['Gender'] = 'Male'
print("Adding a key value pair to the dictionary",my_dict)

# Removing a key-value pair from the dictionary
del my_dict['Age']
print("Remove a key value pair from the dictionary",my_dict)

# Modifying a value in the dictionary
my_dict['City'] = 'Banglore'
print("Modifying a value in the dictionary",my_dict)

# Create a set
my_set = {1, 2, 3, 4, 5}
print("Create a set",my_set)

# Adding an element to the set
my_set.add(6)
print("Adding an element to the set",my_set)

# Removing an element from the set
my_set.remove(3) 
print("Removing an element from the set",my_set)

