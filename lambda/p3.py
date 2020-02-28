#Use lambda functions when an anonymous function is required for a 
#short period of time.
def abc(n):
 return lambda a,b: a*n*b;
 
newfun= abc(4);

print(newfun(2,3));