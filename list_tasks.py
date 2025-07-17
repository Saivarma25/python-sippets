# Mini programs on Lists
#


"""
Flatten nested list - 2 levels
"""

results = []
list1 = [[1,2], [3, 4], [5]]

for x in list1:
    for y in x:
        results.append(y)

print(results)

"""
Remove duplicates without using set
"""
result = []
nums = [1, 2, 2, 3, 4, 4, 5]

for x in nums:
    if x not in result:
        result.append(x)

print(result)

"""
Remove duplicates without using set final
"""
nums = [1, 2, 2, 3, 4, 4, 5]

result = list(dict.fromkeys(nums))
print(result)

"""
Rotate a List to the right or left by K places
"""
nums = [1, 2, 3, 4, 5]
result = []
length = len(nums)
k = int(input("Enter k places: "))

# k = 2 should
for i in range(length):
    if i + k < length:
        result.insert(i + k, nums[i])
    else:
        result.insert((i + k) - length, nums[i])

print(result)

"""
Rotate a List to the right or left by K places final
"""

nums = [1, 2, 3, 4, 5]
result = []
k = int(input("Enter k places to shift:"))
direction = input("Type left for left shift and right for right shift:").lower()

k = k % len(nums)

if direction == 'left':
    result = nums[k:] + nums[:k]
elif direction == 'right':
    result = nums[-k:] + nums[:-k]
else:
    result = nums
    print("Invalid direction, no shift performed")

print(result)

"""
Find all pairs that sum to a target
Duplicate combinations like (2, 5) and (5, 2) both targets to a sum of 7
"""

nums = [2, 3, 4, 5, 7]
result = []
target = input("Enter a target sum: ")
if target.isdigit():
    target = int(target)
else:
    print("Enter valid number")


for x in nums:
    for y in nums:
        if x + y == target:
            result.append((x, y))

print(result)

"""
Find all pairs that sum to a target
"""
result = []
target = input("Enter a target sum: ")
if target.isdigit():
    target = int(target)
else:
    print("Enter valid number")
    exit()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result.append((nums[i], nums[j]))

print(result)


"""
Find all pairs that sum to a target final
"""

pairs = set()
seen = set()

for num in nums:
    compliment = target - num
    if compliment in seen:
        pairs.add(tuple(sorted((num, compliment))))
    seen.add(num)

print(list(pairs))

# Add all items to set
# If missing item is in the set then that should be added to the present item to get total
# missing item and present item should be returned

"""
Create a frequency dict from list
"""
letters = ['a', 'b', 'a', 'c', 'b', 'a']
keys_list = list(dict.fromkeys(letters))
result_dict = {}

for x in keys_list:
    result_dict.update({x : letters.count(x)})

print(result_dict)

"""
Create a frequency dict from list final
"""
result_dict = {}

for letter in letters:
    if letter in result_dict:
        result_dict[letter] += 1
    else:
        result_dict[letter] = 1

print(result_dict)

