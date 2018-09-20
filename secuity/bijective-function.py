
def all_equal(arr, value):
    n = len(arr)
    passes = 0
    for i in range(n - 1):
        if arr[i] != arr[i+1]:
            return False
        elif arr[i] == value:
            passes = 1
        else:
            passes = 0
            return False
#         till now, all n-1 elements are equal to value..
# checking for the last element only...
    if arr[n-1] == value and passes == 1:
        return True


def is_bijective(x, y):
    n = len(x)
    passes = []
#     checking for one-one nature...
    for i in range(n):
        curr = y[i]
        times = 0
        for chk in range(n):
            if y[chk] == curr:
                times = times + 1
        if times > 1:
            return "NO"
    passes.append(True)

#     checking for onto nature...
    if len(x) == len(y):
        passes.append(True)
    
    res = all_equal(passes, True)
    if res == True:
        return "YES"
    else:
        return "NO"


def main():
    n = abs(int(input()))
    X, Y = [], []
    
    for i in range(1, n+1):
        X.append(i)
    
    Y = input().split()

    if len(Y) < n:
        print('Too few values as images. Function cannot be defined.')
        exit()
    
    result = is_bijective(X, Y)
    print(result)


if __name__ == '__main__':
    main()
