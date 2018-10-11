import urllib.request

URL1 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher1.txt"
URL2 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher2.txt"
URL3 = "http://www.cs.ucsb.edu/~tessaro/cs177/hw/cipher3.txt"

URLs = {URL1:cipherText1, URL2:cipherText2, URL3:cipherText3}
for entry in URLs:
    data = urllib.request.urlopen(entry)
    for line in data:
        print(line)

cipherText1= ""
cipherText2= ""
cipherText3= ""

def shiftDecode(text):


