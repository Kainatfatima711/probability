set1 = {'A', 'B' , 'C' , 'D' , 'E'}
set2 = {'D' , 'E' , 'V' , 'X' , 'Y' , 'Z'}

union = set1.union(set2)

finalfriendlist = list(union)

print("Total guests to be invited in party are: " , len(finalfriendlist))
print("Guest List: " , finalfriendlist)