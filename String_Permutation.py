def permutation(arr, i, length):
    if length == i:
        print(toString(arr))
    j = i
    while j < length:
        swap(arr, i, j) # Find combination
        permutation(arr, i + 1, length)
        swap(arr, i, j) # Backtrack
        j += 1

def toString(arr):
    arr=str(arr)
    arr = str.replace(arr, ',','')
    arr = str.replace(arr, '[','')
    arr = str.replace(arr, ']','')
    arr = str.replace(arr, "'",'')
    arr = str.replace(arr, "'",'')
    arr = str.replace(arr, ' ','')
    return arr

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


if __name__ == '__main__':
    arr = list('pass')
    i = 0
    len = len(arr)
    permutation(arr, 0, len)
