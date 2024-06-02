# https://www.hackerrank.com/challenges/python-tuples/
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tp = tuple(integer_list)
    result = hash(tp)
    print(result)
