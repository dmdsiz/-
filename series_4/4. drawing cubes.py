width = int(input())
height = int(input())
depth = int(input())

if  height > depth:
    for i in range(1,depth+1):
        print(' '*(depth+1-i),end='')
        print(':'*(width-1)+'/'+'+'*(i-1))
    for i in range(1,height-depth+1):
        print('#'*width + '+'*depth)
    for i in range(1,depth+1):
        print('#'*width + '+'*(depth-i))
else:
    for i in range(1,height+1):
        print(' '*(depth+1-i),end='')
        print(':'*(width-1)+'/'+'+'*(i-1))
    for i in range(height+1,depth+1):
        print(' '*(depth+1-i),end='')
        print(':'*(width-1)+'/'+'+'*(height-1))
    for i in range(1,height+1):
        print('#'*width + '+'*(height-i))