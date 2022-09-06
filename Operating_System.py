Array =[1,23,5,6,7,8]

Length =len(Array)
print("Length of given Arrayy is ",Length)

print("Elemts in the Array are ;",Array)
print("Sum of these Elements are :" ,sum(Array))

'''Here we are multiplyong the array elemnts
with 2 '''

Array =[element*2 for element in Array]
Minimum =Array[0]
Maximum =Array[0]
print("Multiplying each elements for the array with 2: ",Array)

'''Finding minimum element in the array '''

for Min in Array[1:Length]:
    print(Min)
    if (Min<Minimum):
          Minimum =Min

print("Minimum element in the  array is : ",Minimum)

'''Finding minimum element in the array '''

for Max in Array[1:Length]:
    print(Min)
    if (Max>Maximum):
          Maximum =Max
    
print("Maximum element in the  array is : ",Maximum)