def BracketCombinations(num):
    # catalan[i] = number of valid strings you can make with i pairs
    catalan = [0] * (num + 1)
    catalan[0] = 1  # one way to have zero pairs: the empty string

    for k in range(1, num + 1):
        total = 0
        # try every way to split k pairs into "inside" and "after"
        for i in range(k):
            # i pairs go inside the first (), 
            # the other k–1–i pairs go after it
            total += catalan[i] * catalan[k - 1 - i]
        catalan[k] = total  # store the count for k pairs

    return catalan[num]