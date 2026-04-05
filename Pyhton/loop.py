#sum of n natural number using for and while loops
n=10
sum=0
sum1=0
count=1
while count<=n:
    sum=sum+count
    count+=1
print("Sum of first N natural number:",sum)

for i in range(n+1):
     sum1=sum1+i
    
print("Sum of first N natural number:",sum1)

#print prime number between 1-100

for num in range(1,101):
     if num>1:
        for i in range(2,num):
               if num%i==0:
                    break
        else:
            print(num)
#break continue and pass
count=0
while count<=10:
     if count==3:
          continue
     # elif count==5:
     #      break
     count+=1
     print(count)

                
        
            
        