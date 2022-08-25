import math
import os
import random
import re
import sys

q = int(input().strip())

for q_itr in range(q):
        s = input()
        
        count = 0

        c= ((len(s))/2)
        if(c == int(c)):
            a = list(s)
            s1 = list(s[:int(c)])
            s2 = list(s[int(c):])
            res = []
    
        
            for el1 in s1:
                if el1 not in s2:
                    res.append(el1)
                else:
                    s2.remove(el1)   
        
            print(len(s2))
        else:
            print('-1')
#hi                        
