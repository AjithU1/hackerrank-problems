# https://www.hackerrank.com/challenges/python-print/problem
if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(1,n+1):
        a = str(i)
        l.append(a)
    b = ''.join(l)
    print(b)
