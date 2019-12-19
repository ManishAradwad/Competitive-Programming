# Iterative Implementation

def BinarySearch(arr,l,r,x):
    while r >= l:
        mid = l + (r-1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    else:
        return -1

#Testing

array = [ 2, 3, 4, 10, 40 ] 
x = 4

result = BinarySearch(array,0,len(array)-1,x)
if result != -1:
    print(result)
else:
    print(-1)