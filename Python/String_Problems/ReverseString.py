def reverse(str1):
  list1=[]
  str2=""
  for i in range(len(str1)-1,-1,-1):
    list1.append(str1[i])
  return str2.join(list1)
  
print(reverse("My name is anshUMan"))
