q = []
nums = [5,1,9,8,452,1,3,51,5,516]

def sort(n):
    if not q:
        q.append(n)
        return
    if len(q) == 1:

    l = 0
    r = len(q)
    while l<r:
        m = (l + r)//2
        if