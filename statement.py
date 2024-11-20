name_of_student = input("enter your name: ")
print(f"hello {name_of_student}")
pass_mark = int(input('Enter your score: '))

if pass_mark > 50 or pass_mark == 50:
    print(f'hello {name_of_student}. ')
    print('You passed!')

elif pass_mark < 40 or pass_mark == 40:
     print(f"hello, {name_of_student} you.....failed")

else:
     print("loser")




