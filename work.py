greet = 'Welcome to Learnfactory!'
students_name = input(f'enter your name ')
print(f'{students_name}! {greet}')
exam_score = float(input('Enter your exam score: '))

if exam_score < 0 or exam_score> 100:
    print(f'{exam_score} is an invalid score')
else:
    if exam_score >=90 or exam_score ==100:
        print(f'{students_name} your score {exam_score}. You got A!')
    elif exam_score>=80 or exam_score ==89:
        print(f'{students_name} your score {exam_score}. You got B')
    elif exam_score >=70 or exam_score ==79:
        print(f'{students_name} your score {exam_score}. You got c')
    elif exam_score>=60 or exam_score ==69:
        print(f'{students_name} your score {exam_score}. You got p')
    elif exam_score >=1 or exam_score ==39:
        print(f'{students_name} your score {exam_score}. You got f')
