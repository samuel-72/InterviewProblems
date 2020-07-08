class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_indices = []
        s_len, p_len = len(s), len(p)
        chars_left_to_be_anagram = p_len
        if s_len < p_len:
            return start_indices
        p_char_freq = {c:0 for c in p} # Keep a map of the freq of characters in the anagram
        for c in p:
            p_char_freq[c] += 1
        window_start_index = 0
        for window_end_index, current_char in enumerate(s):  # Go through each char of the 
            if p_char_freq.get(current_char, 0) > 0:
                chars_left_to_be_anagram -= 1
            # Decrement the chars frequency so that it gets counted for the anagram 
            p_char_freq[current_char] = p_char_freq.get(current_char, 0) - 1
            # Iff the length of the window == length of the anagram string, check if its anagram
            # When the window is slid forward, increase the no of chars needed to be anagram iff its contributing as part of the anagram 
            # When the window is slid forward, increase the char's frequency in the hashmap so that it goes back into the pool
            if window_end_index + 1 - window_start_index == p_len:
                if chars_left_to_be_anagram == 0:
                    start_indices.append(window_start_index)
                if p_char_freq.get(s[window_start_index], 0) >= 0:
                    chars_left_to_be_anagram += 1
                p_char_freq[s[window_start_index]] = p_char_freq.get(s[window_start_index], 0) + 1
                window_start_index += 1

        return start_indices

"""
Input:
s: "cbaebacbacd" p: "abc"

Output:
[0, 4, 5, 6, 7]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 4 is "bac", which is an anagram of "abc".
The substring with start index = 5 is "acb", which is an anagram of "abc".
The substring with start index = 6 is "cba", which is an anagram of "abc".
The substring with start index = 7 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "eeeabeab" p: "ab"

Output:
[3, 6]

Explanation:
The substring with start index = 3 is "ab", which is an anagram of "ab".
The substring with start index = 6 is "ab", which is an anagram of "ab".

"""
