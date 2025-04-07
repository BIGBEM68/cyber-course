def isPrime(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True

start= int(input('Enter range start '))
end=int(input('Enter a range end '))
for item in range(start,end):
    if isPrime(item):
        print(item)
