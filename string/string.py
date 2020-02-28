print("Hello python");
print('Hello python');
x = '''hdbvfvhbfvhbf'''
y = """mdnfbvnfbvdfnbvfvbfm"""
print(y)
print(x)
a='whO ARE you Man';
print(a);
print(a.upper());
print(a.lower());
print(len(a));
print(a[1]);
#sub string not including the given position.
print(a[4:8]); 
#The strip() method removes any whitespace from the beginning or the end:
b=" hello ";
print(b);
print(b.strip());
print(b.replace('h','l'));
#The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(' '));
print(a.split('a'));
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
age=36;
c='I am going home {}';
print(c.format(age));
quant=20;
age=28;
mobile=898767898;
txt='total men was {} and their age was {} and have only one mobile no is            {}';
print(txt.format(quant,age,mobile));
age=36;
c='I am going home {}';
print(c.format(age));
quant=20;
age=28;
mobile=898767898;
txt='total men was {2} and their age was {0} and have only one mobile no is            {1}';
print(txt.format(quant,age,mobile));
#reverse the string.
rev= 'hello python'[::-1];
print(rev);