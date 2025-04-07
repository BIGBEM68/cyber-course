#casting
num_str='123'
num_int=int(num_str)
num_int+=10
print(num_int)
#calc
operator=input("select an operator: *,/,+,-")
if operator == '*' or operator == '/' or operator== '+' or operator== '-':
    num1=input("type a number")
    num2=input("type a number")
    if operator=='/' and num2=='0':
        print("can't divide by zero")
    else: 
        result=num1+operator+num2
        print(eval(result))
else:  
    print('not an operator')