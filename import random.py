i = 1  # 몇번째?
j = 0  # 컴?사람?

def aaa(i,user):
      str_i = str(i)
      for a in range(len(str_i)):
          if str_i[a] == '3' or str_i[a] == '6' or str_i[a] == '9':
            i = int(str_i)
            return  True
      return False



while(i>0):
  if j % 2 == 0:  #사용자
    user = input("사용자: ")
    j +=1
    if not aaa(i,user) :  # 3,6,9 x
       if int(user) == i:
          i += 1
       else:
          break

    elif  aaa(i,user)  :  # 3,6,9 O   aaa true
      if user == "짝":
          i += 1
      else:
          break


  else:  #컴퓨터
      if not aaa(i,user) :  # 3,6,9 x
          print("컴퓨터:",i)
          j +=1
          i += 1

      elif  aaa(i,user) :  # 3,6,9 O   aaa true
          print("컴퓨터:"+"짝")
          j +=1
          i += 1


print("game over")