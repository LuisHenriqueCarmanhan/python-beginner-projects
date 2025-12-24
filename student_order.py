from random import shuffle

n1 = input("First student: ")
n2 = input("Second student: ")
n3 = input("Third student: ")
n4 = input("Fourth student: ")

students = [n1, n2, n3, n4]
shuffle(students)
print(students)