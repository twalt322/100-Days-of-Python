import random

wins = 0
losses = 0
draws = 0

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

while True:
    user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
    computer_choice = random.randint(0,2)

    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    else:
        print('Type either 0, 1, or 2.')
        exit()

    print('Computer chose: \n')
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)

    if user_choice == 0 and computer_choice == 0:
        print('It\'s a draw.')
        draws += 1
    elif user_choice == 0 and computer_choice == 1:
        print('You lose!')
        losses += 1
    elif user_choice == 0 and computer_choice == 2:
        print('You win!')
        wins += 1
    elif user_choice == 1 and computer_choice == 0:
        print('You win!')
        wins += 1
    elif user_choice == 1 and computer_choice == 1:
        print('It\'s a draw.')
        draws += 1
    elif user_choice == 1 and computer_choice == 2:
        print('You lose!')
        losses += 1
    elif user_choice == 2 and computer_choice == 0:
        print('You lose!')
        losses += 1
    elif user_choice == 2 and computer_choice == 1:
        print('You win!')
        wins += 1
    elif user_choice == 2 and computer_choice == 2:
        print('It\'s a draw.')
        draws += 1
    print(f'Your record is {wins} - {losses} - {draws}.')
