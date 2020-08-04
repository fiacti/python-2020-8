a = int(input('how many students in the class:'))
list_score = []
name = []

for i in range(a):
    name_input = input('insert your name:')
    score =int(input('insert test score:'))
    if score not in list_score:
      list_score.append(score)
      name.append(name_input)

highest = 0
for score in range(a):
    if list_score[score] > highest:
        highest = list_score[score]
        high_name = name[score]
print('highest score',highest,high_name)

lowest = 100
for score in range(a):
    if list_score[score] < lowest:
        lowest = list_score[score]
        low_name = name[score]
print('lowest score',lowest,low_name)


sum_score = sum(list_score)
print('class average:',sum_score/a)