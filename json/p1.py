#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.
#JSON an ideal data-interchange language.
import json

x= '{"name":"harshit","age":28,"email":"h@gmail.com"}'

y = json.loads(x);

print(y["age"]);