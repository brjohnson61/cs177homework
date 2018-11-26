import crypt

def checkPassword(user, password, salt, hash):
    e_pass = crypt.crypt(password, salt)
    if(str(e_pass) in str(hash)):
        with open("passwords.txt", "a8") as myFile:
            myFile.write("User: " + user + ", Password: " + password)
        return True
    else:
        return False

def passwordFind(maxPasswordLength, username, salt, guess, myhash):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=/?><.,~`"
    if(maxPasswordLength >=4):
        print(guess)
    for i in range(len(characters)):
        guess0 = guess + characters[i]
        #print(guess0)
        if(checkPassword(user, salt, guess0, myhash)):
            return True
        else:
            if(maxPasswordLength > 1):
                passwordFind(maxPasswordLength-1, username, salt, guess0, myhash)
                

def wordSearch(username, salt, myhash):
    with open("words.txt", 'r') as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    for item in data:
        checkPassword(username, salt, item, myhash)






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
        salts.append("aa") 

print(usernames)
print(salts)

for i in range(len(usernames)):
    user = usernames[i]
    salt = salts[i]
    myguess = ""
    myhash = hashes[i]
    minLength = 6

    #textfile search
    wordSearch(user, salt, myhash)

    #brute force
    while(minLength < 20):
        passwordFind(minLength, user, salt, myguess, myhash)
        minLength = minLength + 1

  