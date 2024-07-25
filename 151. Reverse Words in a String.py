class Solution:
    def reverseWords(self, s: str) -> str:
        r = []
        word = ""
        for ss in s:
            if ss != " ":
                word += ss
            else:
                if word:
                    r.append(word)
                    word = ""
        if word:
            r.append(word)
        return " ".join(reversed(r))

s = Solution()
print(s.reverseWords("  hello world  "))
print(s.reverseWords("the sky is blue"))