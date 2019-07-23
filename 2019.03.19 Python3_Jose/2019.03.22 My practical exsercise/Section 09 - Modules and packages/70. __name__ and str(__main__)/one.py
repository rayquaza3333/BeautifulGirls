def one_func():
	print('one_func in one.py')
print("Hi! I am in one.py")
if __name__=="__main__":
	print('one.py is being run directly')
else:
	print("one.py is being run indirectly")
a=0
a+=1
print(a)