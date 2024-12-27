import random
print("*****************\nwelcome guess game\n you have 3 chances \nand guess from 1 and 10\n****************")
computer=random.randint(1,10)
name=input("Enter your name: ")
for i in range(3):
  one=int(input(f"{name} you guess b/n 1 and 10:"))
  if one<=10 and one>=1:
      if computer==one:
        print(f"congrats {name} you winner!!!")
      elif computer>one:
        print(f"ohhh {name} your guess is low!! so game over!!")
      elif computer<one:
        print(f"ohhhh {name} your guess is high!1 so game over!!")
      else:
        print("wrong!!!")

  else:
   print(f"sorry {name } your input is wrong!!")
  
