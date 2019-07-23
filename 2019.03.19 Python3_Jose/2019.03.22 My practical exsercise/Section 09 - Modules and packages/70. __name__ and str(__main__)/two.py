a=7
from one import one_func
print("Hey, this line is in two.py")
one_func()
if __name__=="__main__":
	print('two.py is being run directly')
else:
	print("two.py is being run indirectly")
print(a)
globals()