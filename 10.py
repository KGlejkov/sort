import random
def sorted_(a):
    lenl = len(a)
    for i in range(0, lenl - 1):
        if(a[i] > a[i + 1]):
            return False
    return True

def random(a):
    lenl = len(a)
    for i in range(0, lenl):
        rnd = random.randint(0, lenl - 1)
        temp = a[i]
        a[i] = a[rnd]
        a[rnd] = temp
        
def bogosort(a):
    while(not(sorted_(a))):
        random_permutation(a)
mas = []
n = int(input("Длина массива:")) 
for i in range(0, n): 
    elt = int(input("arr[" + str(i + 1) + "] = "))   
    mas.append(elt)
bogosort(mas) 
print(mas)
