# Finding the roots of a function between a specified region

def f(x):
	return x**2-16



def find_root(a,b):
	c=(a+b)/2
	ans=f(c)

	num_iteration=0
	while ans !=0 and num_iteration<=1000:
		num_iteration += 1

		c=(a+b)/2
		ans=f(c)

		if ans>0: 
			b=c
		elif (ans<0):
			a=c
		else:
			return c

lower=-5
upper=5
print(find_root(lower, upper))