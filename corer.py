question=[["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1],
          ["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1],
         ["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1],
          ["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1],
          ["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1],
          ["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1],
          ["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1],
          ["what is the name of this country ","1.india","2.pakistan","3.america","4.china",1]
         ]

money=["1,000","2,000","3,000","5,000","10,000","20,000","40,000","80,000","1,60,000","3,20,000","6,40,000","1,250,000","25,00,000","50,00,000","1,Crore"]
moneys=0
for i in range(0,len(question)):
  questions=question[i][0]
  print(f"Question of \u20B9 {money[i]}")
  print(f"{i+1}, {questions}")
  print(f"{question[i][1:4]}")
  n=int(input("please enter the right anwser b/w 1 to 4 :-  "))
  if(n!=0 and n>5):
    print("please enter the valid number ")
  if(n==question[i][-1]):
    print("this is  right anwser")
  else:
    print("your are lose the game")
    break
  
  if(i==4):
    moneys=10000
  elif(i==10):
    moneys=3,20,000
  elif(i==15):
    moneys="1 Crore"
print(f"this is the final amount you win  {moneys}")
  