def lengthOfLongestSubstring(s: str) -> int:
    # following the 5 am leetcoding guide
    longest = 0
    is_seen = [False for _ in range(255)]

    l = 0
    r = 0
    # expand until condition is violated or end of the string
    while r < len(s):
        idx = get_index(s[r])
        if is_seen[idx]: 
            print(l, r, s[r])
            longest = max(r - l, longest)
            # shrink until condition is not violated
            while is_seen[idx]:
                idx_l = get_index(s[l])
                is_seen[idx_l] = False
                l += 1
            print(l, r)
        is_seen[idx] = True
        r += 1

    return max(r-l, longest)

def get_index(char):
    return ord(char)

def lengthOfLongestSubstring_faster(s: str) -> int:
    # following leetcoding guide on the right 
    indices = {}
    seq = 0
    longest_seq = 0
    start, r = 0, 0

    while r < len(s):
        if indices.get(s[r], None) is None:
            indices[s[r]] = r
        elif indices[s[r]] < start:
            indices[s[r]] = r
        else:
            seq = r - start
            longest_seq = max(seq, longest_seq)
            #print(f"{r}-{start}={seq}, {longest_seq=}")
            start = indices[s[r]] + 1
            indices[s[r]] = r
            
            #print("------")
        r += 1
    #print(f"finished with: max({r - start}, {longest_seq}) = {max(r - start, longest_seq)}")
    #print("------------------------------------------------------------")
    #print()
    return max(r - start, longest_seq)
         
def lengthOfLongestSubstring_slower(s: str) -> int:
    # following leetcoding guide on the right
    freq = [0] * 255 
    longest_seq = 0
    l, r = 0, 0

    while r < len(s):
        
        idx = ord(s[r]) # new letter 
        #print(f"increasing {s[r]}: {freq[idx]} to {freq[idx]+1}")
        freq[idx] += 1
        #print(f"new seq: {sum(freq)}")
        if freq[idx] == 2:
            #print(f"in else")
            longest_seq = max(sum(freq) - 1, longest_seq) 
            while freq[idx] != 1 and l <= r: # run loop until we remove the repeated character
                l_idx = ord(s[l])
                #print(f"decreasing {s[l]}: {freq[l_idx]} to {freq[l_idx]-1}")
                freq[l_idx] -= 1
                l += 1
            freq[idx] = 1

            #print(f"out else, {l=}, sum: {sum(freq)}")
        r += 1
        
    longest_seq = max(sum(freq), longest_seq)
    #print(f"finished with: max({sum(freq)}, {longest_seq}) = {longest_seq}")
    #print("------------------------------------------------------------")
    return longest_seq 



    



s = "pwwkew"
assert lengthOfLongestSubstring("duda") == 3
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("dvffasddf") == 4
assert lengthOfLongestSubstring("dvdf") == 3
assert lengthOfLongestSubstring("aabaab!bb") == 3
print(lengthOfLongestSubstring(s))