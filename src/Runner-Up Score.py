# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l_arr = list(arr)
    if len(l_arr) == n:
        l_arr.sort()
        res = [*set(l_arr)]
        runner = res[-2]
        print(runner)

    else:
        quit()