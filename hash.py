import hashlib
def hack(hash):
    for i in range(1000000):
        if hashlib.md5((f"{i:06d}").encode()).hexdigest()==hash:
            return i
        
hashed=input("Enter hashed value: ")
print(hack("hashed"))    