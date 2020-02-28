import re

txt='The rain 67556 in spain';

#x= re.search('^The',txt);
'''
if(x):
 print("yes we have match");
else:
 print("no match found");
'''
#x=re.findall("[a-p]",txt);
#x=re.findall("\d",txt);
#x=re.findall("sp..n",txt);
#x=re.findall("spain$",txt);
'''if(x):
 print('yes');
else:
 print('no');
print(x);'''

#x=re.findall("inx*",txt);
#x=re.findall("inx+",txt);
#x=re.findall("\D",txt);
#x=re.findall("\s",txt);
#x=re.findall("\S",txt);
#x=re.findall("\w",txt);
#x=re.findall("\W",txt);
x=re.findall("[apn]",txt);
x=re.findall("[a-z]",txt);
x=re.findall("[^apn]",txt);
x=re.findall("[0-5][0-7]",txt);
x=re.findall("ai",txt);
x=re.split("\s",txt);
x=re.sub("\s","tempo",txt);
x=re.sub("\s","2",txt,2);
print(x);