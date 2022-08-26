n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
count = 0
    
for i in range(0,n):
    if(ar[i]!=0):
        for j in range(i+1,n):
            if(ar[i]==ar[j]):
                count=count+1
                ar[j]=0
                break
print(count)            

