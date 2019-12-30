nums = [-3,-2,-1,0,0,1,2,3]
target = 0
ret = set()
nums.sort()
n = len(nums)
for start in range(n - 3):
    smallest = nums[start] + nums[start + 1] + nums[start + 2] + nums[start + 3]
    biggest = nums[start] + nums[-2] + nums[ -3] + nums[-1]

    if smallest > target:
        print(ret, "its over")
        break
    if biggest < target:
        continue
    for mid in range(start + 2, n - 1):
        left = start + 1
        right = n - 1
        smallest = nums[start] + nums[mid] + nums[mid + 1] + nums[start + 1]
        biggest = nums[start] + nums[mid] + nums[mid - 1] + nums[-1]

        if smallest > target:
            break
        if biggest < target:
            continue

        while right > mid and left< mid:
            cur_sum = nums[start] + nums[left] + nums[mid] + nums[right]
            if cur_sum<target:
                left += 1
            elif cur_sum > target:
                right -= 1
            elif cur_sum == target:
                el = [nums[start], nums[left], nums[mid], nums[right]]
                el.sort()
                ret.add(tuple(el))
                if mid + 1 == right:
                    left +=1
                elif mid - 1 == left:
                    right -= 1
                else:
                    left +=1
print (ret)