# https://www.hackerrank.com/challenges/finding-the-percentage/
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s = 0
    length_dict = len(student_marks[query_name])
    for i in student_marks[query_name]:
        s = s + i
    avg = s / length_dict
    print("%.2f" % (float(avg)))

