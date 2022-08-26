import math
import os
import random
import re
import sys


n = int(input().strip())

s = input()

k = int(input().strip()) % 26

result =""

for alph in s:
    a=ord(alph)
    if(a>96 and a<123):
        b=a+k
        if(b>122):
            result += (chr(96+(b-122)))
        else:
            result += (chr(b))
    elif(a>64 and a<91):    
        b=a+k
        if(b>90):
            result += (chr(64+(b-90)))
        else:
            result += (chr(b))
    else:
        result += (alph)
    
print(result)    

    

