import crypt

def checkPassword(user, password, salt, hash):
    e_pass = crypt.crypt(password, salt)
    if(e_pass in hash):
        print("User: " + user + ", Password: " + password)
        return True
    else:
        return False

def passwordFind(maxPasswordLength, username, salt, guess, myhash):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=/?><.,~`"
    for i in range(len(characters)):
        guess0 = guess + characters[i]
        #print(guess0)
        if(checkPassword(user, salt, guess0, myhash)):
            return True
        else:
            if(maxPasswordLength > 1):
                passwordFind(maxPasswordLength-1, username, salt, guess0, myhash)
                

with open('shadow', 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]


usernames = []
salts = []
hashes = [] 

for hash in data:
    
    usernames.append(hash.split(':')[0])
    hashes.append(hash.split(':')[1])
    if("$" in hash):
        salt = "$" + hash.split("$")[1] + "$" + hash.split("$")[2] + "$"
        salts.append(salt)
    else:
        salts.append("") 

print(usernames)
print(salts)

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=/?><.,~`"

for i in range(len(usernames)):
    user = usernames[i]
    salt = salts[i]
    myguess = ""
    myhash = hashes[i]
    maxLength = 20


    passwordFind(maxLength, user, salt, myguess, myhash)

    # for i in range(len(characters)):
        
    #     guess0 = guess + characters[i]
    #     if(checkPassword(user, salt, guess0, hash)):
    #         break
    #     for i in range(len(characters)):
    #         guess1 = guess0 + characters[i]
    #         if(checkPassword(user, salt, guess1, hash)):
    #             break
    #         for i in range(len(characters)):
    #             guess2 = guess1 + characters[i]
    #             if(checkPassword(user, salt, guess0, hash)):
    #                 break
                
