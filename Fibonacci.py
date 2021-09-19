# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:52:11 2021

@author: UC17
"""

#Program to print Fibonacci series

n_terms = int(input ("How many terms the user wants to print? "))  
  
# First two terms  
n1 = 0  
n2 = 1  
count = 0  
  
# Now, we will check if the number of terms is valid or not  
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")
    
# if there is only one term, it will return n1  
elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n1)  
    
# Then we will generate Fibonacci sequence of number  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n_terms:  
        print(n1)  
        nth = n1 + n2  
        
       # At last, we will update values  
        n1 = n2  
        n2 = nth  
        count += 1