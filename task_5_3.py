def gen_students(tutors, klasses):
    for i in range(len(tutors)):
        result = (tutors[i], (klasses[i] if i < len(klasses) else None))
        yield result


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']  # , '10А', '10Б', '9А']

student = gen_students(tutors, klasses)
print(gen_students(tutors, klasses))
for _ in range(len(tutors) + 1):
    try:
        print(next(student))
    except StopIteration:
        print("...StopIteration...")
