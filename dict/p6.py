pdict={"name":"harshit",
"email":"p@gmail.com",
"Mobile":"7876567876"
};
pdict= dict("name":"harshit","email":"p@gmail.com","Mobile":"7876567876");
for x,y in pdict.items():
 print(x,'=>',y);
 #To determine if a specified key is present in a dictionary use the in keyword:
#if "email" in pdict:
 #print("yes");
pdict.pop("email");
print(pdict);
#************
#del and pop is same in dictniory
#************
#pdict.clear();
mydict= dict(pdict);
print(mydict);