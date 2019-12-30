def differ (a:int, b:int)->int:
    if a>b:
        return a-b
    else:
        return b-a

nums = [0,2,1,-3]

target = 1
difference = 9999999
min_def = 99999999
nums.sort()
n = len(nums)
for mid in range(1, n - 1):

    left = 0
    right = n - 1

#################################### 기본틀에 추가한 부분 다음#까지 ... 
    biggest_this_turn = nums[mid] + nums[mid - 1] + nums[n-1]
    smallest_this_trun = nums[mid] + nums[mid + 1] + nums[0]



    if target<smallest_this_trun:#타겟이 최소보다 크다면 지금 거랑 기록해둔거랑 비교해서 리턴
        d = smallest_this_trun - target
        if d > difference:
            print(min_def)#return min_def
        else:
            print(smallest_this_trun)#return smallest_
    elif target > biggest_this_turn:
        min_def = biggest_this_turn
        difference = target - biggest_this_turn
        continue
####################################
    while left < right:
        s = nums[left] + nums[mid] + nums[right]
        d = differ(target, s)
        if difference > d:
            difference = d
            min_def = s
            if d == 0:
                print(s)#return d

        elif s > target:
            if right - 1 == mid:
                break
            right -= 1

        elif s < target:
            if left +1 == mid:
                break
            left += 1
print(min_def)