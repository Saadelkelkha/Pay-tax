a=int(input("type the age"))
b=str(input("type sex"))
if a>20 and b =="male" :
    print("pay tax")
elif a>=18 and a<=35 and b=="female" :
    print("pay tax")
else :
    print("do not pay tax")