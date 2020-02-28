f = open("abc.txt", "a")

f.write("I am added content");
#f.close();

f = open("abc.txt",'r');
print(f.read())
f.close();