import random

number = random.randint(0, 99)
print ("this is the guess the number game. can you guess the number the computer choose between 0 and 99 in 8 chances ?")
        
guess = input ("what is the number")
guess_num = int(guess)
num_guess = 1
while guess_num != number and num_guess != 8 :
    if guess_num > number:
        print ("your guess is too high")
    elif guess_num < number:
        print ("your guess is too low")
    guess = input ("what is the number")
    guess_num = int(guess)
    num_guess = num_guess + 1        
if guess_num != number or num_guess == 9:
    print ("you lose the number was", number)
elif guess_num == number and  num_guess != 8:
    print ("you win")




















