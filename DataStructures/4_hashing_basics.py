lst1 = [1,2,3,5]
lst2 = [1,1,2,2,3,3,3,5]

def funct(l1, l2):
    l3 = []
    for val in l1:
        var = 0
        for j in range(len(l2)):
            if l2[j] == val:
                var += 1
        l3.append([val,var])
    return l3

print(funct(lst1, lst2))