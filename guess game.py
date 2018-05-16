high = 100
low = -100
status = "low"
base_guess = 0
while (status == "high" or status == "low"):
    if status == "high" or status == "low":
         base_guess = base_guess + 1
    num = ((high + low)//2)
    print (num)
    status = input ("is the number high or low ")
    if status == "high":
        high = num
    elif status == "low":
        low = num
print ("thank you for playing !! you took", base_guess)
