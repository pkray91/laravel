#Arithmetic operators
#Assignment operators
#Comparison operators(==,|=,>,<,>=,<=)
#Logical operators(and or not)
#Identity operators(is  is not);
#Membership operators(in  not in)
#Bitwise operators(&,|,^,>>,<<);
#relational(>,<);true,false.
#uniary(-);
#============================================================
#+,-,*,/,%,**(exponential),//(floor).
a=2;
b=5;
print(a**5);
print(b/a);
print(b//a);18001033300
#============================================================
#Assignment operators.
#=,+=,-=,*=,/=,%=,**=,//=,&=,|=,^=,>>=,<<=.
a=a&4;
print(a);
print(a<b);#true
print(a>b);#false
#============================================================
#Logical operators
x = 5;

print(x > 3 and x < 10);
#=============================================================
##Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": 
#this comparison returns True because x is equal to y