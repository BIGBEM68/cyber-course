test_list=[1 , 2 , 3 , 4 , 5]
isSortedUp=True
for i in range(len(test_list)-1):
    if test_list[i]>=test_list[i+1]:
        isSortedUp=False
        break
if isSortedUp:
    print('list sorted up')
else: 
    print('list not sorted up')