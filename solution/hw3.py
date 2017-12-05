#Skeleton file for HW3 - Winter 2017-2018 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#The following import is required for Q3 and for Q6
import random


############
# QUESTION 2
############

# a
def find_root1(f):
    n = 1
    if (f(n+1) > f(n) > 0) or (f(n+1) < f(n) < 0):  #Positive and ascending or negetive and descending == no root
        return None
    while f(n) != 0:  #Start checking linear function values
        n += 1
    return n  #Return root

# b
def find_root_range(f, a, b):
    left = int(a) + (int(a) != a)  #Ceiling function of a (without math module)
    right = int(b)  #Floor of b
    if f(left) == 0:  #Check if root at borders
        return left
    elif f(right) == 0:
        return right
    n = int((left + right) / 2)  #Start checking from middle of borders
    while f(n) != 0:
        if f(n) > 0:  #Function positive
            if n == int((left + n) / 2):  #If root cannot be found (left border and middle collison)
                return None
            right = n  #Move right border to current middle (because positive)
            n = int((left + n) / 2)  #Move n to middle of left border and prev middle
        else:
            if n == int((right + n) / 2):  #If root cannot be found (right border and middle collison)
                return None
            left = n  #Move left border to current middle (because negative)
            n = int((n + right) / 2)  #Move n to middle of right border and prev middle
    return n

# c
def find_root2(f):
    a = b = 2  #Start with equal borders (powers of 2) = 2^1
    while f(b) < 0 or f(a) > 0:  #Right border is negative or left border is positive (need root!)
        if f(a) > 0 and f(b) > 0:  #Both borders positive
            a = a * -a  #Make left border minus
        else:
            a = b  #Left border is right border (prevent unneeded checking)
            b = b * b  #b = b^2
    return find_root_range(f, a, b)  #Found left border that is negative and right positive (implement find_root_range!)


############
# QUESTION 3
############

# a
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def selection_sort(lst):
    ''' sort lst (in-place) '''
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i+1,n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None

def generate_sorted_blocks(lst, k):
    new_l = []  #list to return
    for i in range(len(lst) // k + (len(lst) % k > 0)):  #Ceiling function for n/k iterations
        if k * (i + 1) <= len(lst):  #Didn't reach end
            tmp = [lst[x] for x in range(i * k, k * (i + 1))]  #Block list
        else:  #Reached end
            tmp = [lst[x] for x in range(i * k, len(lst))]  #Last block list
        selection_sort(tmp)  #Sort block
        new_l.append(tmp)  #Append block to returned list
    return new_l


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n+m)]

    a=0; b=0; c=0
    while  a<n  and  b<m: #more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a+=1
        else:
            C[c] = B[b]
            b+=1
        c+=1

    C[c:] = A[a:] + B[b:] #append remaining elements (one of those is empty)

    return C

# c
def merge_sorted_blocks(lst):
    newl = []  #Returned list
    while any(isinstance(x, list) for x in lst):  #While there are list elements in lst
        for i in range(int(len(lst)/2)):  #Iterate half of len(lst) times
            newl.append(merge(lst[i*2],lst[i*2+1]))  #Append 2 sorted blocks at a time to returned list
        if len(lst) % 2 == 0:  #Even number of lists to merge
            lst = newl  #Lst has half of previous elements and are sorted (copy from newl)
        else:  #Odd number of lists to merge
            newl.append(lst[len(lst)-1])  #Take last list (we merge in pairs), it will be merged in last iteration
            lst = newl  #Lst has half of previous elements and are sorted (copy from newl)
        newl = []  #Initialize newl
        if len(lst) == 1:  #Finished merging
            lst = lst[0]  #Get out of while loop
    return lst



def sort_by_block_merge(lst,k):
   return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 5
############

# a
def sort_triplets1(lst, k):
    newl = []  #Returned list
    tmp = [[[(a, b, c) for c in range(k)] for b in range(k)] for a in range(k)]  #3 dimension list of all tuples \
    #  with values from 0 to k according to their indices
    for i in range(k):  #Iterate through each list in 3 dim list
        for j in range(k):
            for m in range(k):
                if tmp[i][j][m] in lst:  #If tuple according to index is needed to be sorted
                    newl.append(tmp[i][j][m])  #Add to return list at end (we iterate from smallest to biggest)
    return newl

