a=int(input("Please enter 1 for Encoding or 2 for Decoding : "))
if a==1:
  b=input("enter message for encoding - ")
  if len(b)<=3:
    print(b[::-1])
  else:
    if len(b)%2!=0:
      print(b[::-2],b[1::2])
    else:
      print(b[::-2],b[::2])

elif a==2:
  b=input("enter message for decoding - ")
  if len(b)<=3:
    print(b[::-1])
  else:
    if len(b)%2!=0:
      c=len(b)//2
      d=b[c::-1]
      e=b[c+1::]
      e+="."
      for i,j in zip(d,e):
        print(i+j,end="")
    elif len(b)%2==0:
      c=len(b)//2
      d=b[c-1::-1]
      e=b[c::]
      for i,j in zip(d,e):
        print(j+i,end="")
      
else:
  print("sorry it could not be understood, i am a beginner so if you want to leave an input, i will appreciate it.")
  x=input("Enter your input here - ")
  print("thanks for your input.")