import urllib.request

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

    for commonChar in frequency:
        min = 0
        minLetter = ""
        if(len(newMapping)<12):
            newMapping += commonChar
        else:
            if(min < frequency[commonChar]):
                #do something


    for c in frequency:
        print(c + ": " + str(frequency[c]))
    print(newMapping)

def setupURLs(URLs):
    for entry in URLs:
        data = urllib.request.urlopen(entry)
        cipherText = data.read().decode("utf-8")
        URLs[entry] = cipherText

setupURLs(URLs)

for url in URLs:
    print(URLs[url])

#Task 2a
shiftDecode(URLs[URL1])

#Task 2b
monoSub(URLs[URL2])
