'''
Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 PM and 
will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the party venue 
within this time which takes him P minutes. The contest comprises of N problems that are 
arranged in order of difficulty, with problem 1 being the simplest and problem N being the 
most difficult. Max is aware that he will require 5*i minutes to solve the ith problem.  
Your task is help Max find and return an integer value, representing the number of 
problems Max can solve and reach the party venue within the given time frame of 4 hours.  
Note: Max will leave his home at exactly 8 PM to reach the party venue.  
Input Format:  
input1: An integer value N, representing the total number of problems.  
input2: An integer value P, Representing the time to travel in minutes from his home to the 
party venue.  
Example:  
Input:  
6 180  
Output:  
4'''

time_have = 240 # 4 hours
prob = int(input("enter the no of problems : "))
time= int(input("enter the time has(In minutes) less than 240min  : "))
cnt = 0
remaining = time_have - time 
i=1;
temp_time = remaining
caltime =0
while prob>0 :
  rem_time = remaining - (i*5)
  remaining = rem_time
  i+=1
  prob-=1
  if(remaining<0):
    break
  cnt+=1

print(f"{cnt} problems is solved in given time !")
  