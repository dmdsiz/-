try:
    a = []
    while True:
        aa = input()
        if aa:
            a.append(aa)
        else:
            break
except:
    for i in range(2, len(a) - 1):
        if int(a[i]) - int(a[i - 1]) != int(a[0]):
            if int(int(a[i]) - int(a[i - 1])) >= 0:
                print(int(a[i - 1]), ' -> ', int(a[i]), ' (+', int(int(a[i]) - int(a[i - 1])), ')', sep='')
            else:
                print(int(a[i - 1]), ' -> ', int(a[i]), ' (', int(int(a[i]) - int(a[i - 1])), ')', sep='')