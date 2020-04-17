'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    key = "th"
    n1 = len(word)
    n2 = len(key)

    # base case
    # if word = zero or word is greater than length of key, return 0
    if (n1 == 0 or n1 < n2):
        return 0

    # recursive
    # word[0: n2] == [0:2]
    if (word[0: n2] == key):
        print(word[0: n2])
        return count_th(word[n2 - 1:]) + 1

    return count_th(word[n2 - 1:])

print(count_th('xthxth'))