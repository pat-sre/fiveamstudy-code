def lengthOfLongestSubstring(s: str) -> int:
    # following leetcoding guide on the right
    freq = [0] * 255 
    longest_seq = 0
    seq = 0
    l, r = 0, 0
    while r < len(s):
        idx = ord(s[r])
        freq[idx] += 1
        if freq[idx] == 2:
            longest_seq = max(longest_seq, sum(freq))
            while l < r:
                idx_l = ord(s[l])
                freq[idx_l] -= 1
                l += 1
                if freq[idx_l] == 1:
                    break
                print(freq)
        r += 1

        
    return max(sum(freq), longest_seq) 



    



s = "dvdf"
#assert lengthOfLongestSubstring(" ") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("aabaab!bb") == 3
print(lengthOfLongestSubstring(s))