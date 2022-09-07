
import re                                                                             

String ="I am in bRoad  Road Roadway in "                                                              

Updated =re.sub(r'\bRoad\b','Testpress',String)                                         
print (Updated)                                                              

L1=[1,2,3,4,5]
L3={v:v for v in L1}

print(L3)

L2=dict(L1)
print(L2)

Phone_Pattern ='''Phone Number Pattern using 
  regular Expression
  
  232-123-1231
  2334-30-313123

  '''

pattern= re.compile(r'[0-9]{4,5}+?-[0-9]+?-[0-9]+')
matches =pattern.finditer(Phone_Pattern)
for match in matches : 
    print(match)


line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"