def geo2dec(geohash):
    geohash =geohash [::-1]  # reverse the geohash
    list = []
    count = -1
    sum = 0
    for i in geohash.lower():     # use the ascii code to change letters to numbers
        if 47 < ord(i) < 58:
            list.append(ord(i)-48)
        if 97 < ord(i) < 105:
            list.append(ord(i)-88)
        if 105 < ord(i) < 108:
            list.append(ord(i)-89)
        if 108 < ord(i) < 111:
            list.append(ord(i)-90)
        if 111 < ord(i) < 123:
            list.append(ord(i)-91)
    for j in list:
        count +=1               #count is for power
        sum += j * (32**count)
    return sum
def geo2bin(geohash):
    a=bin(geo2dec(geohash))[2:]
    if len(a) < 20 :                   #length of binary is at least 20 and it is multiple of 5
        a = (20 - len(a)) * '0' + a
    if len(a) % 5 !=0:
        a = (((len(a) // 5) + 1) * 5 - len(a)) * '0' + a
    return a
def unravel(geohash):
    a=''
    b=''
    for i in range(len(geohash)):
        if i % 2 == 0:
            a += geohash[i]
        else:
            b += geohash[i]
    return a,b
def bin2coord(geohash,degree1,degree2):
    for i in geohash:                     # find latitude and longitude if i is 0 mid is (degree1+degree2)/2 and mid change into degree2
        if i == '0':                      # if i is 1 mid is (degree1+degree2)/2 and mid change into degree1
            mid = (degree1+degree2)/2
            degree2 = mid
        if i == '1':
            mid = (degree1+degree2)/2
            degree1 = mid
    if geohash[-1] == '0':
        return degree1, mid
    else:
        return  mid, degree2
def geo2coord(geohash):
    answer = geo2bin(geohash)
    binary1,binary2 = unravel(answer)
    longitude1,longitude2 = bin2coord(binary1,-180, 180)
    latitude1,latitude2 = bin2coord(binary2, -90, 90)
    return (longitude1+longitude2)/2, (latitude1+latitude2)/2