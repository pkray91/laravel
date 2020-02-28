import mymodule

a= mymodule.rec['name']
b= mymodule.rec['age']
change= mymodule.rec['age']=30
c= mymodule.rec['mobile']
d= mymodule.rec['Address']='Noida'
print(a,b,c,d,change)

import platform

print(platform.system())

from mymodule import rec

print(rec['age'])