import re
String = "1abc Testpress"
x='''x

Ha HaHa Hisa

Ha

kar

Bala'''

phone='''
321-333-4356
213.456.1234
Karthik@gmail.com
'''
# Sentence="Welcome to Chennai"
# print(r'\tTab \t\t\tTab')
# print(String[1:4])
pattern = re.compile(r'[a-zA-Z0-9]+?@[a-zA-Z]+\.com')
matches =pattern.finditer(phone)
for match in matches : 
    print(match)



