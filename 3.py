
#xplanation : Each element of ‘gfg’ is repeated 3, 5 and 2 times to output different strings. 

list1 = ["gfg", "is", "best"]

list4 = []

list2 = [3,5,2]

list3 = []

i = 0


m = 1
while m <= len(list1):
    j = 0
    str = ""
    a = list1[i]
    b = list2[j]


    for k in a:
        str1 = k * b
        str = str + str1
    list4.append(str)
    i = i + 1
    
    m = m + 1


i = 0
n = 1
while n <= len(list1):
    j = 1
    str = ""
    a = list1[i]
    b = list2[j]


    for k in a:
        str1 = k * b
        str = str + str1
    list4.append(str)
    i = i + 1
    
    n = n + 1

i = 0
s= 1
while s <= len(list1):
    j = 2
    str = ""
    a = list1[i]
    b = list2[j]


    for k in a:
        str1 = k * b
        str = str + str1
    list4.append(str)
    i = i + 1
    
    s = s + 1

print(list4)



