# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def old(T):
    # write your code in Python 3.6
    s = 0
    m = 0
    l = 0

    for letter in T:
        if letter == 'S':
            s += 1
        if letter == 'M':
            m += 1
        if letter == 'L':
            l += 1
    final = ""

    final = final.ljust(s, 'S')
    final = final.ljust(m + len(final), 'M')
    final = final.ljust(l+ len(final), 'L')

    return final

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6

    def unbalanced_check(S):
        # first we can check for it being unbalanced
        temp = "".join(set(S))

        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


        for letter in lower:
            if letter in temp:
                pos = lower.index(letter)
                if upper[pos] in temp:
                    temp = temp.replace(upper[pos], '')
                    temp = temp.replace(letter, '')

        # if the leftover length after eliminating the pairs is not 0, there was something leftover that did not have a pair
        # this must make it unbalanced
        if len(temp) != 0:
            return -1
        else:
            return 1


    # now that we know the string is balanced
    smallest = len(S)+1
    # a very heavily brute force way to do this is check every possible substring
    # then if it is not unbalanced, compare its length to the current smallest and replace if smaller
    # once every substring is checked, we will have a smallest value

    substrings = [S[i: j] for i in range(len(S)) for j in range(i + 1, len(S) + 1)]

    for el in substrings:
        if unbalanced_check(el) == 1:
            if len(el) < smallest:
                smallest = len(el)

    if smallest == len(S)+1:
        return -1
    else:
        return smallest

