class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        mn = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < mn:
                mn = len(strs[i])
        prefix = ""
        for i in range(mn):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return prefix
            prefix += char
        return str(prefix)