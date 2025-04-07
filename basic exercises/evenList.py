def evens(list):
    temp=[]
    for item in list:
        if item%2==0:
            temp.append(item)
    return temp
original_list=[1 , 4 , 5 , 7 , 8 , 10 , 13]
print(evens(original_list))
    