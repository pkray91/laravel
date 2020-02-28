f = open("abc.txt", "w")

f.write("I am added content");
#f.close();

f = open("abc.txt",'r');
print(f.read())
f.close();