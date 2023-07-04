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

# Write your code below this line 👇
game = [rock, paper, scissors]
person = input("Enter 0 for rock, 1 for paper or 2 for scissors!: ")
cpu = random.randint(0, 2)
print("Person: "+game[int(person)])
print("CPU: "+game[int(cpu)])

if person == '0':
    if cpu == '0':
        print("It's a draw!\n")
    elif cpu == '1':
        print("You lost!\n")
    else:
        print("You won!\n")
elif person == '1':
    if cpu == '0':
        print("You won!\n")
    elif cpu == '1':
        print("It's a draw!\n")
    else:
        print("You lost!\n")
elif person == '2':
    if cpu == '0':
        print("You won!\n")
    elif cpu == '1':
        print("You lost!\n")
    else:
        print("It's a draw!\n")
else:
    print("Bad boy! You can't play like this.\n")