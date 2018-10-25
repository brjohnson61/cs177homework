import urllib.request
from Crypto.Cipher import AES
from Crypto import Random  

URL1 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher1.txt"
URL2 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher2.txt"
URL3 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher3.txt"
URLs = {URL1:"", URL2:"", URL3:""}

def shiftDecode(text):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(text)
    for i in range(26):
        newText = ""
        for letter in text:
            newLetter = alpha[(alpha.find(letter)+i)%26]
            newText += newLetter
        print(str(i) + " ")
        print(newText)

def monoSub(text):
    text = text.rstrip()
    text = text.upper()
    print(text)
    common = "ETAOINSHRDLU"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newMapping = ""
    frequency = {"A":0, "B":0,"C":0,"D":0,"E":0,
             "F":0,"G":0,"H":0,"I":0,"J":0,
             "K":0,"L":0,"M":0,"N":0,"O":0,
             "P":0,"Q":0,"R":0,"S":0,"T":0,
             "U":0,"V":0,"W":0,"X":0,"Y":0,
             "Z":0}
    for letter in text:
        frequency[letter] = frequency[letter] + 1
    
    
    max = -1
    maxLetter = ""
    descending = ""    
    for i in frequency:
        max = -1
        for commonChar in frequency:
            if(frequency[commonChar] > max and commonChar not in descending):
                max = frequency[commonChar]
                maxLetter = commonChar
        descending+=maxLetter

    min=0
    minLetter = ""
    for commonChar in frequency:
        if(len(newMapping)<12):
            print(newMapping)
            newMapping += commonChar
            if(frequency[commonChar] < min or len(newMapping)==1):
                min = frequency[commonChar]
                minLetter = commonChar
        elif(frequency[commonChar] > min):
            newMapping = newMapping.replace(minLetter, commonChar)
            min = frequency[commonChar];
            minLetter = commonChar
            for c in newMapping:
                if(frequency[c] < min):
                    min = frequency[c]
                    minLetter = c
        print(newMapping)
    moreFrequent=""
    lessFrequent=""
    
    for i in range(6):
        maxMore = 0
        maxLetterMore = ""
        for c in newMapping:
            if(frequency[c] > maxMore and c not in moreFrequent):
                maxMore = frequency[c]
                maxLetterMore = c;
        moreFrequent += maxLetterMore
    for i in range(6):
        maxLess = 0
        maxLetterLess = ""
        for c in newMapping:
            if(frequency[c] > maxLess and c not in moreFrequent and c not in lessFrequent):
                maxLess = frequency[c]
                maxLetterLess = c
        lessFrequent += maxLetterLess
      
    print("moreFrequent "+ moreFrequent)
    print("lessFrequent "+ lessFrequent)  

    for letter in moreFrequent:
        print(letter + " " + str(frequency[letter]))

    for letter in lessFrequent:
        print(letter + " " + str(frequency[letter]))

    
    moreCommon = ["etaoin","etaoni","etaion","etaino","etanoi","etanio",
                  "etoian","etoina","etoain","etoani","etonia","etonai"]
    
    lessCommon = ["shrdlu","shrdul","shrldu","shrlud","srhdlu","srhdul",
                  "srhldu","srhlud","hsrdlu","hsrdul","hsrldu","hsrlud"]

    
    ##Interactive Method

    output = text
    Frequent = descending
    i=0
    mapping = {"e":"G","t":"Q","a":"","o":"","i":"","n":"","h":"S","s":"","r":"","d":"","l":"","u":""}
    print("Frequent: "+Frequent)
    print(mapping)
    option = input("Enter a letter to replace the letter "+ Frequent[i] +" next or enter 'quit' to quit")
    while(option != "quit"):
        output = output.replace("Q","t")
        output = output.replace("G","e")
        output = output.replace("S","h")
        output = output.replace("H", "g")
        output = output.replace("W", "r")
        output = output.replace("M", "b")
        output = output.replace("Z", "u")   
        if(option == "reset"):
            output = text
            
            i=0
            for entry in mapping:
                mapping[entry] = ""
        else:
            print("Replacing "+Frequent[i]+" with "+option)
            mapping[option] = Frequent[i]
            output = output.replace(Frequent[i], option)
            outputclean = output
            for c in outputclean:
                if(c.isupper()):
                    outputclean = outputclean.replace("Q","t")
                    outputclean = outputclean.replace("G","e")
                    outputclean = outputclean.replace("S","h")
                    outputclean = outputclean.replace("H", "g")
                    outputclean = outputclean.replace("M", "b")
                    outputclean = outputclean.replace(c, "*")
                    
                    
            print("output: "+output)
            print("output clean: " + outputclean)
            i += 1
            print(mapping)
        option = input("Enter a letter to replace the letter "+ Frequent[i] +" next, enter 'quit' to quit, or enter 'reset' to start over")
        

    
    
    ##ORIGINAL METHOD

    #outputBoth = ""
    #for j in range(12):
    #    output = text
    #    #output = output.replace("S", "h")
    #    for i in range(6):
    #        output = output.replace(moreFrequent[i], moreCommon[j][i])
    #        #print("replacing "+moreFrequent[i]+" with "+moreCommon[j][i])
    #    for k in range(12):
    #        outputBoth = output
    #        for l in range(6):
    #            outputBoth = outputBoth.replace(lessFrequent[l], lessCommon[k][l])
    #            #print("replacing "+lessFrequent[l]+" with "+lessCommon[k][l])
    #        if("the" in outputBoth and "and" in outputBoth and "in" in outputBoth and "that" in outputBoth):
    #            print(moreFrequent+lessFrequent)
    #            print(moreCommon[j]+lessCommon[k])
    #            print(outputBoth)
    #            print("\n")








##BRUTE FORCE
    print("BRUTE FORCE")
    max = -1
    maxLetter = ""
    descending = ""
    print("Frequency")
    print(frequency)
    for i in frequency:
        max = -1
        for commonChar in frequency:
            if(frequency[commonChar] > max and commonChar not in descending):
                max = frequency[commonChar]
                maxLetter = commonChar
        descending+=maxLetter


    print(descending)
    for c in descending:
        print(c + " " + str(frequency[c]))

    output = text
    frequentLetters = "etaoinsrhldcumfpgwybvkxjqz"
    mapping = {"e":"","t":"","a":"","o":"","i":"","n":"","s":"","r":"","h":"","l":"","d":"","c":"","u":"","m":"","f":"","p":"","g":"","w":"","y":"","b":"","v":"","k":"","x":"","j":"","q":"","z":""}


    


def mapFunc(text, commonEng, commonText, index):
        output = text
        output = output.replace(commonText[index], commonEng)



def setupURLs(URLs):
    for entry in URLs:
        data = urllib.request.urlopen(entry)
        cipherText = data.read().decode("utf-8")
        URLs[entry] = cipherText

setupURLs(URLs)

for url in URLs:
    print(URLs[url])

def task4a():
   key = bytes.fromhex("10042018000000000000000000000000")
   iv = Random.new().read(16)
   AEScipher =  AES.new(key, AES.MODE_ECB, iv)
   message = iv + AEScipher.encrypt(key)
   output = message.hex()
   print(output)


#Task 2a
#shiftDecode(URLs[URL1])

#Task 2b
#monoSub(URLs[URL2])

#Task 4
#task4a()
