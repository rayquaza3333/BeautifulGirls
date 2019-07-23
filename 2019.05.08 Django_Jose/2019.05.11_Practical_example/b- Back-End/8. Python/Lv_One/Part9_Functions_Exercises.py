#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) #→ True
# arrayCheck([1, 1, 2, 4, 1]) #→ False
# arrayCheck([1, 1, 2, 1, 2, 3])# → True

def arrayCheck(nums):
    # CODE GOES HERE
    position=0
    for x in nums:
        if position <= (len(nums) - 3):
            if nums[position] == (nums[position+1] -1)  == (nums[position+2] -2):
                print('True')
                return True
            position +=1
    else:
        print('False')
        return False

print('\n')
print('Problem 1')
print('\n')



arrayCheck([1, 1, 2, 3, 1])
arrayCheck([1, 1, 2, 4, 1])
arrayCheck([1, 1, 2, 1, 2, 3])


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  # CODE GOES HERE
  new_str = ""
  for x in range(len(str)):
      if (x % 2) == 0:
          new_str += str[x]
  print(new_str)
  return new_str

print('\n')
print('Problem 2')
print('\n')


stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')



#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#

# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    if len(a) <= len(b):
        a=a.lower()
        b = b.lower()
        print(b[:-len(a)-1:-1][::-1] == a)
        return b[:-len(a)-1:-1][::-1] == a
    else:
        c = a
        a = b
        b = a
        a=a.lower()
        b = b.lower()
        print(b[:-len(a)-1:-1][::-1] == a)
        return b[:-len(a)-1:-1][::-1] == a


print('\n')
print('Problem 3')
print('\n')


end_other('Hiabc', 'abc')
end_other('AbC', 'HiaBc')
end_other('abc', 'abXabc')

  # CODE GOES HERE

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  # CODE GOES HERE
  new_str =""
  for x in str:
      new_str += x*2
  print(new_str)
  return new_str



print('\n')
print('Problem 4')
print('\n')


doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3



def fix_teen(n):
  # CODE GOES HERE
  for x in [13,14,17,18,19]:
      if n ==x:
          return 0
  else:
      return n

def no_teen_sum(a, b, c):
    print(fix_teen(a) + fix_teen(b) + fix_teen(c))
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
  # CODE GOES HERE



print('/n')
print('Problem 5')
print('/n')


no_teen_sum(1, 2, 3)
no_teen_sum(2, 13, 1)
no_teen_sum(2, 1, 14)

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for x in nums:
        if (x % 2) ==0:
            count += 1
    print(count)
    return count
  # CODE GOES HERE
print('/n')
print('Problem 5')
print('/n')


count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])
