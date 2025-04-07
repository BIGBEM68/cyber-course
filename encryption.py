import requests
def encrypt_file(file):
    key=5
    with open(file,"rb") as f_in,open("encrypted.png","wb") as f_encrypted:
        data=f_in.read()
        encrypted_data=bytes([b^key for b in data])
        f_encrypted.write(encrypted_data)
def decrypt_file(file,key):
    with open(file,"rb") as f_encrypted, open("original.png","wb") as f_original:
        encrypted_data=f_encrypted.read()
        original_data=bytes([b^key for b in encrypted_data])
        f_original.write(original_data)



image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuUT1amMza1Xgx9B27TpyVjsam11pat5RaQA&s"
response= requests.get(image_url)
file=open("image.png","wb")
file.write(response.content)
encrypt_file("image.png")
decrypt_file("encrypted.png",5)


    