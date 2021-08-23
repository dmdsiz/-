word1 = str(input())
word2 = str(input())
reverse1 = word1[::-1]
reverse2 = word2[::-1] # reverse1&2 are for suffix
empty_list1=[] # common part of prefix
empty_list2=[] # common part of suffix
count =0
if len(word1)>=len(word2):
    count+=1
    for i in range(len(word2)):
        if word1[0] == word2[0]:       # compare word1&2. If first letter of word are same,
            if word1[i] == word2[i]:   # add the letters into empty_list1
                empty_list1.append(i)  # until letter of word1&2 are different
            elif word1[i] != word2[i]:
                break
    for u in range(len(word2)-len(empty_list1)):
        if reverse1[0] == reverse2[0]:      # compare reverse1&2. If first letter of reversed word are same,
            if reverse1[u] == reverse2[u]:  # add the letters into the empty_list2
                empty_list2.append(u)       # until letter of reverse1&2 are different.
            elif reverse1[u] != reverse2[u]:
                break
if len(word1) < len(word2):
    count =0
    for i in range(len(word1)):
        if word1[0] == word2[0]:       # compare word1&2. If first letter of word are same,
            if word1[i] == word2[i]:   # add the letters into empty_list1
                empty_list1.append(i)  # until letter of word1&2 are different
            elif word1[i] != word2[i]:
                break
    for u in range(len(word1) - len(empty_list1)):
        if reverse1[0] == reverse2[0]:         # compare reverse1&2. If first letter of reversed word are same,
            if reverse1[u] == reverse2[u]:     # add the letters into the empty_list2
                empty_list2.append(u)          # until letter of reverse1&2 are different.
            elif reverse1[u] != reverse2[u]:
                break
if count >=1:
    print(' ' * len(empty_list1) + '┏' + word1[len(empty_list1):len(word1) - len(empty_list2)] + '┓')
    print(word1[:len(empty_list1)] + '┫' + ' ' * (len(word1) - len(empty_list1) - len(empty_list2)) + '┣' + word1[len(word1) - len(empty_list2):])
    print(' ' * (len(empty_list1)) + '┗' + word2[len(empty_list1):len(word2) - len(empty_list2)].center(len(word1) - len(empty_list1) - len(empty_list2), ' ') + '┛')
elif count == 0:
    print(' ' * len(empty_list1) + '┏' + word1[len(empty_list1):len(word1) - len(empty_list2)].center(len(word2) - len(empty_list1) - len(empty_list2), ' ') + '┓')
    print(word1[:len(empty_list1)] + '┫' + ' ' * (len(word2) - len(empty_list1) - len(empty_list2)) + '┣' + word1[len(word1) - len(empty_list2):])
    print(' ' * (len(empty_list1)) + '┗' + word2[len(empty_list1):len(word2) - len(empty_list2)] + '┛')