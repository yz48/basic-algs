__author__ = 'yz48'

# bubble sort

def bubble_sort(array):
    for i in range(len(array)):
        f = 0
        for j in range(1,len(array)-i):
            if array[j-1] > array[j]:
                f = 1
                array[j-1], array[j] = array[j], array[j-1]
        if f == 0:
            break
    return array

# insertion sort

def insertion_sort(ary):
    n = len(ary)
    for i in range(1,n):

        temp = ary[i]
        index = i
        for j in range(i-1,-1,-1):
            if ary[j] > temp :
                ary[j+1] = ary[j]
                index = j
            else:
                break
        ary[index] = temp

    return ary



# binary insertion sort
def binary_insertion_sort(ary):
    n = len(ary)
    for i in range(1,n):
        temp = ary[i]
        left = 0
        right = i-1
        while left <= right:
            mid = (left+right)/2
            if ary[mid] > temp:
                right = mid-1
            else:
                left = mid+1
        ary[left+1:i+1] = ary[left:i1]
        ary[left] = temp
    return ary


# selection sort

def selection_sort(ary):
    n = len(ary)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if ary[min] > ary[j]:
                min = j
        ary[min],ary[i] = ary[i],ary[min]
    return ary

# merge sort


# quick sort
def quick_sort(ary):
    return qsort(ary,0,len(ary)-1)


def qsort(ary, left, right):
    if left >= right:
        return ary
    key = ary[left]
    lp = left
    rp = right
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1

        ary[lp], ary[rp] = ary[rp], ary[lp]
    ary[lp], ary[left] = ary[left], ary[lp]

    qsort(ary,left,lp-1)
    qsort(ary,lp+1,right)
    return ary

# merge sort bottom up
def merge_sort(lst):
    if not lst:
        return []
    lists = [[x] for x in lst]
    while len(lists) > 1:
        lists = merge_lists(lists)
    return lists[0]

def merge_lists(lists):
    result = []
    for i in range(0, len(lists) // 2):
        result.append(merge2(lists[i*2], lists[i*2 + 1]))
    if len(lists) % 2:
        result.append(lists[-1])
    return result

def merge2(xs, ys):
    i = 0
    j = 0
    result = []
    while i < len(xs) and j < len(ys):
        x = xs[i]
        y = ys[j]
        if x > y:
            result.append(y)
            j += 1
        else:
            result.append(x)
            i += 1
    result.extend(xs[i:])
    result.extend(ys[j:])
    return result

# merge sort top down
def merge_sort2(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)
    left = merge_sort2(ary[:num])
    right = merge_sort2(ary[num:])
    return merge(left,right)

def merge(left,right):
    l,r = 0,0
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


# heap sort
def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)
    for start in range(first,-1,-1) :
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary


def max_heapify(ary,start,end):
    root = start
    child = 2*root+1
    while child <= end:
        if child+1 <= end and ary[child] < ary[child+1]:
            child += 1
        if ary[root] < ary[child]:
            ary[child], ary[root] = ary[root], ary[child]
            root = child
            child = 2*root+1
        else:
            break



l = [5,2,1,3,-1,4,5]
print heap_sort(l)
