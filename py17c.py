print("sum of number")
print("-------")
sn=int(input("enter the starting no:"))
en=int(input("enter the ending no:"))
d=int(input("enter the difference"))
print("result")
print("---------")
print("series")
count=0
sum=0
for i in range(sn,en+1,d):
    print("+"+i)
  sum=sum+i;
  count++;
  print("sum value:",sum)
  print("count value:",count)
