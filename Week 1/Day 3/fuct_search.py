

def search(n,list):
    #n=int("enter a number: ")
   found=False
   i=0
   while i<=len(list) and found==False:
       if list[i]==n:
           found=True
           index=i
       i+=1
   return index

list=[10,8,7,19,42,2]
ans=search(2,list)

print(ans)