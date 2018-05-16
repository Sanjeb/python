
from time import sleep

c = int(input ("enter number of seconds in countdown "))
c = c + 1
h = 1
while (h != c):
    c = c - 1
    print (c)
    sleep (1)
print ("blast off !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
