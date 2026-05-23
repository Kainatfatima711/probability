set1 = {'A', 'B' , 'C' , 'D' , 'E'}
set2 = {'D' , 'E' , 'V' , 'X' , 'Y' , 'Z'}

union = set1.intersection(set2)
finalfriendlist = list(union)

print("Total common guests to be invited in party are: " , len(finalfriendlist))
print("Common Guest List: " , finalfriendlist)