# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:19:50 2020

@author: Juhana
"""

import numpy as np

""" Alustukset ja tiedoston sisäänluku"""

with open(r"C:\Users\Juhana\Desktop\input2.txt", 'r') as file:
     pituus = [line.strip() for line in file]
     j = 0
    

     pituus_2 = list()
     policy = list()
     policy_2 = list()
     policy_len = list()
     policy_len_2 = list()
     policy_len_min = list()
     policy_len_max = list()
     policy_char = list()
     passwords = list()
     
     for i in pituus:
         pituus_2.append(i.split(":"))
        
     for item in pituus_2:
         policy.append(item[0])
         passwords.append(item[1])
      
     for item in policy:
         policy_2.append(item.split(" "))
         
     for item in policy_2:
         policy_len.append(item[0])
         policy_char.append(item[1])    
         
     for item in policy_len:
         policy_len_2.append(item.split("-"))
    
     for item in policy_len_2:
         policy_len_min.append(int(item[0]))
         policy_len_max.append(int(item[1]))   

#print (len(policy_len_min),len(policy_len_max),len(policy_char),len(passwords))



"""
validien salasanojen etsintä, part 1
"""
i = 0
counter = 0
for password in passwords:
    if password.count(policy_char[i]) >= policy_len_min[i] and password.count(policy_char[i]) <= policy_len_max[i]:
        counter = counter + 1
    i = i + 1

"""
validien salasanojen etsintä, part 2
"""
j = 0
counter_2 = 0

for password in passwords:
    if password[policy_len_min[j]] == policy_char[j] and password[policy_len_max[j]] != policy_char[j]:
        print(j)
        print(password)
        print(policy_char[j])
        print(policy_len_min[j])
        print(password[policy_len_min[j]])
        counter_2 = counter_2 + 1
    elif password[policy_len_min[j]] != policy_char[j] and password[policy_len_max[j]] == policy_char[j]:
        counter_2 = counter_2 + 1
    j = j +1

print(counter_2)
        

        