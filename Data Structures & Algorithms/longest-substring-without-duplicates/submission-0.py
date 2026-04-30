class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        # 'right' moves across the string
        for right in range(len(s)):
            # If we hit a duplicate, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character and update max_length
            char_set.add(s[right])
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length