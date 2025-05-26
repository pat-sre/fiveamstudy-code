from typing import List
import string 

def findAnagrams(s: str, p: str) -> List[int]:
    # following the leetcoding guide
    # we will use a sliding window of a fixed len,
    # cause p is given
    l = 0
    r = len(p)
    hashmap = {c:0 for c in string.ascii_lowercase}
    hashmap_substring = {c:0 for c in string.ascii_lowercase}
    
    for c in p:
        hashmap[c] = hashmap.get(c, 0) + 1
    for i in range(len(p)):
        hashmap_substring[s[i]] = hashmap_substring.get(s[i], 0) + 1
    print(hashmap)
    solution = []
    # now we have 2 hashmaps with count of len(p) words 
    # sliding window will add and remove 1 char each
    # we check whether hashmaps are the same, if they are we add a new anagram to solutions
    # check for l == 0 manually
    if is_anagram(hashmap.copy(), s[:len(p)]):
        solution.append(0)
    # count substring in a hashmap?
    # slide the window when condition is violated
    l = 0
    r = len(p)
    while r < len(s):
        # add a new char and remove an old one
        char_r = s[r]
        old_char = s[l]
        hashmap_substring[char_r] = hashmap_substring.get(char_r, 0) + 1
        hashmap_substring[old_char] = hashmap_substring.get(old_char, 0) - 1
        # hashmap == hashmap_substring ? add_l_to_solution : keep on moving
        print(f"{l=}, {hashmap=}\n {hashmap_substring=}\n")
        if is_dict_equal(hashmap, hashmap_substring):
            solution.append(l+1)
        # slide the window
        l += 1
        r += 1
    return solution


def is_anagram(hashmap, string):
    for c in string:
        left = hashmap.get(c, -1)
        if left == 0 or left == -1:
            return False
        hashmap[c] = left - 1
    # did we remove all characters? - i think so hashmap will have sum of len(string) letters 
    return True

def is_dict_equal(dict1, dict2):
    for c in string.ascii_lowercase:
        if dict1[c] != dict2[c]:
            print(f"{c=}: {dict1[c]} != {dict2[c]}")
            return False
    return True

s = "cbaebabacd"
p = "abc"

print(findAnagrams(s, p))