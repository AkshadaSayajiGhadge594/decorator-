print("---------Decorators in Python------------");

print("Demonstration of Decorators");

def sub(a,b):
	print(a-b);
	

# SmartSub is our decorators which accepts function as argument
def SmartSub(fptr):

	# define inner function which Swap the number depends on its value
	def Inner(a,b):
		if a<b:
			a,b=b,a;
		
		#inner function calls our sub function & return
		return fptr(a,b);

	# return inner function
	return Inner;

sub=SmartSub(sub);

#Now we can call sub function which is decorated function
print("Substarction of 7 and 2 is :");
sub(7,2);

print("substraction of 2 and 7 is :");
sub(2,7);

#///////////////////////////////////////////////////////////////////////////////////////////
## Output:
##	---------Decorators in Python------------
##	Demonstration of Decorators
##	Substarction of 7 and 2 is :
#	5
##	substraction of 2 and 7 is :
##	5
##///////////////////////////////////////////////////////////////////////////////////////////
