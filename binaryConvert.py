def to_binary(num,size):
    binary_num_list=[]
    for i in range(0,size):
        binary_num_list.append(0)
    for i in range(len(binary_num_list)-1,-1,-1):
        if num>= pow(2,i):
            binary_num_list[len(binary_num_list)-1-i]=1
            num-=pow(2,i)
    binary_num=""
    for value in range(0,len(binary_num_list)):
        binary_num+=str(binary_num_list.pop(0))
    return binary_num         

def to_negative(binary_num):
    negative_num=""
    for char in binary_num:
        if char=='1':
            negative_num+='0'
        else:
            negative_num+='1'
    return negative_num


def plus_one(binary_num:str):
    list=[]
    for char in binary_num:
        list.append(int(char))
    list=list[::-1]
    list[0]+=1
    if list[0]==2:
        for item in list:
            if list[item]==2:
                if item==len(list)-1:
                    list[item]-=1
                    list.insert(len(list))
                list[item]-=1
                list[item+1]+=1
    list=list[::-1]
    binary_num=""
    for value in list:
        binary_num+=str(value)
    
    return binary_num

def complete_to_two(num,size):
    result=to_binary(num,size)
    result=to_negative(result)
    result=plus_one(result)
    return result

number=3
print(complete_to_two(3,8))
    





  
        

    