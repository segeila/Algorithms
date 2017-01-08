# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 11:38:12 2017

@author: della
"""

def karatsuba(n1, n2):
    len1 = len(str(n1))/2
    len2 = len(str(n2))/2
    if len(str(n1))>1 & len(str(n2))>1:
        a = int(str(n1)[:len1])
        b = int(str(n1)[len1:])
        c = int(str(n2)[:len2])
        d = int(str(n2)[len2:]) 
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d)- ac - bd
        xy = 10**len(str(n1))*ac + 10**len1*ad_plus_bc + bd
    else:
        xy = n1*n2
    return xy
