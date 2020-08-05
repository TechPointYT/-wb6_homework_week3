def isValidAnagram(s,t):
    s = [ord(char) for char in s]
    t = [ord(char) for char in t]
    print(s)
    print(t)
    quickSort(s, 0, len(s) - 1)
    quickSort(t, 0, len(t) - 1)
    print(s)
    print(t)
    for i,j in zip(s,t):
        if i != j:
            return False
    return True

def quickSort(arr, s, e):
    #print(arr)
    if s >= e:
        return
    parIndex = partition(arr, s, e)
    quickSort(arr, s, parIndex - 1)
    quickSort(arr, parIndex + 1, e)
    
def partition(arr,s, e):
    pivot = arr[e]
    parIndex = s
    for i in range(s, e ):
        if arr[i] <= pivot:
            temp = arr[i]
            arr[i] = arr[parIndex]
            arr[parIndex] = temp
            parIndex += 1 
    temp = arr[parIndex]
    arr[parIndex] = arr[e]
    arr[e] = temp
    return parIndex

print(isValidAnagram("anagram", "nagaram"))
