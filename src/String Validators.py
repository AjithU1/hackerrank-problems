# https://www.hackerrank.com/challenges/string-validators/
if __name__ == '__main__':
    s = input()
    ls = m = n = o = p = False
    for i in s:
        if i.isalnum():
            ls = True
        if i.isalpha():
            m = True
        if i.isdigit():
            n = True
        if i.islower():
            o = True
        if i.isupper():
            p = True
    print(f"{ls}\n{m}\n{n}\n{o}\n{p}")


