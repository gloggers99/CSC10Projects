students=['dog','cat','zebra','bird','pinguin','fish','whale','tuna']
score=[91,62,82,78,86,74,94,85]

for i in range(0, len(students)):
    for j in range(0, len(score)):
        if score[i] > score[j]:
            score[i], score[j] = score[j], score[i]
            students[i], students[j] = students[j], students[i]

def horiz(dataset):
    for item, amount in dataset.items():
        print(item.rjust(10) + " : " + str(amount) + "%")

horiz(dict(zip(students, score)))