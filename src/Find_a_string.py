# https://www.hackerrank.com/challenges/find-a-string/
def count_substring(string, sub_string):
    a = []
    for i in range(len(string)):
        b = string.find(sub_string, i, len(string))
        if b != -1 and b not in a:
            a.append(b)

    return len(a)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)