# kadens algorithm : to find the maximum sum 

list = [4,-1,-3,6,-2,-1,3,2,-8,-2]
sum_list = sum(list)
cur_sums = list[0]
max_sum = list[0]

# for i in range(1,len(list)):
#   cur_sums += list[i]
#   if max_sum < cur_sums:
#     max_sum = cur_sums
#   if cur_sums < 0:
#     cur_sums = 0

# print(max_sum)
  
# leetcode 53
  
max_so_far = list[0]
max_end = list[0]

for i in range(1,len(list)):
  max_end +=list[i]
  max_so_far = max(max_so_far,max_end)
  if max_end < 0:
    max_end = 0

print(max_so_far)
  

    
