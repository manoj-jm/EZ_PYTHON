# kadens algorithm : to find the maximum sum 

list = [4,-1,-3,6,-2,-1,3,2,-8,-2]
sum_list = sum(list)
cur_sums = 0
max_sum = 0

for i in range(len(list)):
  cur_sums += list[i]
  if max_sum < cur_sums:
    max_sum = cur_sums
  if cur_sums < 0:
    cur_sums = 0

print(max_sum)
  
# leetcode 53
  
      


    
