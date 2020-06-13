def reverse(str1):
  #Check Input
  if(len(str1)==0 or len(str1)==1):
    return "Not Eligible for Reverse"

  list1=[]
  str2=""
  length=len(str1)
  for i in range(length-1,-1,-1):
    list1.append(str1[i])
  return str2.join(list1)

print(reverse("My name is anshUMan"))