# c
def sort_triplets2(lst, k):
    new_l = lst.copy()  #Copy list to list to be sorted in-place
    for i in range(len(new_l)):  #Iterate through new_l tuples
        m_index = i  #Minimum index
        for j in range(i+1,len(new_l)):  #Iterate through all following tuples
            if (new_l[m_index][0] > new_l[j][0]) or \
               (new_l[m_index][0] == new_l[j][0] and new_l[m_index][1] > new_l[j][1]) or \
               (new_l[m_index][0] == new_l[j][0] and new_l[m_index][1] == new_l[j][1]
                and new_l[m_index][2] > new_l[j][2]):  #Conditions for smaller tuple
                m_index = j  #Found smaller tuple
        swap(new_l, i, m_index)  #I implemented selection - sort
    return new_l


############
# QUESTION 6
############

def diff_param(f,h=0.001):
    return (lambda x: (f(x+h)-f(x))/h)
 
 
def NR(func, deriv, epsilon=10**(-8), n=100, x0=None):
    if x0 is None:
        x0 = random.uniform(-100.,100.)
    x=x0; y=func(x)
    for i in range(n):
        if abs(y)<epsilon:
            #print (x,y,"convergence in",i, "iterations")
            return x
        elif abs(deriv(x))<epsilon:
            #print ("zero derivative, x0=",x0," i=",i, " xi=", x)
            return None
        else:
            #print(x,y)
            x = x- func(x)/deriv(x)
            y = func(x)
    #print("no convergence, x0=",x0," i=",i, " xi=", x)
    return None
 
# a
def equal(f1, f2):
    f = lambda x: f1(x) - f2(x)  #Function of difference between given functions, root will be intersection
    return NR(f, diff_param(f))  #Return root (intersection)

# c1
def source(f,y):
    source_f = lambda x: f(x) - y  #Function's root returns the source x for given y
    return NR(source_f, diff_param(source_f))  #Return root (source)
 
# c2
def inverse(f):
    return lambda x: source(f, x)  #Return source function


   
    
########
# Tester
########

def test():
    
    f1, f2 = lambda x : x - 8, lambda y : y - 5
    f3 = lambda x : 2*x + 1

    res1, res2 = find_root1(f1), find_root1(f2)
    if res1 == None or res2 == None or res1 != 8  or \
       res2 != 5:
        print("error in find_root1")
    res3 = find_root1(f3)
    if res3 != None:
        print("error in find_root1")
        
    res1, res2 = find_root_range(f1, 1, 9), find_root_range(f1, 1, 3)
    if res1 == None or res1 != 8 or res2 != None:
        print("error in find_root_range")
    res3 = find_root_range(f3, 100, 200)
    if res3 != None:
        print("error in find_root_range")
    
    res1, res2 = find_root2(f1), find_root2(f2)
    if res1 == None or res2 == None or res1 != 8  or \
       res2 != 5:
        print("error in find_root2")
    res3 = find_root2(f3)
    if res3 != None:
        print("error in find_root2")


    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if generate_sorted_blocks(lst, 2) != \
       [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 3) != \
       [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 10) != \
       [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if merge_sorted_blocks(block_lst1) != \
       [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if merge_sorted_blocks(block_lst2) != \
       [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")


    lst1 = [(30, 57, 52), (93, 63, 87), (83, 57, 68), (65, 90, 65), (69, 86, 6), (76, 18, 42), (82, 15, 51), (11, 39, 68)]
    if sort_triplets1(lst1, 100) \
       != [(11, 39, 68), (30, 57, 52), (65, 90, 65), (69, 86, 6), (76, 18, 42), (82, 15, 51), (83, 57, 68), (93, 63, 87)]:
        print("error in sort_triplets1")
        
    if sort_triplets2(lst1, 100) \
       != [(11, 39, 68), (30, 57, 52), (65, 90, 65), (69, 86, 6), (76, 18, 42), (82, 15, 51), (83, 57, 68), (93, 63, 87)]:
        print("error in sort_triplets2")
    
    f1, f2 = lambda x:4*x+1, lambda x:-x+6
    if equal(f1,f2) == None or abs(equal(f1, f2) - 1) > 10**-7:
        print("error in equal")
    
    lin = lambda x: x+3
    if source(lin,5) == None or abs(source(lin,5) - 2.0000000003798846) > 10**-7:
        print("error in source")
 
    if inverse(lin) == None or abs(inverse(lin)(5) - 1.9999999998674198) > 10**-7:
        print("error in inverse")
   
