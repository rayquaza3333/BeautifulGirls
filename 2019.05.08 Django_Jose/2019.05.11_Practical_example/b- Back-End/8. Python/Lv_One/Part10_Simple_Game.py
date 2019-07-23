import random
while True:
    a = random.randint(100,999)
    if a//100 != (a % 100)//10 !=a % 10 :
        break

digits=[a//100,(a % 100)//10,a % 10]
print(a)
print(digits)

print("""Hello, welcome to this guessing game
Your mission is to guess a 3 digits number which doesn't have any repeated digit inside.
We will return Match for each Match Item, close for correct value but wrong position item
""")


while True:
    b=int(input("Now, please give your first guess:"))
    while not( b <=999 and b >=100 and ( b//100 != (b % 100)//10 !=b % 10)):
        b=int(input("Your number is not under our rules, please give your first guess:"))
    if a//100 == b//100:
        print("Match!")
    elif b//100 in digits:
        print('Close!')
    if (a % 100)//10 == (b % 100)//10:
        print("Match!")
    elif (b % 100)//10 in digits:
        print('Close!')
    if a % 10 == b % 10:
        print("Match!")
    elif b % 10 in digits:
        print('Close!')
    if a//100 == b//100 and (a % 100)//10 == (b % 100)//10 and a % 10 == b % 10:
        print(f"Congratulation,  you have the correct guess. Our code is {a}")
        break












###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
# import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
#
# # Another hint:
# guess = input("What is your guess? ")
# print(guess)
#
# # Think about how you will compare the input to the random number, what format
# # should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
