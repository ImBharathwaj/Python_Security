import random
from unittest.result import STDERR_LINE


def permute(strList, permute_list):
    # hash_key = '3639EFCD08ABB273B1619E82E78C29A7DF02C1051B1820E99FC395DCAA3326B8'
    # hash_len = len(hash_key)
    # hInList = hash_len // 5
    # rand_len = 5
    str_lst = strList
    per_list = permute_list
    str_len = len(str_lst)
    test = []
    for i in range(5):
        temp = str_lst[i][i]
        print(temp)
        # test[i] = temp[per_list[i]]
    # print(test)

    

def splitIt(str1):
    str1 = str.replace(str1, ' ', '')
    strLen = len(str1) - 1
    inListLen = strLen // 5
    n = 0
    lst = []
    for i in range(inListLen):
        lst.append(list(str1[n:n + 5]))
        n += 5
    return lst


def dif_rand():
    lst = []
    length = 5
    while True:
        ran = random.randint(0, 5)
        if ran not in lst:
            lst.append(ran)
        if len(lst) == 5:
            break
    return lst


if __name__ == '__main__':
    per_list = dif_rand()
    str_list = splitIt('So if your girlfriend/boyfriend deletes all the pictures you have of your ex, for example, the hash of the folder will change. That way, youll know somethings wrong without checking each picture.')
    permute(str_list, per_list)
