def pr(node):
    temp = node[0]
    while temp != None:
        print (temp.val)
        temp = temp.next
def get_size(node):
    n = 0
    while node!= None:
        node = node.next
        n += 1
    return n
def makeNode(n):
    if len(n) == 0:
        return None
    head = ListNode(n[0])
    cur = head
    for i in range (1, len(n)):
        cur.next = ListNode(n[i])
        cur = cur.next
    return head

def insert_merge(list, n):
    left = 0
    right = len(list) - 1
    mid = int((left + right)/2)
    if len(list) == 0:
        list.append(n)
        return
    while left<right:
        mid = int((left + right)/2)
        if list[mid][0]> n[0]:
            right = mid
        elif list[mid][0] < n[0]:
            left = mid
        elif list[mid][0] == n[0]:
            list[mid+1:] = list[mid:]
            list[mid] = n
            return
        if left + 1 == right:
            if list[right][0]< n[0]:
                left += 1

            elif list[left][0] < n[0]:
                right -= 1
    mid = int((right + left)/2)
    if list[mid][0] > n[0]:
        list[mid+1:] = list[mid:]
        list[mid] = n
    else:
        if len(list) > 1:
            list[mid+1:] = list[mid :]
            list[mid+1] = n
        else:
            list.append(n)
    return
def node_list_to_nodes(ret):
    for i in range(len(ret) - 1):
        ret[i].next = ret[i+1]
    return ret

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def find_min(nums)->int:
    smallest = nums[0]
    sidx = 0
    for i, n in enumerate(nums[1:]):
        if smallest > n:
            smallest = n
            sidx = i + 1
    return sidx

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        input = []
        ret = []
        sorted_array = []

        if len(lists) == 0:
            return None

        for i in lists:
            input.append(i)
        current_list = [None] * len(input)
        for i ,x in enumerate(input):
            current_list[i] = x

        whole_size = 0
        for i in current_list:
            whole_size += get_size(i)

         ### 초기화
        for i, l in enumerate(current_list):
            if l == None:
                continue
            sorted_array.append([l.val, i])
        sorted_array.sort()


        while len(sorted_array)!= 0:
            index_of_smallest = sorted_array[0][1]
            ret.append(current_list[index_of_smallest])
            #ret.append(sorted_array[0][0])
            sorted_array[:] =sorted_array[1:]
            if current_list[index_of_smallest].next != None:
                current_list[index_of_smallest] = current_list[index_of_smallest].next
                insert_merge(sorted_array, [current_list[index_of_smallest].val, index_of_smallest])

                #insert_merge current_list[[leaved_index].val, leaved_index]
        ##
        """
        for qwe in range(whole_size):

           
            mset = []
            for i in current_list:
                if i == None:
                    mset.append(999999)
                    continue
                mset.append(i.val)
            min_idx = find_min(mset)
            ret.append(current_list[min_idx])
            current_list[min_idx] = current_list[min_idx].next#일단 ret에 넣고 한번에 합치자
            """
        node_list_to_nodes(ret)
        #pr(ret)
        return ret[0]


sol = Solution()
l1 = makeNode([])
l2 = makeNode([1])
l3 = makeNode([])
lists = [l1, l2, l3]
sol.mergeKLists(lists)
#우선 1차완성인데
#TODO
"""
맨처음에 가장작은걸 찾는게아니라 정렬과 그에따른 인덱스 부여를 하고 나중에 삽입해서 정렬을 계속 하는 식으로

"""