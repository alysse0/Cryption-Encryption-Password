import base64
import json


#getting password and xor_key from json 
def parse():
    password = ""
    xor_key = ""
    with open("passwords.json") as json_data:
        data = json.loads(json_data.read()) 
        password = data["pw"]
        xor_key = data["xor_key"]
    return password, xor_key
pw, xor_key = parse()


#initializing exclusive or gate.
def x0r(password, xor_key):
    j = 0
    encrypted = ""
    
    for i in range(0, len(password)):
        encrypted += chr(ord(password[i]) ^ ord(xor_key[j]))
        j += 1
        if j == len(xor_key):  
            j = 0
    return encrypted


crypted = base64.b64encode(x0r(pw, xor_key).encode()).decode() #decoding in order to get the result without b'name'.
print("crypted password: " , crypted)

#trying to get the original password.
def x0r_otherwise(password_crypted, xor_key):
    j = 0
    decrypted = ""

    #data comes as bytes. change it to str.
    if type(password_crypted) == bytes:
        password_crypted = password_crypted.decode()
    for i in range(0, len(password_crypted)):
        decrypted += chr(ord(password_crypted[i]) ^ ord(xor_key[j])); 
        j += 1
        if j == len(xor_key):  
            j = 0
    return decrypted


decrypted = base64.b64decode(crypted).decode()

original = (x0r_otherwise(decrypted, xor_key))
print("decrypted(original) password: " , original)