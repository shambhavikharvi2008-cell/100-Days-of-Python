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
import random
print("What do you choose?Type 0 for rock,1 for paper or 2 for scissor")
b=[rock,paper,scissors]
choice=input()
if choice=="":
    print(rock)
    a = random.choice(b)

    print("computer choose:")
    print(a)
    if a == rock:
        print("its draw")
    elif a == scissors:
        print("you win")
    else:
        print("you lose")
elif not choice.isdigit():
    print("undefined")
    a=random.choice(b)
    print("computer choose:")
    print(a)
else:

    if choice=='0':
        print(rock)
        a=random.choice(b)

        print("computer choose:")
        print(a)
        if a==rock:
            print("its draw")
        elif a==scissors:
            print("you win")
        else:
            print("you lose")
    elif choice=='1':
            print(paper)
            a=random.choice(b)
            print("computer choose:")
            print(a)
            if a==rock:
                print("you lose")
            elif a==scissors:
                print("you won")
            else:
                print("its draw")
    elif choice=='2':
                print(scissors)
                a=random.choice(b)
                print("computer choose")
                print(a)
                if a==rock:
                  print("you lose")
                elif a==scissors:
                  print("its draw")


    elif int(choice)>len(b):
            print("you typed an invalid number,you lose!")





