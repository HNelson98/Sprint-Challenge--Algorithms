'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # counter = word.count("th")
    # return counter
    check = "th"
    wordL = len(word)
    checkL = len(check)

    if (wordL == 0 or wordL < checkL):
        return 0  
        
    if (word[0 : checkL] == check):
        return count_th(word[checkL - 1:]) + 1
    return count_th(word[checkL - 1:])