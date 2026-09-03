import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# print(rock)
choices=[rock,paper,scissors]
computer_choice = random.choice(choices)

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
if your_choice not in [0,1,2]:
    print("You typed an invalid number. You lose")
else:
    print(choices[your_choice])
    print("Computer chose:\n",computer_choice)

    if choices[your_choice] == computer_choice:
        print("It's a tie!")
    elif choices[your_choice] == rock and computer_choice == paper:
        print("You lose")
    elif choices[your_choice] == rock and computer_choice == scissors:
        print("You win")
    elif choices[your_choice] == paper and computer_choice == rock:
        print("You win")
    elif choices[your_choice] == paper and computer_choice == scissors:
        print("You lose")
    elif choices[your_choice] == scissors and computer_choice == paper:
        print("You win")
    elif choices[your_choice] == scissors and computer_choice == rock:
        print("You lose")
    else:
        print("You typed an invalid number. You lose")
