a = [3,4,3,4,4,5,5,4]
def dfs(array, ret):
    for i in range(len(array)):
        ret += array[i]
        if i >0 and i < len(array) - 1:
            dfs(array[:i-1] + array[i+1:])
        elif i == 0:
            dfs(array[i + 1:])
        elif i == len(array) - 1:
            dfs(array[:i-1])
        if