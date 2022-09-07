'''Concatenate 2
Strings with + Operation'''

String1="Welcome to "
String2="TestPress"
S3=String1 + String2
print(S3)
print(len(S3))
print(S3[15])

UserName ='Karthik'
Mark = "100"
"{0} is  your name and {1} is you marks ".format(UserName,Mark)

Query = " UserName = Karthik&Age =25&Job=Software_Developer"
List =Query.split('&')
print(List)

Sub_List = [v.split('=',1) for v in List]
print(Sub_List)

Dict = dict(Sub_List)
print(Dict)

Slicing ="We are gona Slice you into pieces "

print(Slicing[4:])
print(Slicing[4:-4])
print(Slicing[:-1])


Byte =b'abcd\x65'
print((Byte))
print(Byte[-1])

Encoding = "Lets Secure it"
Secured =Encoding.encode('utf-8')
print(Secured)