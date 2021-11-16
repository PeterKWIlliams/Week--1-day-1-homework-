

 iuser_num = input("pick a number between 1-20 ")
n = 8 
num = abs(n - int(user_num))
print(num)

if num == 0:
  print("WOW incredible omg")

elif num <= 20 and num >= 16: 
  print("so far away")

elif num <= 15  and num >= 11: 
  print("not too far away")

elif num <= 10  and num >= 6 :
  print("getting real close")
  
elif num <= 5  and num >=2 :
  print("on fire ")
elif num == 1 :
  print("as close as one can be")
else:
  print ("you havent chosen a valid value")