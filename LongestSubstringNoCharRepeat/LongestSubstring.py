def solve (input_string):
    '''
        Given a string s, find the length of the longest substring without repeating characters

        ex.
        Input: s = "abcabcbb"
        Output: 3
    '''
    string_list = list(input_string)
    compare_set = set()
    left = 0
    max_len = 0
    print(string_list)

    for right in range(len(string_list)):
        print(compare_set)
        if string_list[right] in compare_set:
            while left < right:
                compare_set.pop()
                left+=1
        
        '''
        # This is a different loop that can be used for the same result
        while string_list[right] in compare_set:
           compare_set.remove(string_list[left])
           left +=1
        '''
        
        compare_set.add(string_list[right])
        max_len = max(max_len, right - left + 1)
        

    return max_len


print(solve("abcabcbb"))  # 3
print(solve("bbbbb"))     # 1
print(solve("pwwkew"))    # 3