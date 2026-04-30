from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create a hash map where the value is a list
        ans = defaultdict(list)

        for s in strs:
            # 2. Sort the string to create a unique key
            # sorted("eat") returns ['a', 'e', 't'], so we join it
            key = "".join(sorted(s))
            
            # 3. Add the original string to the list for that key
            ans[key].append(s)

        # 4. Return just the values (the groups)
        return list(ans.values())