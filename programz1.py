Elements=[1,2,3,4,5,3,4,5,5,8,11,12,11,12]
Length =len(Elements)
Elements.sort()
print(Elements)
Count =0
ans =[]

Set =[*set(Elements)]
Length_Set=len(Set)

for i in range(0,Length_Set-1):
    if Set[i]+1==Set[i+1]:
      Count +=1
    else :
      ans.append(Count)
      Count=0
      continue

print(max(ans))