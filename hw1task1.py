import urllib.request

URL1 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher1.txt"
URL2 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher2.txt"
URL3 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher3.txt"
URLs = {URL1:"", URL2:"", URL3:""}

def shiftDecode(text):
    text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(text)
    for i in range(26):
        newText = ""
        for letter in text:
            newLetter = alpha[(alpha.find(letter)+i)%26]
            newText += newLetter
        print(str(i) + " ")
        print(newText)

for entry in URLs:
    data = urllib.request.urlopen(entry)
    cipherText = data.read().decode("utf-8")
    URLs[entry] = cipherText

for url in URLs:
    print(URLs[url])





shiftDecode(URLs[URL1])