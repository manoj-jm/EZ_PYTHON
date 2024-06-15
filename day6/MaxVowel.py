no_person = int(input("enter the number of person : "))
output = []
input_p =[]
res_person = {}

def max_vowel(inp_list):
  vowel = { 'a':0,'e':0,'i':0,'o':0,'u':0}
  sen = inp_list[1]
  for i in sen:
    match(i):
      case 'a': vowel['a']+=1
      case 'e': vowel['e']+=1
      case 'i': vowel['i']+=1
      case 'o': vowel['o']+=1
      case 'u': vowel['u']+=1
  res =[]
  
  x = max(vowel.values())
  for i,j in vowel.items():
    if j == x:
      res.append(i)  
  return res

for i in range(no_person):
  person_sentence = list(map(str,input("enter name with :(colon)and followed by sentence in one line : ").split(':')))
  name = person_sentence[0]
  input_p.append(person_sentence)
  res_person[name]=max_vowel(person_sentence)

print(res_person)
output.append(res_person)

res = max(res_person.values())
for i,j in res_person.items():
  if res == j:
    print("maxium vowels used : " ,i )
    
  





  



