# Sliding Window [Accepted]
# Algorithm
#
# The naive approach is very straightforward. But it is too slow. So how can we optimize it?
#
# In the naive approaches, we repeatedly check a substring to see if it has duplicate character.
# But it is unnecessary. If a substring from index to is already checked to have no duplicate characters. We only need to check if is already in the substring .
#
# To check if a character is already in the substring, we can scan the substring, which leads to an algorithm. But we can do better.
#
# By using HashSet as a sliding window, checking if a character in the current can be done in .
#
# A sliding window is an abstract concept commonly used in array/string problems.
# A window is a range of elements in the array/string which usually defined by the start and end indices,
# i.e. (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction.
# For example, if we slide to the right by element, then it becomes (left-closed, right-open).
#
# Back to our problem. We use HashSet to store the characters in current window ( initially).
# Then we slide the index to the right. If it is not in the HashSet, we slide further.
# Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index .
# If we do this for all , we get our answer.

def lengthOfLongestSubstring(s):
    window_start = 0
    max_length = 0
    char_frequency = {}
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_frequency:
            window_start = max(window_start, char_frequency[right_char]+1)
        char_frequency[right_char] = window_end
        max_length = max(max_length, window_end-window_start+1)
    return max_length
        
