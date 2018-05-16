import statistics 
nums = [8, 8, 8, 8, 8, 4, 4, 3, 3, 3, 1]

j = 0  # initial value of the number to be added
for i in nums:
    j = i + j
k = len(nums)
f = j/k # finding the average
print ("the mean is" ,f)

sort = sorted(nums) # sorts the number in order
the_num = k//2
print ("the median is" ,sort[the_num])

print(statistics.mode(nums))
counts = []
count = 0
indx = 0


"""
for q in nums:
    for t in nums:
        if q == t:
            count += 1
    counts.append(count)
    indx += 1
    count = 0
    
print(counts)

max_cnt = 0
for c in counts:
    if c > max_cnt:
        max_cnt = c

max_indx = counts.index(max_cnt)
print(max_indx)
print("the mode is" ,nums[max_indx])

"""
