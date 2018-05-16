from time import sleep

n = int(input ("enter the number of integers printed in the fibonacci sequence "))
n = n - 1
num_1 = 1
num_2 = 1
value = 1
h = 0
print (1)
while (h != n):
    h = h + 1
    value = num_1 + num_2 
    num_1 = num_2
    num_2 = value
    print (num_1)
    sleep (1)
