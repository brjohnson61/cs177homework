from math import gcd

def eulersTotient(target):
    count = 0
    for i in range(target):
        if(gcd(target, i+1) == 1):
            count = count + 1
    return count


print(eulersTotient(2214119))






