print("guru's supermarket")
print("no,44 street,pondicherry")
print("--------------")
print("bill recipt")
print("--------------")
str1=input("enter the serial no")
str2=input("enter the particular")
str3=int(input("enter the rate"))
str4=int(input("enter the quality"))
total=str3*str4
print("total amt:",total)
gst=total*10/100
print("gst 10 percentage:",gst)
paid=total+gst
print("amt to be paid",total)
         
