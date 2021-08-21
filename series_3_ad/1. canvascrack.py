table_num = int(input())
value = int(input())
double = int(input())
ending = str(input())

sequence = 0
result = 0
# quadratic sequence difference and result

for i in range (1, table_num+1):        # input numbers from 1 to table_num
    sequence = value*i      # result of 1st difference and 2nd difference
    result = result + sequence      # previous value + 'sequence'
    if ending == 'stopped':
        if i == double * (i//double):       # i = 'double'*n , i is multiple of 'double'
            result = result * 2         # when i is number of 'double', it has to be doubled
            print('table #',i,' (x2): €',int(result),sep='')
        else:
            print('table #',i,': €',int(result),sep='')
    elif ending == 'lost':
        if i == table_num:
            print('table #', i, ': €', int(result/2 - sequence/2), sep='')      # result should be (previous result of final result)/2. It also can be (final result/2 - final sequence/2)
        elif i == double * (i // double):
            result = result * 2
            print('table #', i, ' (x2): €', int(result), sep='')
        elif i != double * (i // double):
            print('table #', i, ': €', int(result), sep='')