# https://www.hackerrank.com/challenges/nested-list/
if __name__ == '__main__':
    li = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])
    grades = set(score for name, score in li)
    second_lowest_grade = sorted(grades)[1]
    student_with_second_grade = [name for name, score in li if score == second_lowest_grade]
    student_with_second_grade.sort()
    for name in student_with_second_grade:
        print(name)
