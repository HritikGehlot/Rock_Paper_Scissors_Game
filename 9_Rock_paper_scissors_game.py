import random
print("\tWelcome to rock, paper, scissors\n")
a = random.randint(0, 2)
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
value = [f"Rock: {Rock}", f"Paper: {Paper}", f"Scissors: {Scissors}"]
won = """ 
 __      __   ___    _ __  
 \ \ /\ / /  / _ \  | '_ \ 
  \ V  V /  | (_) | | | | |
   \_/\_/    \___/  |_| |_|
                           
 """

draw = """
  .___                            
  __| _/ _______  _____    __  _  __
 / __ |  \_  __ \ \__  \   \ \/ \/ /
/ /_/ |   |  | \/  / __ \_  \     / 
\____ |   |__|    (____  /   \/\_/  
     \/                \/           
"""

lost = """
_____.___.                   .__                              
\__  |   |   ____    __ __   |  |     ____     ______   ____  
 /   |   |  /  _ \  |  |  \  |  |    /  _ \   /  ___/ _/ __ \ 
 \____   | (  <_> ) |  |  /  |  |__ (  <_> )  \___ \  \  ___/ 
 / ______|  \____/  |____/   |____/  \____/  /____  >  \___  >
 \/                                               \/       \/ 
"""
user_choice = int(input("\tFor rock press 0\n\tFor paper press 1\n\tFor scissors press 2\n"))

computer = value[a]

if user_choice == a:
    print(f"User: {value[user_choice]}")
    print(f"Computer: {computer}")
    print(draw)
elif user_choice == 1 and a== 0:
    print(f"User: {value[user_choice]}")
    print(f"Computer: {computer}")
    print(won)
elif user_choice == 0 and a==2:
    print(f"User: {value[user_choice]}")
    print(f"Computer: {computer}")
    print(won)    
elif user_choice == 2 and a ==1:
    print(f"User: {value[user_choice]}")
    print(f"Computer: {computer}")
    print(won)  
else:
    print(f"User: {value[user_choice]}")
    print(f"Computer: {computer}")
    print(lost)  

