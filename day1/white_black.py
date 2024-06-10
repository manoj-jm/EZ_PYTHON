cordinate  = input("enter the coordinate of chessboard :")

#4 w b w b
#3 b w b w
#2 w b w b
#1 b w b w
#  a b c d

even_rows = '2468'
odd_rows = '1357'

even_col = 'bdfh'
odd_col = 'aceg'
# a1
if cordinate[0] in odd_col:
  if cordinate[1] in odd_rows:
    print('black')
  else:
    print('white')
else:
  if cordinate[0] in even_rows:
    print('white')
  else:
    print('black')




