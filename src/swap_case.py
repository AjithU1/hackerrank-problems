# https://www.hackerrank.com/challenges/swap-case/
def swap_case(s):
    res = ''
    for i in s:
        if i.isupper():
            n = i.lower()
            res += n
        elif i.islower():
            n = i.upper()
            res += n
        else:
            res += i
    return res


b = swap_case('HackerRank.com presents "Pythonist 2".')
print(b)
