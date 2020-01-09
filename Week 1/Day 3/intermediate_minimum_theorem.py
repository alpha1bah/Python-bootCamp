# Finding the roots of a function between a specified region

def f(x):
	return 2*x+1



def find_root(a,b):
	c=(a+b)/2
	ans=f(c)

	while ans !=0:

		c=(a+b)/2
		ans=f(c)

		if ans>0: 
			b=c
		elif (ans<0):
			a=c
		else:
			return c

lower=-5
upper=0
print(find_root(lower, upper))