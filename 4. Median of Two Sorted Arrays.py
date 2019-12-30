def left_left(nums1, standard):
    if standard <= nums1[0]:
        return 0
    elif standard > nums1[-1]:
        return len(nums1)

    left = 0
    right = len(nums1)-1
    #last_op = 0 # 0 = left    1 = right
    while(right - left >1):

        mid = int((left + right) / 2)# 한가운데거나 오른쪽에 하나 많게 남음
        if nums1[mid] >= standard:
            right = mid
            #last_op = 1
        else:
            left = mid
            #last_op = 0
    return left + 1

def rightMinusLeft(nums1, nums2, index):
    left = index +left_left(nums2, nums1[index])
    right = len(nums1) + len(nums2) - left - 1
    return right - left


nums1 = [0,0]
nums2 = [0,0]
# O(lon n + m)

if len(nums1)<len(nums2):
    nums1, nums2 = nums2, nums1
m = len(nums1)
n = len(nums2)
far_right = int((m + n + 1) / 2 - 1)
far_left = int((m - n + 1) / 2 - 1)
nums1 = nums1[far_left : far_right + 1 ]

ret = []
m = len(nums1)
is_even_number = False
if (m+n)%2 == 0:
    is_even_number = True
right = m - 1
left = 0
while right - left > 1 :
    mid = int((right + left)/ 2)# 가운데거나 오른쪽이 하나 많음
    rml = rightMinusLeft(nums1,nums2,mid)

    if rml < 0:#right - left < 0 즉 왼쪽이 더많으면 기준을 오른쪽으로
        right = mid
    elif rml > 0:
        left = mid
    elif rml == 0:
        #return nums1[mid]
        print(nums1[mid])

rml = rightMinusLeft(nums1, nums2, left)
if  -1<= rml <= 1:
    if not is_even_number:
        print(nums1[left])
    else:
        print(nums1[left])  # add return
        ret.append(nums1[left])


rml = rightMinusLeft(nums1, nums2, right)
if  -1<= rml <= 1:
    if not is_even_number:
        print(nums1[right])
    else:
        print(nums1[right])  # add return
        ret.append(nums1[right])


if is_even_number:
    if len(ret)<2:
        pass#goto phase 2
    else:
        print((ret[0] + ret[1])/2)

else:
    if len(ret) == 1:
        print(ret[0])# return ret[0]
    else:
        pass#goto phase 2


exleft = left
exright = right
#nums2 시작
left = left_left(nums2, nums1[left])
right = left_left(nums2, nums1[right]) - 1

if rightMinusLeft(nums1, nums2, exleft) < 0:
    left = n-2
    ret.append(nums2[n-1])
    print(ret)
if rightMinusLeft(nums1, nums2, exright) > 0:
    right = 2
    ret.append(nums2[0])
    print(ret)

while right - left > 1 :
    mid = int((right + left)/ 2)
    rml = rightMinusLeft(nums2, nums1, mid)

    if rml < 0:  # right - left < 0 즉 왼쪽이 더많으면 기준을 오른쪽으로
        right = mid
    elif rml > 0:
        left = mid
    elif rml == 0:
        # return nums1[mid]
        print(nums1[mid])

rml = rightMinusLeft(nums2, nums1, left)
if -1 <= rml <= 1:
    ret.append(nums2[left])
rml = rightMinusLeft(nums2, nums1, right)
if -1 <= rml <= 1:
    ret.append(nums2[right])
if is_even_number:
    print((ret[0] + ret[1] )/ 2)
else:
    print(ret[0])

"""
case1 n = 홀 m = 짝
target in n

n에서 가운데값 구한다
m에서 n의 위치를 구한다.  m1<mid_n<m2
왼쪽남은게 오른쪽 보다 크다면 왼쪽으로 이동
아니면 ㅗㅇ른쪽이동
같다면 n = target
case2
target in m

"""
