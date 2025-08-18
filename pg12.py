print("goverment of tamilnadu")
print("electricity of board")
print("--------------")
print("bill recipt")
print("----------")
eb=int(input("enter the eb no"))
name=input("enter the name")
pu=int(input("enter the previous unit"))
cu=int(input("enter the current unit"))
unit=cu-pu
print("unit consumed",unit)
if(unit>=1000):
   amount=unit*1100
   print("amount to be paid",amount)
elif(unit>=500):
   amt=unit*5
   print("amount to be paid",amount)
elif(unit>=100):
   amount=unit*2
   print("amount to be paid",amount)
else:
   print("amount to be paid,nill")
